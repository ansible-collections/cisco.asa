from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)


def _tmplt_object_group(config_data):
    command = "object-group {object_type} {name}".format(**config_data)
    return command


def _tmplt_icmp_object(config_data):
    commands = []
    if config_data.get("icmp_type").get("icmp_object"):
        for each in config_data.get("icmp_type").get("icmp_object"):
            commands.append("icmp-object {0}".format(each))
        return commands


def _tmplt_network_object(config_data):
    commands = []
    if config_data.get("network_object").get("host"):
        for each in config_data.get("network_object").get("host"):
            commands.append("network-object host {0}".format(each))
        return commands


def _tmplt_network_object_address(config_data):
    commands = []
    if config_data.get("network_object").get("address"):
        for each in config_data.get("network_object").get("address"):
            commands.append("network-object {0}".format(each))
        return commands


def _tmplt_network_object_ipv6(config_data):
    commands = []
    if config_data.get("network_object").get("ipv6_address"):
        for each in config_data.get("network_object").get("ipv6_address"):
            commands.append("network-object {0}".format(each))
        return commands


def _tmplt_protocol_object(config_data):
    commands = []
    if config_data.get("protocol_object").get("protocol"):
        for each in config_data.get("protocol_object").get("protocol"):
            commands.append("protocol {0}".format(each))
        return commands


def _tmplt_sec_group_name(config_data):
    commands = []
    if config_data.get("security_group").get("sec_name"):
        for each in config_data.get("security_group").get("sec_name"):
            commands.append("security-group name {0}".format(each))
        return commands


def _tmplt_sec_group_tag(config_data):
    commands = []
    if config_data.get("security_group").get("tag"):
        for each in config_data.get("security_group").get("tag"):
            commands.append("security-group tag {0}".format(each))
        return commands


def _tmplt_service_object(config_data):
    if config_data.get("service_object").get("protocol"):
        commands = []
        for each in config_data.get("service_object").get("protocol"):
            commands.append("service-object {0}".format(each))
        return commands


def _tmplt_user_object_user(config_data):
    commands = []
    if config_data.get("user_object").get("user"):
        for each in config_data.get("user_object").get("user"):
            commands.append("user {domain}\\{name}".format(**each))
    return commands


def _tmplt_user_object_user_gp(config_data):
    commands = []
    if config_data.get("user_object").get("user_group"):
        for each in config_data.get("user_object").get("user_group"):
            commands.append("user-group {domain}\\{name} {0}".format(**each))
    return commands


def _tmplt_group_object(config_data):
    command = "group-object { group_object }".format(**config_data)
    return command


class OGsTemplate(NetworkTemplate):
    def __init__(self, lines=None):
        super(OGsTemplate, self).__init__(lines=lines, tmplt=self)

    PARSERS = [
        {
            "name": "og_name",
            "getval": re.compile(
                r"""
                    ^object-group*
                    \s*(?P<obj_type>\S+)*
                    \s*(?P<obj_name>\S+)
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_object_group,
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {
                            "object_type": "{{ obj_type }}",
                            "name": "{{ obj_name }}",
                        }
                    }
                }
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
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"description": "{{ description }}"}
                    }
                }
            },
        },
        {
            "name": "icmp_type",
            "getval": re.compile(
                r"""\s+icmp-object*
                    \s*(?P<object>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_icmp_object,
            "compval": "icmp_type",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"icmp_object": ["{{ object }}"]}
                    }
                }
            },
        },
        {
            "name": "network_object.address",
            "getval": re.compile(
                r"""\s+network-object*
                    \s*(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_network_object_address,
            "compval": "network_object.address",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"address": ["{{ address }}"]}
                    }
                }
            },
        },
        {
            "name": "network_object.host",
            "getval": re.compile(
                r"""\s+network-object*
                    \s*(?P<host_obj>host)*
                    \s*(?P<host_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_network_object,
            "compval": "network_object.host",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"host": ["{{ host_address }}"]}
                    }
                }
            },
        },
        {
            "name": "network_object.ipv6_address",
            "getval": re.compile(
                r"""\s+network-object*
                    \s*(?P<ipv6>\S+::/\d+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_network_object_ipv6,
            "compval": "network_object.ipv6_address",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"ipv6_address": ["{{ ipv6 }}"]}
                    }
                }
            },
        },
        {
            "name": "network_object.object",
            "getval": re.compile(
                r"""\s+network-object\s
                    object*
                    \s*(?P<object>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": "network-object object {{ object }}",
            "compval": "network_object.object",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"object": "{{ object }}"}
                    }
                }
            },
        },
        {
            "name": "protocol_object",
            "getval": re.compile(
                r"""\s+protocol-object*
                    \s*(?P<protocol>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_protocol_object,
            "compval": "protocol_object",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"protocol": ["{{ protocol }}"]}
                    }
                }
            },
        },
        {
            "name": "security_group.sec_name",
            "getval": re.compile(
                r"""\s+security-group\s
                    name*
                    \s*(?P<name>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_sec_group_name,
            "compval": "security_group.sec_name",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"sec_name": ["{{ name }}"]}
                    }
                }
            },
        },
        {
            "name": "security_group.tag",
            "getval": re.compile(
                r"""\s+security-group\s
                    tag*
                    \s*(?P<tag>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_sec_group_tag,
            "compval": "security_group.tag",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"tag": ["{{ tag }}"]}
                    }
                }
            },
        },
        {
            "name": "service_object",
            "getval": re.compile(
                r"""\s+service-object*
                    \s*(?P<protocol>\S+)*\s
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_service_object,
            "compval": "service_object",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"protocol": ["{{ protocol }}"]}
                    }
                }
            },
        },
        {
            "name": "service_object.object",
            "getval": re.compile(
                r"""\s+service-object\s
                    object*
                    \s*(?P<object>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": "service-object object {{ object }}",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"object": "{{ object }}"}
                    }
                }
            },
        },
        {
            "name": "user_object.user",
            "getval": re.compile(
                r"""\s+user*
                    \s*(?P<domain>\S+)\\
                    (?P<user_name>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_user_object_user,
            "compval": "user_object",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {
                            "user": [
                                {
                                    "name": "{{ user_name }}",
                                    "domain": "{{ domain }}",
                                }
                            ]
                        }
                    }
                }
            },
        },
        {
            "name": "user_object.user_gp",
            "getval": re.compile(
                r"""\s+user-group*
                    \s*(?P<domain>\S+)\\
                    (?P<user_gp>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_user_object_user_gp,
            "compval": "user_object",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {
                            "user_group": [
                                {
                                    "name": "{{ user_gp }}",
                                    "domain": "{{ domain }}",
                                }
                            ]
                        }
                    }
                }
            },
        },
        {
            "name": "group_object",
            "getval": re.compile(
                r"""\s+group-object*
                    \s*(?P<gp_obj>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_group_object,
            "compval": "group_object",
            "result": {
                "ogs": {
                    "{{ obj_type }}": {
                        "{{ obj_name }}": {"group_object": "{{ gp_obj }}"}
                    }
                }
            },
        },
    ]
