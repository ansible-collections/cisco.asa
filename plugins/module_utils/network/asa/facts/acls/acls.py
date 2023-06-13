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
                index = each_list.index(item)
                if (
                    source.get("address")
                    or source.get("any")
                    or source.get("host")
                    and not source.get("port_protocol")
                ):
                    try:
                        source_index = each_list.index(source.get("address"))
                    except ValueError:
                        try:
                            source_index = each_list.index("any")
                        except ValueError:
                            source_index = each_list.index("host")
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
                    elif source.get("any"):
                        if (source_index + 1) == index:
                            source["port_protocol"] = {
                                item: each_list[index + 1]
                            }
                            each_list.remove(item)
                            del each_list[source_index]
                            del each_list[index - 1]
                    elif source.get("host"):
                        if (source_index + 1) == index:
                            source["port_protocol"] = {
                                item: each_list[index + 1]
                            }
                            each_list.remove(item)
                            del each_list[index - 1]
                        del each_list[source_index]
                if (
                    destination.get("address")
                    or source.get("any")
                    or destination.get("host")
                ):
                    try:
                        destination_index = each_list.index(
                            destination.get("address")
                        )
                    except ValueError:
                        try:
                            destination_index = each_list.index("any")
                        except ValueError:
                            destination_index = each_list.index("host") + 1
                            index -= 1
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
        if "any" in each:
            any = re.findall("any", each)
            if len(any) == 2:
                source["any"] = True
                destination["any"] = True
        elif "host" in each:
            host = re.findall("host", each)
            if len(host) == 2:
                host_index = each.index("host")
                source["host"] = each[host_index + 1]
                del each[host_index]
                host_index = each.index("host")
                destination["host"] = each[host_index + 1]
            else:
                ip_n_wildcard_bits = re.findall(r"[0-9]+(?:\.[0-9]+){3}", each)
                ip_index = None
                if ip_n_wildcard_bits:
                    ip_index = each.index(ip_n_wildcard_bits[0])
                host_index = each.index("host")
                if ip_index:
                    if host_index < ip_index:
                        source["host"] = each(host_index + 1)
                        destination["address"] = ip_n_wildcard_bits[0]
                        destination["netmask"] = ip_n_wildcard_bits[1]
                    elif host_index > ip_index:
                        destination["host"] = each(host_index + 1)
                        source["address"] = ip_n_wildcard_bits[0]
                        source["netmask"] = ip_n_wildcard_bits[1]
        else:
            if ":" in each:
                temp_ipv6 = []
                each = each.split(" ")
                check_n_return_valid_ipv6_addr(self._module, each, temp_ipv6)
                count = 0
                for every in each:
                    if len(temp_ipv6) == 2:
                        if temp_ipv6[0] in every or temp_ipv6[1] in every:
                            temp_ipv6[count] = every
                            count += 1
                    elif len(temp_ipv6) == 1:
                        if temp_ipv6[0] in every:
                            temp_ipv6[count] = every
                if "any" in each:
                    if each.index("any") > each.index(temp_ipv6[0]):
                        source["address"] = temp_ipv6[0]
                        destination["any"] = True
                    elif each.index("any") < each.index(temp_ipv6[0]):
                        source["any"] = True
                        destination["address"] = temp_ipv6[0]
                elif len(temp_ipv6) == 2:
                    source["address"] = temp_ipv6[0]
                    destination["address"] = temp_ipv6[1]
            else:
                ip_n_netmask = re.findall(r"[0-9]+(?:\.[0-9]+){3}", each)
                if len(ip_n_netmask) == 0 and len(any) == 1:
                    source["any"] = True
                elif len(ip_n_netmask) == 1:
                    source["address"] = ip_n_netmask[0]
                elif len(ip_n_netmask) == 2:
                    if "any" in each:
                        if each.index("any") > each.index(ip_n_netmask[0]):
                            source["address"] = ip_n_netmask[0]
                            source["netmask"] = ip_n_netmask[1]
                            destination["any"] = True
                        elif each.index("any") < each.index(ip_n_netmask[0]):
                            source["any"] = True
                            destination["address"] = ip_n_netmask[0]
                            destination["netmask"] = ip_n_netmask[1]
                    else:
                        source["address"] = ip_n_netmask[0]
                        source["netmask"] = ip_n_netmask[1]
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
                    "ipsec" "nos",
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
                self.populate_source_destination(each, source, destination)

                if source.get("address") and source.get(
                    "address"
                ) == destination.get("address"):
                    self._module.fail_json(
                        msg="Source and Destination address cannot be same!"
                    )
                else:
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

                aces.append(ace_options)
                acls["aces"] = aces
            else:
                config["acls"].append(acls)
        if acls:
            config["acls"].append(acls)

        return utils.remove_empties(config)
