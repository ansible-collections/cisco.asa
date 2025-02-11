#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for asa_asa_objects
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: asa_objects
short_description: Object resource module
description: This module configures and manages Objects on ASA platforms.
version_added: 1.0.0
author: Vladimir Rulev
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
          service:
            description: Enter this keyword to specify a service
            type: dict
            suboptions:
              protocol:
                description: protocol name or number
                type: str
                required: true
              source_port:
                description: specify service source port
                type: dict
                suboptions:
                  eq:
                    description: Match only packets on a given port number.
                    type: str
                  gt:
                    description: Match only packets with a greater port number.
                    type: str
                  lt:
                    description: Match only packets with a lower port number.
                    type: str
                  neq:
                    description: Match only packets not on a given port number.
                    type: str
                  range:
                    description: Port range operator
                    type: dict
                    suboptions:
                      start:
                        description: Specify the start of the port range.
                        type: str
                      end:
                        description: Specify the end of the port range.
                        type: str
              destination_port:
                description: specify service source port
                type: dict
                suboptions:
                  eq:
                    description: Match only packets on a given port number.
                    type: str
                  gt:
                    description: Match only packets with a greater port number.
                    type: str
                  lt:
                    description: Match only packets with a lower port number.
                    type: str
                  neq:
                    description: Match only packets not on a given port number.
                    type: str
                  range:
                    description: Port range operator
                    type: dict
                    suboptions:
                      start:
                        description: Specify the start of the port range.
                        type: str
                      end:
                        description: Specify the end of the port range.
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
                    type: int

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
    - The state the configuration should be left in
    type: str
    choices:
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
"""

EXAMPLES = """

"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.argspec.asa_objects.asa_objects import (
    Asa_objectsArgs,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.config.asa_objects.asa_objects import (
    Asa_objects,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Asa_objectsArgs.argument_spec,
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

    result = Asa_objects(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
