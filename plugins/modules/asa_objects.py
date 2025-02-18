#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for asa_objects
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: asa_objects
short_description: Object resource module
description: This module configures and manages Objects on ASA platforms.
version_added: 1.0.0
author: Vladimir Rulev (@rulev)
notes:
- Tested against Cisco ASA Version 9.16
- This module works with connection C(network_cli). See L(ASA Platform Options,../network/user_guide/platform_asa.html).
options:
  config:
    description: A list of Objects options.
    type: list
    elements: dict
    suboptions:
      object_type:
        description: The object type.
        type: str
        required: true
        choices:
        - network
        - service
      objects:
        description: The objects.
        type: list
        elements: dict
        suboptions:
          name:
            description: Specifies object ID
            required: true
            type: str
          description:
            description: The description for the object.
            type: str
          host:
            description: Set this to specify a single host object.
            type: str
          subnet:
            description: Enter an IPv4 network address with space seperated netmask or IPv6 CIDR.
            type: str
          range:
            description: Enter this keyword to specify a range
            type: str
          fqdn:
            description: Enter this keyword to specify a FQDN
            type: str
          fqdn_v4:
            description: Enter this keyword to specify an IPv4 FQDN
            type: str
          fqdn_v6:
            description: Enter this keyword to specify an IPv6 FQDN
            type: str
          nat:
            description: Enable NAT on a singleton object
            type: dict
            suboptions:
              real_if:
                description: Prenat interface
                type: str
              mapped_if:
                description: Postnat interface
                type: str
              dynamic:
                description: Specify NAT type as dynamic
                type: dict
                suboptions:
                  name:
                    description: Mapped IP address, network object/object-group name or IPv6 prefix
                    type: str
                  interface:
                    description: Use interface address as mapped IP
                    type: dict
                    suboptions:
                      ipv6:
                        description: Use IPv6 address(es) as mapped IP(s)
                        type: bool
                  pat_pool:
                    description: Specify object or object-group name for mapped source pat pool
                    type: dict
                    suboptions:
                      name:
                        description: Mapped network object/object-group name
                        type: str
                      interface:
                        description: Use interface address as mapped IP
                        type: dict
                        suboptions:
                          ipv6:
                            description: Use IPv6 address(es) as mapped IP(s)
                            type: bool
                      flat:
                        description: Translate TCP and UDP ports into flat range 1024-65535
                        type: bool
                      include_reserve:
                        description: Translate TCP and UDP ports into flat range 1-65535
                        type: bool
                      round_robin:
                        description: Specify to use PAT ip addresses in round robin instead one by one
                        type: bool
                      block_allocation:
                        description: Enable port block allocation
                        type: bool
                      extended:
                        description: Extend PAT uniqueness to per destination instead of per interface
                        type: bool
                  dns:
                    description: Use the created xlate to rewrite DNS record
                    type: bool
              static:
                description: Specify NAT type as static
                type: dict
                suboptions:
                  name:
                    description: Mapped IP address, network object/object-group name or IPv6 prefix
                    type: str
                  interface:
                    description: Use interface address as mapped IP
                    type: dict
                    suboptions:
                      ipv6:
                        description: Use IPv6 address(es) as mapped IP(s)
                        type: bool
                  service:
                    description: Define port mapping
                    type: dict
                    suboptions:
                      protocol:
                        description: Define transport protocol
                        type: str
                        choices:
                          - tcp
                          - udp
                          - sctp
                      real_port:
                        description: Specify real port
                        type: str
                      mapped_port:
                        description: Specify mapped port
                        type: str
                  net_to_net:
                    description: Use Net to net mapping of IPv4 to IPv6 address(es)
                    type: bool
                  dns:
                    description: Use the created xlate to rewrite DNS record
                    type: bool
                  no_proxy_arp:
                    description: Disable proxy ARP on the egress interface
                    type: bool
                  route_lookup:
                    description: Perform route lookup for this rule
                    type: bool
          service:
            description: Enter this keyword to specify a service
            type: dict
            suboptions:
              protocol:
                description: Protocol name or number
                type: str
                required: true
              source_port:
                description: Service source port
                type: dict
                suboptions:
                  eq:
                    description: Port equal
                    type: str
                  gt:
                    description: Port greater than
                    type: str
                  lt:
                    description: Port less than
                    type: str
                  neq:
                    description: Port not equal
                    type: str
                  range:
                    description: Port in range
                    type: dict
                    suboptions:
                      start:
                        description: Port range start
                        type: str
                      end:
                        description: Port range end
                        type: str
              destination_port:
                description: Service destination port
                type: dict
                suboptions:
                  eq:
                    description: Port equal
                    type: str
                  gt:
                    description: Port greater than
                    type: str
                  lt:
                    description: Port less than
                    type: str
                  neq:
                    description: Port not equal
                    type: str
                  range:
                    description: Port in range
                    type: dict
                    suboptions:
                      start:
                        description: Port range start
                        type: str
                      end:
                        description: Port range end
                        type: str
              icmpopt:
                description: specify icmp option name
                type: dict
                suboptions:
                  name:
                    description: Specify ICMP option name
                    type: str
                  code:
                    description: Specify ICMP code
                    type: str

  running_config:
    description:
    - The module, by default, will connect to the remote device and retrieve the current
      running-config to use as a base for comparing against the contents of source.
      There are times when it is not desirable to have the task get the current running-config
      for every task in a playbook.  The I(running_config) argument allows the implementer
      to pass in the configuration to use as the base config for comparison. This
      value of this option should be the output received from device by executing
      command.
    type: str
  state:
    description:
    - The state the configuration should be left in. There is no meaning of merged state, as
      an object can only have single configuration command, and they overwrite one another.
      So if an object already existed, merging would behave like replacement.
    type: str
    choices:
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: replaced
"""

EXAMPLES = """
# Using Replaced

# Before state:
# -------------

# ciscoasa# sh run object
# object network test_fqdn_obj
#  fqdn google.com
#  description a test fqdn object
# object network test_host_obj
#  host 1.2.3.4
#  description a test host object
# object network test_nat_obj
#  host 1.2.3.4
#  description a test nat object
# object network test_range_obj
#  range 10.0.0.1 10.0.0.10
#  description a test range object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object service test_gre_obj
#  service gre
# object service test_icmp_echo_obj
#  service icmp echo
# object service test_icmp_echo_repl_code_obj
#  service icmp echo-reply 0
# object service test_tcp_eq_obj
#  service tcp destination eq https
# object service test_tcp_range_obj
#  service tcp destination range www https
# object service test_tcp_source_eq_obj
#  service tcp source eq 5671
# object service test_tcp_source_range_obj
#  service tcp source range 5671 5672
# ciscoasa# sh run nat | ex ^nat
# object network test_nat_obj
#  nat (any,any) static 5.6.7.8 net-to-net
# ciscoasa#

- name: Replace module attributes of given objects
  become: true
  cisco.asa.asa_objects:
    config:
      - object_type: network
        objects:
          - description: a test fqdn v4 object
            fqdn_v4: microsoft.com
            name: test_fqdn_obj
          - description: a test range object
            name: test_range_obj
            range: 10.0.0.1 10.0.0.10
          - description: another test host object
            host: 1.2.3.4
            name: test_host_obj_1
          - name: test_nat_obj
      - object_type: service
        objects:
          - name: test_tcp_source_range_obj
            service:
              protocol: tcp
              source_port:
                range:
                  end: '5672'
                  start: '5671'
          - name: test_tcp_eq_obj
            service:
              destination_port:
                eq: https
              protocol: tcp
          - name: test_icmp_echo_obj
            service:
              icmpopt:
                name: echo
                code: 8
              protocol: icmp
    state: replaced

# Commands Fired:
# ---------------
#
# object network test_fqdn_obj
# description a test fqdn v4 object
# fqdn v4 microsoft.com
# object network test_host_obj_1
# description another test host object
# host 1.2.3.4
# object network test_nat_obj
# no description a test nat object
# no nat (any,any) static 5.6.7.8 net-to-net
# object service test_icmp_echo_obj
# service icmp echo 8

# After state:
# ------------
#
# ciscoasa# sh run object
# object network test_fqdn_obj
#  fqdn v4 microsoft.com
#  description a test fqdn v4 object
# object network test_host_obj
#  host 1.2.3.4
#  description a test host object
# object network test_nat_obj
#  host 1.2.3.4
# object network test_range_obj
#  range 10.0.0.1 10.0.0.10
#  description a test range object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object service test_gre_obj
#  service gre
# object service test_icmp_echo_obj
#  service icmp echo 8
# object service test_icmp_echo_repl_code_obj
#  service icmp echo-reply 0
# object service test_tcp_eq_obj
#  service tcp destination eq https
# object service test_tcp_range_obj
#  service tcp destination range www https
# object service test_tcp_source_eq_obj
#  service tcp source eq 5671
# object service test_tcp_source_range_obj
#  service tcp source range 5671 5672
# object network test_host_obj_1
#  host 1.2.3.4
#  description another test host object
# ciscoasa# sh run nat | ex ^nat
# ciscoasa#

# Using Overridden

# Before state:
# -------------

# ciscoasa# sh run object
# object network test_fqdn_obj
#  fqdn google.com
#  description a test fqdn object
# object network test_host_obj
#  host 1.2.3.4
#  description a test host object
# object network test_nat_obj
#  host 1.2.3.4
#  description a test nat object
# object network test_range_obj
#  range 10.0.0.1 10.0.0.10
#  description a test range object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object service test_gre_obj
#  service gre
# object service test_icmp_echo_obj
#  service icmp echo
# object service test_icmp_echo_repl_code_obj
#  service icmp echo-reply 0
# object service test_tcp_eq_obj
#  service tcp destination eq https
# object service test_tcp_range_obj
#  service tcp destination range www https
# object service test_tcp_source_eq_obj
#  service tcp source eq 5671
# object service test_tcp_source_range_obj
#  service tcp source range 5671 5672
# ciscoasa# sh run nat | ex ^nat
# object network test_nat_obj
#  nat (any,any) static 5.6.7.8 net-to-net
# ciscoasa#

- name: Overridden module attributes of given objects
  become: true
  register: result
  cisco.asa.asa_objects:
    config:
      - object_type: network
        objects:
          - description: a modified test fqdn object
            fqdn_v4: microsoft.com
            name: test_fqdn_obj
          - description: a test subnet object
            name: test_subnet_obj
            subnet: 10.0.0.0 255.255.255.0
          - description: a test range object
            name: test_range_another_obj
            range: 10.0.10.1 10.0.10.10
      - object_type: service
        objects:
          - name: test_gre_obj
            service:
              protocol: gre
    state: overridden

# Commands Fired:
# ---------------
#
# no object network test_host_obj
# no object network test_nat_obj
# no object network test_range_obj
# no object service test_icmp_echo_obj
# no object service test_icmp_echo_repl_code_obj
# no object service test_tcp_eq_obj
# no object service test_tcp_range_obj
# no object service test_tcp_source_eq_obj
# no object service test_tcp_source_range_obj
# object network test_fqdn_obj
# description a modified test fqdn object
# fqdn v4 microsoft.com
# object network test_range_another_obj
# description a test range object
# range 10.0.10.1 10.0.10.10

# After state:
# ------------
#
# ciscoasa# sh run object
# object network test_fqdn_obj
#  fqdn v4 microsoft.com
#  description a modified test fqdn object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object service test_gre_obj
#  service gre
# object network test_range_another_obj
#  range 10.0.10.1 10.0.10.10
#  description a test range object
# ciscoasa# sh run nat | ex ^nat
# ciscoasa#

# Using Deleted

# Before state:
# -------------

# ciscoasa# sh run object
# object network test_fqdn_obj
#  fqdn google.com
#  description a test fqdn object
# object network test_host_obj
#  host 1.2.3.4
#  description a test host object
# object network test_nat_obj
#  host 1.2.3.4
#  description a test nat object
# object network test_range_obj
#  range 10.0.0.1 10.0.0.10
#  description a test range object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object service test_gre_obj
#  service gre
# object service test_icmp_echo_obj
#  service icmp echo
# object service test_icmp_echo_repl_code_obj
#  service icmp echo-reply 0
# object service test_tcp_eq_obj
#  service tcp destination eq https
# object service test_tcp_range_obj
#  service tcp destination range www https
# object service test_tcp_source_eq_obj
#  service tcp source eq 5671
# object service test_tcp_source_range_obj
#  service tcp source range 5671 5672
# ciscoasa# sh run nat | ex ^nat
# object network test_nat_obj
#  nat (any,any) static 5.6.7.8 net-to-net
# ciscoasa#

- name: Delete module attributes of given objects
  become: true
  cisco.asa.asa_objects:
    config:
      - object_type: network
        objects:
          - name: test_range_obj
          - name: test_non_existent_obj
      - object_type: service
        objects:
          - name: test_icmp_echo_obj
    state: deleted

# Commands Fired:
# ---------------
#
# no object network test_range_obj
# no object service test_icmp_echo_obj

# After state:
# ------------
#
# ciscoasa# sh run object
# object network test_fqdn_obj
#  fqdn google.com
#  description a test fqdn object
# object network test_host_obj
#  host 1.2.3.4
#  description a test host object
# object network test_nat_obj
#  host 1.2.3.4
#  description a test nat object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object service test_gre_obj
#  service gre
# object service test_icmp_echo_repl_code_obj
#  service icmp echo-reply 0
# object service test_tcp_eq_obj
#  service tcp destination eq https
# object service test_tcp_range_obj
#  service tcp destination range www https
# object service test_tcp_source_eq_obj
#  service tcp source eq 5671
# object service test_tcp_source_range_obj
#  service tcp source range 5671 5672
# ciscoasa# sh run nat | ex ^nat
# object network test_nat_obj
#  nat (any,any) static 5.6.7.8 net-to-net
# ciscoasa#

# Using DELETED without any config passed
# "(NOTE: This will delete all of configured resource module attributes)"

# Before state:
# -------------

# ciscoasa# sh run object
# object network test_fqdn_obj
#  fqdn google.com
#  description a test fqdn object
# object network test_host_obj
#  host 1.2.3.4
#  description a test host object
# object network test_nat_obj
#  host 1.2.3.4
#  description a test nat object
# object network test_range_obj
#  range 10.0.0.1 10.0.0.10
#  description a test range object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object service test_gre_obj
#  service gre
# object service test_icmp_echo_obj
#  service icmp echo
# object service test_icmp_echo_repl_code_obj
#  service icmp echo-reply 0
# object service test_tcp_eq_obj
#  service tcp destination eq https
# object service test_tcp_range_obj
#  service tcp destination range www https
# object service test_tcp_source_eq_obj
#  service tcp source eq 5671
# object service test_tcp_source_range_obj
#  service tcp source range 5671 5672
# ciscoasa# sh run nat | ex ^nat
# object network test_nat_obj
#  nat (any,any) static 5.6.7.8 net-to-net
# ciscoasa#

- name: Delete module attributes of given objects
  become: true
  cisco.asa.asa_objects:
    state: deleted

# Commands Fired:
# ---------------
#
# no object network test_fqdn_obj
# no object network test_host_obj
# no object network test_nat_obj
# no object network test_range_obj
# no object network test_subnet_obj
# no object service test_gre_obj
# no object service test_icmp_echo_obj
# no object service test_icmp_echo_repl_code_obj
# no object service test_tcp_eq_obj
# no object service test_tcp_range_obj
# no object service test_tcp_source_eq_obj
# no object service test_tcp_source_range_obj

# After state:
# ------------
#
# ciscoasa# sh run object
# ciscoasa# sh run nat | ex ^nat
# ciscoasa#

# Using Gathered

# Before state:
# -------------

# ciscoasa# sh run object
# object network test_fqdn_obj
#  fqdn google.com
#  description a test fqdn object
# object network test_host_obj
#  host 1.2.3.4
#  description a test host object
# object network test_nat_obj
#  host 1.2.3.4
#  description a test nat object
# object network test_range_obj
#  range 10.0.0.1 10.0.0.10
#  description a test range object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object service test_gre_obj
#  service gre
# object service test_icmp_echo_obj
#  service icmp echo
# object service test_icmp_echo_repl_code_obj
#  service icmp echo-reply 0
# object service test_tcp_eq_obj
#  service tcp destination eq https
# object service test_tcp_range_obj
#  service tcp destination range www https
# object service test_tcp_source_eq_obj
#  service tcp source eq 5671
# object service test_tcp_source_range_obj
#  service tcp source range 5671 5672
# ciscoasa# sh run nat | ex ^nat
# object network test_nat_obj
#  nat (any,any) static 5.6.7.8 net-to-net
# ciscoasa#

- name: Gather the provided configuration with the exisiting running configuration
  register: result
  cisco.asa.asa_objects:
    config:
    state: gathered

# Module Execution Result:
# ------------
#
# "gathered": [
#     {
#         "object_type": "network",
#         "objects": [
#             {
#                 "description": "a test fqdn object",
#                 "fqdn": "google.com",
#                 "name": "test_fqdn_obj"
#             },
#             {
#                 "description": "a test host object",
#                 "host": "1.2.3.4",
#                 "name": "test_host_obj"
#             },
#             {
#                 "description": "a test nat object",
#                 "host": "1.2.3.4",
#                 "name": "test_nat_obj",
#                 "nat": {
#                     "mapped_if": "any",
#                     "real_if": "any",
#                     "static": {
#                         "name": "5.6.7.8",
#                         "net_to_net": true
#                     }
#                 }
#             },
#             {
#                 "description": "a test range object",
#                 "name": "test_range_obj",
#                 "range": "10.0.0.1 10.0.0.10"
#             },
#             {
#                 "description": "a test subnet object",
#                 "name": "test_subnet_obj",
#                 "subnet": "10.0.0.0 255.255.255.0"
#             }
#         ]
#     },
#     {
#         "object_type": "service",
#         "objects": [
#             {
#                 "name": "test_gre_obj",
#                 "service": {
#                     "protocol": "gre"
#                 }
#             },
#             {
#                 "name": "test_icmp_echo_obj",
#                 "service": {
#                     "icmpopt": {
#                         "name": "echo"
#                     },
#                     "protocol": "icmp"
#                 }
#             },
#             {
#                 "name": "test_icmp_echo_repl_code_obj",
#                 "service": {
#                     "icmpopt": {
#                         "code": "0",
#                         "name": "echo-reply"
#                     },
#                     "protocol": "icmp"
#                 }
#             },
#             {
#                 "name": "test_tcp_eq_obj",
#                 "service": {
#                     "destination_port": {
#                         "eq": "https"
#                     },
#                     "protocol": "tcp"
#                 }
#             },
#             {
#                 "name": "test_tcp_range_obj",
#                 "service": {
#                     "destination_port": {
#                         "range": {
#                             "end": "https",
#                             "start": "www"
#                         }
#                     },
#                     "protocol": "tcp"
#                 }
#             },
#             {
#                 "name": "test_tcp_source_eq_obj",
#                 "service": {
#                     "protocol": "tcp",
#                     "source_port": {
#                         "eq": "5671"
#                     }
#                 }
#             },
#             {
#                 "name": "test_tcp_source_range_obj",
#                 "service": {
#                     "protocol": "tcp",
#                     "source_port": {
#                         "range": {
#                             "end": "5672",
#                             "start": "5671"
#                         }
#                     }
#                 }
#             }
#         ]
#     }
# ]

# Using Rendered

- name: Render the commands for provided  configuration
  become: true
  cisco.asa.asa_objects:
    config: "{{ initial_config }}"
    state: rendered

# Module Execution Result:
# ------------
#
# "rendered": [
#     "object network test_fqdn_obj",
#     "description a test fqdn object",
#     "fqdn google.com",
#     "object network test_host_obj",
#     "description a test host object",
#     "host 1.2.3.4",
#     "object network test_nat_obj",
#     "description a test nat object",
#     "host 1.2.3.4",
#     "nat (any,any) static 5.6.7.8 net-to-net",
#     "object network test_range_obj",
#     "description a test range object",
#     "range 10.0.0.1 10.0.0.10",
#     "object network test_subnet_obj",
#     "description a test subnet object",
#     "subnet 10.0.0.0 255.255.255.0",
#     "object service test_gre_obj",
#     "service gre",
#     "object service test_icmp_echo_obj",
#     "service icmp echo",
#     "object service test_icmp_echo_repl_code_obj",
#     "service icmp echo-reply 0",
#     "object service test_tcp_eq_obj",
#     "service tcp destination eq https",
#     "object service test_tcp_range_obj",
#     "service tcp destination range www https",
#     "object service test_tcp_source_eq_obj",
#     "service tcp source eq 5671",
#     "object service test_tcp_source_range_obj",
#     "service tcp source range 5671 5672"
# ]

# Using Parsed

# _parsed.cfg
# -------------

# object network test_host_obj
#  host 1.2.3.4
#  description a test host object
# object network test_subnet_obj
#  subnet 10.0.0.0 255.255.255.0
#  description a test subnet object
# object network test_range_obj
#  range 10.0.0.1 10.0.0.10
#  description a test range object
# object network test_fqdn_obj
#  fqdn google.com
#  description a test fqdn object
# object network test_nat_obj
#  description a test nat object
#  host 1.2.3.4
#  nat (any,any) static 5.6.7.8 net-to-net
# object service test_tcp_eq_obj
#  service tcp destination eq https
# object service test_tcp_range_obj
#  service tcp destination range www https
# object service test_gre_obj
#  service gre
# object service test_icmp_echo_obj
#  service icmp echo
# object service test_icmp_echo_repl_code_obj
#  service icmp echo-reply 0
# object service test_tcp_source_eq_obj
#  service tcp source eq 5671
# object service test_tcp_source_range_obj
#  service tcp source range 5671 5672

- name: Parse the commands for provided configuration
  become: true
  cisco.asa.asa_objects:
    running_config: "{{ lookup('file', '_parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------
#
# "parsed": [
#     {
#         "object_type": "network",
#         "objects": [
#             {
#                 "description": "a test fqdn object",
#                 "fqdn": "google.com",
#                 "name": "test_fqdn_obj"
#             },
#             {
#                 "description": "a test host object",
#                 "host": "1.2.3.4",
#                 "name": "test_host_obj"
#             },
#             {
#                 "description": "a test nat object",
#                 "host": "1.2.3.4",
#                 "name": "test_nat_obj",
#                 "nat": {
#                     "mapped_if": "any",
#                     "real_if": "any",
#                     "static": {
#                         "name": "5.6.7.8",
#                         "net_to_net": true
#                     }
#                 }
#             },
#             {
#                 "description": "a test range object",
#                 "name": "test_range_obj",
#                 "range": "10.0.0.1 10.0.0.10"
#             },
#             {
#                 "description": "a test subnet object",
#                 "name": "test_subnet_obj",
#                 "subnet": "10.0.0.0 255.255.255.0"
#             }
#         ]
#     },
#     {
#         "object_type": "service",
#         "objects": [
#             {
#                 "name": "test_gre_obj",
#                 "service": {
#                     "protocol": "gre"
#                 }
#             },
#             {
#                 "name": "test_icmp_echo_obj",
#                 "service": {
#                     "icmpopt": {
#                         "name": "echo"
#                     },
#                     "protocol": "icmp"
#                 }
#             },
#             {
#                 "name": "test_icmp_echo_repl_code_obj",
#                 "service": {
#                     "icmpopt": {
#                         "code": "0",
#                         "name": "echo-reply"
#                     },
#                     "protocol": "icmp"
#                 }
#             },
#             {
#                 "name": "test_tcp_eq_obj",
#                 "service": {
#                     "destination_port": {
#                         "eq": "https"
#                     },
#                     "protocol": "tcp"
#                 }
#             },
#             {
#                 "name": "test_tcp_range_obj",
#                 "service": {
#                     "destination_port": {
#                         "range": {
#                             "end": "https",
#                             "start": "www"
#                         }
#                     },
#                     "protocol": "tcp"
#                 }
#             },
#             {
#                 "name": "test_tcp_source_eq_obj",
#                 "service": {
#                     "protocol": "tcp",
#                     "source_port": {
#                         "eq": "5671"
#                     }
#                 }
#             },
#             {
#                 "name": "test_tcp_source_range_obj",
#                 "service": {
#                     "protocol": "tcp",
#                     "source_port": {
#                         "range": {
#                             "end": "5672",
#                             "start": "5671"
#                         }
#                     }
#                 }
#             }
#         ]
#     }
# ]
"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(replaced), C(overridden), C(deleted) or C(purged)
  type: dict
  sample:
    before:
    - object_type: network
      objects:
      - description: a test fqdn object
        fqdn: google.com
        name: test_fqdn_obj
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
  sample:
    after:
    - object_type: network
      objects:
      - description: a test fqdn v4 object
        fqdn_v4: microsoft.com
        name: test_fqdn_obj
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample:
    commands:
      - object network test_fqdn_obj
      - description a test fqdn v4 object
      - fqdn v4 microsoft.com
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    rendered:
      - object network test_fqdn_obj
      - description a test fqdn object
      - fqdn google.com
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample:
    gathered:
      - object_type: network
        objects:
        - description: a test fqdn object
          fqdn: google.com
          name: test_fqdn_obj
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample:
    parsed:
      - object_type: network
        objects:
        - description: a test fqdn object
          fqdn: google.com
          name: test_fqdn_obj
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.cisco.asa.plugins.module_utils.network.asa.argspec.objects.objects import (
    ObjectsArgs,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.config.objects.objects import (
    Objects,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=ObjectsArgs.argument_spec,
        mutually_exclusive=[["config", "running_config"]],
        required_if=[
            ["state", "merged", ["config"]],
            ["state", "replaced", ["config"]],
            ["state", "overridden", ["config"]],
            ["state", "rendered", ["config"]],
            ["state", "parsed", ["running_config"]],
        ],
        supports_check_mode=True,
    )

    result = Objects(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
