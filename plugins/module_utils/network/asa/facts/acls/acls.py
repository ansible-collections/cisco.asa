#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The asa_acls fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


from copy import deepcopy
import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.utils.utils import (
    check_n_return_valid_ipv6_addr,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.argspec.acls.acls import (
    AclsArgs,
)


class AclsFacts(object):
    """ The asa_acls fact class
    """

    def __init__(self, module, subspec="config", options="options"):

        self._module = module
        self.argument_spec = AclsArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_acls_data(self, connection):
        return connection.get("sh access-list")

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for acls
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        objs = []
        if not data:
            data = self.get_acls_data(connection)
        # operate on a collection of resource x
        config = data.split("\n")
        spec = {"acls": None, "afi": None}

        if config:
            obj = self.render_config(spec, config)
            if obj:
                objs.append(obj)
        facts = {}

        if objs:
            facts["acls"] = []
            params = utils.validate_config(
                self.argument_spec, {"config": objs}
            )
            for cfg in params["config"]:
                facts["acls"].append(utils.remove_empties(cfg))
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts

    def populate_port_protocol(self, source, destination, each_list):
        """ Function Populates port portocol wrt to source and destination
        :param acls: source config
        :param config: destination config
        :param each_list: config
        :rtype: A list
        :returns: the commands generated based on source and destination params
        """
        operators = ["eq", "gt", "lt", "neq", "range"]
        for item in operators:
            if item in each_list:
                if (
                    source.get("address")
                    or source.get("any")
                    or source.get("host")
                    and not source.get("port_protocol")
                    or source.get("object_group_network")
                    or source.get("interface")
                ):
                    index = each_list.index(item)
                    try:
                        source_index = each_list.index(source.get("address"))
                    except ValueError:
                        try:
                            source_index = each_list.index(source.get("host"))
                        except ValueError:
                            try:
                                source_index = each_list.index(
                                    source.get("object_group_network")
                                )
                            except ValueError:
                                try:
                                    source_index = each_list.index(
                                        source.get("interface")
                                    )
                                except ValueError:
                                    source_index = each_list.index("any")
                    if source.get("address"):
                        if (
                            source_index + 2
                        ) == index and ":" not in source.get("address"):
                            source["port_protocol"] = {
                                item: each_list[index + 1]
                            }
                            each_list.remove(item)
                            del each_list[index]
                        elif (source_index + 1) == index and ":" in source.get(
                            "address"
                        ):
                            source["port_protocol"] = {
                                item: each_list[index + 1]
                            }
                            each_list.remove(item)
                            del each_list[source_index]
                            del each_list[index - 1]
                    else:
                        if (source_index + 1) == index:
                            source["port_protocol"] = {
                                item: each_list[index + 1]
                            }
                            each_list.remove(item)
                    if source.get("any"):
                        del each_list[source_index]
                    elif (
                        source.get("host")
                        or source.get("object_group_network")
                        or source.get("interface")
                    ):
                        del each_list[source_index]
                        del each_list[source_index - 1]
                if (
                    destination.get("address")
                    or destination.get("any")
                    or destination.get("host")
                    or destination.get("object_group_network")
                    or destination.get("interface")
                ):
                    index = each_list.index(item)
                    try:
                        destination_index = each_list.index(
                            destination.get("address")
                        )
                    except ValueError:
                        try:
                            destination_index = each_list.index(
                                destination.get("host")
                            )
                        except ValueError:
                            try:
                                destination_index = each_list.index(
                                    destination.get("object_group_network")
                                )
                            except ValueError:
                                try:
                                    destination_index = each_list.index(
                                        destination.get("interface")
                                    )
                                except ValueError:
                                    destination_index = each_list.index("any")
                    if (destination_index + 1) == index or (
                        destination_index + 2
                    ) == index:
                        destination["port_protocol"] = {
                            item: each_list[index + 1]
                        }
                        each_list.remove(item)
                        del each_list[index]
                break
        if (
            "eq" in each_list
            or "gt" in each_list
            or "lt" in each_list
            or "neq" in each_list
            or "range" in each_list
        ):
            self.populate_port_protocol(source, destination, each_list)

    def populate_source_destination(self, each, source, destination):
        each_list = each.split(" ")
        if "permit" in each:
            grant_index = each_list.index("permit")
        elif "deny" in each:
            grant_index = each_list.index("deny")
        if "any" in each:
            any = len(re.findall("any", each))
            if any == 2:
                source["any"] = True
                destination["any"] = True
            elif any == 1:
                any_index = each_list.index("any")
                if grant_index + 2 == any_index:
                    source["any"] = True
                else:
                    destination["any"] = True
        if "host" in each:
            host = re.findall(r"host\s[0-9]+(?:\.[0-9]+){3}", each)
            if len(host) == 2:
                each_split = each.split(" ")
                host_index = each_split.index("host")
                source["host"] = each_split[host_index + 1]
                del each_split[host_index]
                host_index = each_split.index("host")
                destination["host"] = each_split[host_index + 1]
            elif len(host) == 1:
                host_ip = host[0].split(" ")[1]
                host_index = each_list.index("host")
                if host_index == (grant_index + 2):
                    source["host"] = host_ip
                else:
                    destination["host"] = host_ip
        if "object-group" in each:
            object_group_network = re.findall(r"object-group\s\S+", each)
            if object_group_network:
                if len(object_group_network) == 2:
                    source["object_group_network"] = object_group_network[
                        0
                    ].split(" ")[1]
                    destination["object_group_network"] = object_group_network[
                        1
                    ].split(" ")[1]
                elif len(object_group_network) == 1:
                    if each.index("object-group") == grant_index + 2:
                        source["object_group_network"] = object_group_network[
                            0
                        ].split(" ")[1]
                    else:
                        destination[
                            "object_group_network"
                        ] = object_group_network[0].split(" ")[1]
        if "interface" in each:
            interface = re.findall(r"interface\s\S+", each)
            if interface:
                if len(interface) == 2:
                    source["interface"] = interface[0].split(" ")[1]
                    destination["interface"] = interface[1].split(" ")[1]
                elif len(interface) == 1:
                    if each.index("interface") == grant_index + 2:
                        source["interface"] = interface[0].split(" ")[1]
                    else:
                        destination["interface"] = interface[0].split(" ")[1]
        if ":" in each:
            temp_ipv6 = []
            check_n_return_valid_ipv6_addr(self._module, each_list, temp_ipv6)
            count = 0
            for every in each_list:
                if len(temp_ipv6) == 2:
                    if temp_ipv6[0] in every or temp_ipv6[1] in every:
                        temp_ipv6[count] = every
                        count += 1
                elif len(temp_ipv6) == 1:
                    if temp_ipv6[0] in every:
                        temp_ipv6[count] = every
            if "any" in each_list:
                if destination["any"]:
                    source["address"] = temp_ipv6[0]
                elif source["any"]:
                    destination["address"] = temp_ipv6[0]
            elif len(temp_ipv6) == 2:
                source["address"] = temp_ipv6[0]
                destination["address"] = temp_ipv6[1]
        else:
            ip_n_netmask = re.findall(r"[0-9]+(?:\.[0-9]+){3}", each)
            if len(ip_n_netmask) == 2:
                if (
                    destination.get("any") or destination.get("host")
                ) and not (source.get("any") or source.get("host")):
                    source["address"] = ip_n_netmask[0]
                    source["netmask"] = ip_n_netmask[1]
                elif (source.get("any") or source.get("host")) and not (
                    source.get("any") or source.get("host")
                ):
                    destination["address"] = ip_n_netmask[0]
                    destination["netmask"] = ip_n_netmask[1]
            elif len(ip_n_netmask) == 4:
                source["address"] = ip_n_netmask[0]
                source["netmask"] = ip_n_netmask[1]
                destination["address"] = ip_n_netmask[2]
                destination["netmask"] = ip_n_netmask[3]

    def render_config(self, spec, have_config):
        """
        Render config as dictionary structure and delete keys
          from spec for null values
        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)
        config["acls"] = []
        acls = {}
        aces = []
        temp_name = ""
        object_group_line = None
        for each in have_config:
            each_list = each.split(" ")
            if "access-list" in each:
                temp_index = each_list.index("access-list")
                name = (each_list[temp_index + 1]).split(";")[0]
                if temp_name != name:
                    if acls:
                        config["acls"].append(acls)
                        acls = dict()
                        aces = list()
                    temp_name = name
                if name != "cached":
                    acls["name"] = name
            if "line" not in each:
                continue
            if temp_name in each:
                ace_options = {}
                line = utils.parse_conf_arg(each, "line")
                if line:
                    ace_options["line"] = line.split(" ")[0]
                remark = utils.parse_conf_arg(each, "remark")
                if remark:
                    ace_options["remark"] = remark.split(" ")[0]
                if "extended" in each:
                    acls["acl_type"] = "extended"
                elif "standard" in each:
                    acls["acl_type"] = "standard"
                if utils.parse_conf_arg(each, "permit"):
                    ace_options["grant"] = "permit"
                elif utils.parse_conf_arg(each, "deny"):
                    ace_options["grant"] = "deny"
                if "inactive" in each:
                    ace_options["inactive"] = True
                time_range = utils.parse_conf_arg(each, "time-range")
                if time_range:
                    ace_options["time_range"] = time_range.split(" ")[0]

                protocol_option = [
                    "ah",
                    "eigrp",
                    "esp",
                    "gre",
                    "icmp",
                    "icmp6",
                    "igmp",
                    "igrp",
                    "ip",
                    "ipinip",
                    "ipsec",
                    "nos",
                    "ospf",
                    "pcp",
                    "pim",
                    "pptp",
                    "sctp",
                    "snp",
                    "tcp",
                    "udp",
                ]

                icmp_options = [
                    "alternate_address",
                    "conversion_error",
                    "echo",
                    "echo_reply",
                    "information_reply",
                    "information_request",
                    "mask_reply",
                    "mask_request",
                    "mobile_redirect",
                    "parameter_problem",
                    "redirect",
                    "router_advertisement",
                    "router_solicitation",
                    "source_quench",
                    "time_exceeded",
                    "timestamp_reply",
                    "timestamp_request",
                    "traceroute",
                    "unreachable",
                ]
                icmp6_options = [
                    "echo",
                    "echo_reply",
                    "membership_query",
                    "membership_reduction",
                    "membership_report",
                    "neighbor_advertisement",
                    "neighbor_redirect",
                    "neighbor_solicitation",
                    "packet_too_big",
                    "parameter_problem",
                    "router_advertisement",
                    "router_renumbering",
                    "router_solicitation",
                    "time_exceeded",
                    "unreachable",
                ]

                temp_option = ""
                for option in protocol_option:
                    if option in each_list:
                        temp_option = option
                        if temp_option == "icmp":
                            temp_flag = [
                                each_option
                                for each_option in icmp_options
                                if each_option.replace("_", "-") in each
                            ]
                            if temp_flag:
                                flag = temp_flag[0]
                                if flag in each_list:
                                    pass  # each_list.remove(flag)
                                temp_flag = flag
                        if temp_option == "icmp6":
                            temp_flag = [
                                each_option
                                for each_option in icmp6_options
                                if each_option.replace("_", "-") in each
                            ]
                            if temp_flag:
                                flag = temp_flag[0]
                                if flag in each_list:
                                    pass  # each_list.remove(flag)
                                temp_flag = flag
                        break
                log = utils.parse_conf_arg(each, "log")
                if log:
                    ace_options["log"] = log.split(" ")[0]
                time_range = utils.parse_conf_arg(each, "time_range")
                if time_range:
                    ace_options["time_range"] = time_range.split(" ")[0]

                source = {}
                destination = {}
                line = re.findall(r"line\s(?P<line>\d+)", each)[0]
                if "object-group " in each:
                    object_group_line = line
                    self.populate_source_destination(each, source, destination)
                if line != object_group_line:
                    self.populate_source_destination(each, source, destination)
                    object_group_line = None

                if source.get("address") and source.get(
                    "address"
                ) == destination.get("address"):
                    self._module.fail_json(
                        msg="Source and Destination address cannot be same!"
                    )
                elif source and destination:
                    self.populate_port_protocol(source, destination, each_list)

                if source:
                    ace_options["source"] = source
                if destination:
                    ace_options["destination"] = destination
                if temp_option:
                    protocol_options = {}
                    ace_options["protocol"] = temp_option
                    if temp_option == "icmp":
                        icmp = dict()
                        if temp_flag:
                            icmp[temp_flag] = True
                        protocol_options[temp_option] = icmp
                    elif temp_option == "icmp6":
                        icmp6 = dict()
                        if temp_flag:
                            icmp6[temp_flag] = True
                        protocol_options[temp_option] = icmp6
                    else:
                        protocol_options[temp_option] = True
                    ace_options["protocol_options"] = protocol_options
                if not ace_options.get("source") and not ace_options.get(
                    "destination"
                ):
                    continue
                aces.append(ace_options)
                acls["aces"] = aces
            else:
                config["acls"].append(acls)
        if acls:
            config["acls"].append(acls)

        return utils.remove_empties(config)
