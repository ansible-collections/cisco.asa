#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for asa_banner
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: asa_banner
short_description: Module to configure multiline banners.
description:
  - This will configure the asdm, exec, login and motd banners on remote devices
    running Cisco ASA. It allows playbooks to add or remove banner text from the
    active running configuration.
version_added: 7.0.0
author: Jørgen Spange (@jorgenspange)
extends_documentation_fragment:
  - cisco.asa.asa
notes:
  - Tested against Cisco ASA Version 9.20.
  - This module works with connection C(network_cli).
options:
  banner:
    description:
      - Specifies which banner should be configured on the remote device.
    required: true
    choices:
      - asdm
      - exec
      - login
      - motd
    type: str
  text:
    description:
      - The banner text that should be present in the remote device running
        configuration. Each line of the text becomes a separate C(banner) command,
        which is how the ASA stores a multiline banner. Requires I(state=present).
    type: str
  state:
    description:
      - Specifies whether or not the configuration is present in the current devices
        active running configuration.
    default: present
    type: str
    choices:
      - present
      - absent
"""

EXAMPLES = """
# Using state: present

# Before state:
# -------------
# asa#show running-config banner
# asa#

- name: Configure the motd banner
  cisco.asa.asa_banner:
    banner: motd
    text: |
      this is my motd banner
      that has a multiline
      string
    state: present

# Task Output:
# ------------
# commands:
# - banner motd this is my motd banner
# - banner motd that has a multiline
# - banner motd string

# After state:
# ------------
# asa#show running-config banner
# banner motd this is my motd banner
# banner motd that has a multiline
# banner motd string

# Using state: absent

# Before state:
# -------------
# asa#show running-config banner
# banner motd this is my motd banner

- name: Remove the motd banner
  cisco.asa.asa_banner:
    banner: motd
    state: absent

# Task Output:
# ------------
# commands:
# - no banner motd

# After state:
# ------------
# asa#show running-config banner
# asa#
"""

RETURN = """
commands:
  description: The list of configuration mode commands to send to the device.
  returned: always
  type: list
  sample:
    - banner motd this is my motd banner
    - banner motd that has a multiline
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    emit_warnings,
)

from ansible_collections.cisco.asa.plugins.module_utils.network.asa.asa import (
    asa_argument_spec,
    check_args,
    get_config,
    load_config,
)


def map_obj_to_commands(updates, module):
    commands = list()
    want, have = updates
    state = module.params["state"]
    banner = module.params["banner"]

    if state == "absent":
        if have.get("text"):
            commands.append("no banner %s" % banner)
        return commands

    if want["text"] and want["text"] != have.get("text"):
        # The ASA appends each banner command to the end of the existing banner,
        # so the banner is cleared before the wanted lines are added.
        if have.get("text"):
            commands.append("no banner %s" % banner)
        for line in want["text"].splitlines():
            commands.append(("banner %s %s" % (banner, line)).rstrip())
    return commands


def map_config_to_obj(module):
    banner = module.params["banner"]
    out = get_config(module, flags=["banner %s" % banner])
    prefix = "banner %s" % banner
    lines = list()
    for line in out.splitlines():
        line = line.strip()
        if line == prefix:
            lines.append("")
        elif line.startswith(prefix + " "):
            lines.append(line.split(" ", 2)[2])
    obj = {"banner": banner, "state": "absent"}
    if lines:
        obj["text"] = "\n".join(lines)
        obj["state"] = "present"
    return obj


def map_params_to_obj(module):
    text = module.params["text"]
    if text:
        text = text.rstrip("\n")
    return {
        "banner": module.params["banner"],
        "text": text,
        "state": module.params["state"],
    }


def main():
    """main entry point for module execution"""
    argument_spec = dict(
        banner=dict(required=True, choices=["asdm", "exec", "login", "motd"]),
        text=dict(),
        state=dict(default="present", choices=["present", "absent"]),
    )
    argument_spec.update(asa_argument_spec)
    required_if = [("state", "present", ("text",))]
    module = AnsibleModule(
        argument_spec=argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )
    check_args(module)
    warnings = list()
    result = {"changed": False}
    if warnings:
        result["warnings"] = warnings
    want = map_params_to_obj(module)
    have = map_config_to_obj(module)
    commands = map_obj_to_commands((want, have), module)
    result["commands"] = commands
    if commands:
        if not module.check_mode:
            load_config(module, commands)
        result["changed"] = True
    emit_warnings(module, result)
    module.exit_json(**result)


if __name__ == "__main__":
    main()
