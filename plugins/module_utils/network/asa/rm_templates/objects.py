# -*- coding: utf-8 -*-
# Copyright 2025 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Asa_objects parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


def _tmplt_service(config_data):
    if config_data.get("service"):
        service = config_data.get("service")
        cmd = "service {protocol}".format(**service)
        if service.get("source_port"):
            if service["source_port"].get("range"):
                cmd += " source range {start} {end}".format(
                    **service["source_port"]["range"],
                )
            else:
                key = list(service["source_port"])[0]
                cmd += " source {0} {1}".format(
                    key,
                    service["source_port"][key],
                )
        if service.get("destination_port"):
            if service["destination_port"].get("range"):
                cmd += " destination range {start} {end}".format(
                    **service["destination_port"]["range"],
                )
            else:
                key = list(service["destination_port"])[0]
                cmd += " destination {0} {1}".format(
                    key,
                    service["destination_port"][key],
                )
        if service.get("icmpopt"):
            if service["icmpopt"].get("name"):
                cmd += " {0}".format(
                    service["icmpopt"]["name"],
                )
            if service["icmpopt"].get("code"):
                cmd += " {0}".format(
                    service["icmpopt"]["code"],
                )
        return cmd


def _tmplt_nat(config_data):
    if config_data.get("nat"):
        nat = config_data.get("nat")
        cmd = "nat"
        if nat.get("real_if"):
            cmd += " ({real_if},{mapped_if})".format(**nat)
        if nat.get("dynamic"):
            cmd += " dynamic"
            if nat["dynamic"].get("name"):
                cmd += " {name}".format(**nat["dynamic"])
            elif nat["dynamic"].get("pat_pool"):
                cmd += " pat-pool"
                pp = nat["dynamic"].get("pat_pool")
                if pp.get("name"):
                    cmd += " {name}".format(**pp)
                    if pp.get("block_allocation"):
                        cmd += " block-allocation"
                    elif pp.get("extended"):
                        cmd += " extended"
                if pp.get("interface"):
                    cmd += " interface"
                    if pp["interface"].get("ipv6"):
                        cmd += " ipv6"
                if pp.get("flat"):
                    cmd += " flat"
                if pp.get("include_reserve"):
                    cmd += " include-reserve"
                if pp.get("round_robin"):
                    cmd += " round-robin"
            if nat["dynamic"].get("interface"):
                cmd += " interface"
                if nat["dynamic"]["interface"].get("ipv6"):
                    cmd += " ipv6"
            if nat["dynamic"].get("dns"):
                cmd += " dns"
        if nat.get("static"):
            cmd += " static"
            if nat["static"].get("name"):
                cmd += " {name}".format(**nat["static"])
            elif nat["static"].get("interface"):
                cmd += " interface"
                if nat["static"]["interface"].get("ipv6"):
                    cmd += " ipv6"
            if nat["static"].get("net_to_net"):
                cmd += " net-to-net"
            if nat["static"].get("dns"):
                cmd += " dns"
            if nat["static"].get("no_proxy_arp"):
                cmd += " no-proxy-arp"
            if nat["static"].get("route_lookup"):
                cmd += " route-lookup"
            if nat["static"].get("service"):
                cmd += " service {protocol} {real_port} {mapped_port}".format(
                    **nat["static"]["service"],
                )
        return cmd


class ObjectsTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(ObjectsTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "obj_name",
            "getval": re.compile(
                r"""
                ^object\s
                \s*(?P<obj_type>\S+)*
                \s*(?P<obj_name>\S+)*
                $""", re.VERBOSE,
            ),
            "setval": "object {{ object_type }} {{ name }}",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {
                            "object_type": "{{ obj_type }}",
                            "name": "{{ obj_name }}",
                        },
                    },
                },
            },
            "shared": True,
        },
        {
            "name": "description",
            "getval": re.compile(
                r"""\s+description:*
                    \s*(?P<description>.+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": "description {{ description }}",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"description": "{{ description }}"},
                    },
                },
            },
        },
        {
            "name": "obj_host",
            "getval": re.compile(
                r"""\s+host\s
                    \s*(?P<host>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": "host {{host}}",
            "compval": "host",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"host": "{{ host }}"},
                    },
                },
            },
        },
        {
            "name": "obj_subnet",
            "getval": re.compile(
                r"""\s+subnet\s
                    \s*(?P<subnet>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
                    *$""",
                re.VERBOSE,
            ),
            "setval": "subnet {{ subnet }}",
            "compval": "subnet",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"subnet": "{{ subnet }}"},
                    },
                },
            },
        },
        {
            "name": "obj_range",
            "getval": re.compile(
                r"""\s+range\s
                    \s*(?P<range>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
                    *$""",
                re.VERBOSE,
            ),
            "setval": "range {{ range }}",
            "compval": "range",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"range": "{{ range }}"},
                    },
                },
            },
        },
        {
            "name": "obj_fqdn_v4",
            "getval": re.compile(
                r"""\s+fqdn\s+v4\s
                    \s*(?P<fqdn_v4>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": "fqdn v4 {{ fqdn_v4 }}",
            "compval": "fqdn_v4",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"fqdn_v4": "{{ fqdn_v4 }}"},
                    },
                },
            },
        },
        {
            "name": "obj_fqdn_v6",
            "getval": re.compile(
                r"""\s+fqdn\s+v6\s
                    \s*(?P<fqdn_v6>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": "fqdn v6 {{ fqdn_v6 }}",
            "compval": "fqdn_v6",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {
                            "fqdn_v6": "{{ fqdn_v6 }}",
                        },
                    },
                },
            },
        },
        {
            "name": "obj_fqdn",
            "getval": re.compile(
                r"""\s+fqdn\s
                    \s*(?P<fqdn>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": "fqdn {{ fqdn }}",
            "compval": "fqdn",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {
                            "fqdn": "{{ fqdn }}",
                        },
                    },
                },
            },
        },
        {
            "name": "obj_nat",
            "getval": re.compile(
                r"""\s+nat\s
                    \s*(\((?P<nat_real_if>[^,]+),(?P<nat_mapped_if>[^)]+)\))*
                    \s*(dynamic\s+pat-pool\s+(?P<dnat_pp_name>\S+)(?P<dnat_pp_if>(\s+interface)?)(?P<dnat_pp_if_v6>(\s+ipv6)?)(?P<dnat_pp_opts>(\s+.*)?))*
                    \s*(dynamic\s+(?P<dnat_name>\S+)(?P<dnat_if>(\s+interface)?)(?P<dnat_if_v6>(\s+ipv6)?)(?P<dnat_dns>(\s+dns)?))*
                    \s*(static\s+(?P<snat_name>\S+)(?P<snat_if>(\s+interface)?)(?P<snat_if_v6>(\s+ipv6)?)(?P<snat_opts>(\s+(dns|net-to-net|no-proxy-arp|route-lookup))*)(\s+service\s+(?P<snat_proto>(tcp|udp|sctp))\s+(?P<snat_rport>\S+)\s+(?P<snat_mport>\S+))?\s*)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_nat,
            "compval": "nat",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {
                            "nat": {
                                "real_if": "{{ nat_real_if }}",
                                "mapped_if": "{{ nat_mapped_if }}",
                                "dynamic": {
                                    "name": "{{ dnat_name if dnat_name and dnat_name != 'interface' }}",
                                    "interface": {
                                        "ipv6": "{{ True if dnat_if_v6 else False if dnat_name == 'interface' or dnat_if else None }}",
                                    },
                                    "pat_pool": {
                                        "name": "{{ dnat_pp_name if dnat_pp_name and dnat_pp_name != 'interface' }}",
                                        "interface": {
                                            "ipv6": "{{ True if dnat_pp_if_v6 else False if dnat_pp_name == 'interface' or dnat_pp_if else None }}",
                                        },
                                        "flat": "{{ True if 'flat' in dnat_pp_opts else None }}",
                                        "include_reserve": "{{ True if 'include-reserve' in dnat_pp_opts else None }}",
                                        "round_robin": "{{ True if 'round-robin' in dnat_pp_opts else None }}",
                                        "block_allocation": "{{ True if 'block-allocation' in dnat_pp_opts else None }}",
                                        "extended": "{{ True if 'extended' in dnat_pp_opts else None }}",
                                    },
                                    "dns": "{{ True if dnat_dns else None }}",
                                },
                                "static": {
                                    "name": "{{ snat_name if snat_name and snat_name != 'interface' }}",
                                    "interface": {
                                        "ipv6": "{{ True if snat_if_v6 else False if snat_name == 'interface' or snat_if else None }}",
                                    },
                                    "service": {
                                        "protocol": "{{ snat_proto }}",
                                        "real_port": "{{ snat_rport }}",
                                        "mapped_port": "{{ snat_mport }}",
                                    },
                                    "net_to_net": "{{ True if 'net-to-net' in snat_opts else None }}",
                                    "dns": "{{ True if 'dns' in snat_opts else None }}",
                                    "no_proxy_arp": "{{ True if 'no-proxy-arp' in snat_opts else None }}",
                                    "route_lookup": "{{ True if 'route-lookup' in snat_opts else None }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "obj_service",
            "getval": re.compile(
                r"""\s+service\s
                    \s*(?P<protocol>\S+)
                    \s*(?P<source_port>source\s((eq|gts|lt|neq)\s(\S+|\d+)|(range\s(\S+|\S+)\s(\S+|\S+))))*
                    \s*(?P<destination_port>destination\s((eq|gt|lt|neq)\s(\S+|\d+)|(range\s(\S+|\S+)\s(\S+|\S+))))*
                    \s*(?P<icmpopt>(alternate-address|conversion-error|echo(-reply)?|information-(reply|request)|mask-(reply|request)|membership-(query|reduction|report)|mobile-redirect|neighbor-(advertisement|redirect|solicitation)|packet-too-big|parameter-problem|redirect|router-(advertisement|solicitation|renumbering)|source-quench|time-exceeded|timestamp-(reply|request)|traceroute|unreachable)(\s+\d+)?)
                    *""",
                re.VERBOSE,
            ),
            "setval": _tmplt_service,
            "compval": "service",
            "result": {
                "objects": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {
                            "service": {
                                "protocol": "{{ protocol }}",
                                "source_port": {
                                    "eq": "{{ source_port.split(' ')[2] if source_port is defined and\
                                        'eq' in source_port and 'range' not in source_port }}",
                                    "gt": "{{ source_port.split(' ')[2] if source_port is defined and\
                                        'gt' in source_port and 'range' not in source_port }}",
                                    "lt": "{{ source_port.split(' ')[2] if source_port is defined and\
                                        'lt' in source_port and 'range' not in source_port }}",
                                    "neq": "{{ source_port.split(' ')[2] if source_port is defined and\
                                        'neq' in source_port and 'range' not in source_port }}",
                                    "range": {
                                        "start": "{{ source_port.split('range ')[1].split(' ')[0] if source_port is defined and\
                                            'range' in source_port else None }}",
                                        "end": "{{ source_port.split('range ')[1].split(' ')[1] if source_port is defined and\
                                            'range' in source_port else None }}",
                                    },
                                },
                                "destination_port": {
                                    "eq": "{{ destination_port.split(' ')[2] if destination_port is defined and\
                                        'eq' in destination_port and 'range' not in destination_port }}",
                                    "gt": "{{ destination_port.split(' ')[2] if destination_port is defined and\
                                        'gt' in destination_port and 'range' not in destination_port }}",
                                    "lt": "{{ destination_port.split(' ')[2] if destination_port is defined and\
                                        'lt' in destination_port and 'range' not in destination_port }}",
                                    "neq": "{{ destination_port.split(' ')[2] if destination_port is defined and\
                                        'neq' in destination_port and 'range' not in destination_port }}",
                                    "range": {
                                        "start": "{{ destination_port.split('range ')[1].split(' ')[0] if destination_port is defined and\
                                            'range' in destination_port else None }}",
                                        "end": "{{ destination_port.split('range ')[1].split(' ')[1] if destination_port is defined and\
                                            'range' in destination_port else None }}",
                                    },
                                },
                                "icmpopt": {
                                    "name": "{{ icmpopt.split(' ')[0] }}",
                                    "code": "{{ icmpopt.split(' ')[1] }}",
                                },
                            },
                        },
                    },
                },
            },
        },
    ]
    # fmt: on
