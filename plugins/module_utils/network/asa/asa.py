# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
#
# (c) 2016 Red Hat Inc.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type
import json

from ansible.module_utils._text import to_text
from ansible.module_utils.basic import env_fallback
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    EntityCollection,
)
from ansible.module_utils.connection import exec_command
from ansible.module_utils.connection import Connection, ConnectionError

_DEVICE_CONFIGS = {}
_CONNECTION = None

asa_provider_spec = {
    "host": dict(),
    "port": dict(type="int"),
    "username": dict(fallback=(env_fallback, ["ANSIBLE_NET_USERNAME"])),
    "password": dict(
        fallback=(env_fallback, ["ANSIBLE_NET_PASSWORD"]), no_log=True
    ),
    "ssh_keyfile": dict(
        fallback=(env_fallback, ["ANSIBLE_NET_SSH_KEYFILE"]), type="path"
    ),
    "authorize": dict(
        fallback=(env_fallback, ["ANSIBLE_NET_AUTHORIZE"]), type="bool"
    ),
    "auth_pass": dict(
        fallback=(env_fallback, ["ANSIBLE_NET_AUTH_PASS"]), no_log=True
    ),
    "timeout": dict(type="int"),
}

asa_argument_spec = {
    "provider": dict(
        type="dict",
        options=asa_provider_spec,
        removed_at_date="2022-06-01",
        removed_from_collection="cisco.asa",
    )
}

asa_top_spec = {
    "authorize": dict(
        fallback=(env_fallback, ["ANSIBLE_NET_AUTHORIZE"]), type="bool"
    ),
    "context": dict(type="str"),
    "passwords": dict(type="bool"),
}
asa_argument_spec.update(asa_top_spec)

command_spec = {"command": dict(key=True), "prompt": dict(), "answer": dict()}


def get_provider_argspec():
    return asa_provider_spec


def check_args(module):
    pass


def get_connection(module):
    if hasattr(module, "_asa_connection"):
        return module._asa_connection

    # Not all modules include the 'context' key.
    context = module.params.get("context")
    capabilities = get_capabilities(module)
    network_api = capabilities.get("network_api")
    if network_api == "cliconf":
        module._asa_connection = Connection(module._socket_path)
    else:
        module.fail_json(msg="Invalid connection type %s" % network_api)

    if context:
        if context == "system":
            command = "changeto system"
        else:
            command = "changeto context %s" % context
        module._asa_connection.get(command)

    return module._asa_connection


def get_capabilities(module):
    if hasattr(module, "_asa_capabilities"):
        return module._asa_capabilities
    try:
        capabilities = Connection(module._socket_path).get_capabilities()
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
    module._asa_capabilities = json.loads(capabilities)

    return module._asa_capabilities


def to_commands(module, commands):
    if not isinstance(commands, list):
        raise AssertionError("argument must be of type <list>")

    transform = EntityCollection(module, command_spec)
    commands = transform(commands)

    for index, item in enumerate(commands):
        if module.check_mode and not item["command"].startswith("show"):
            module.warn(
                "only show commands are supported when using check "
                "mode, not executing `%s`" % item["command"]
            )

    return commands


def run_commands(module, commands, check_rc=True):
    connection = get_connection(module)
    try:
        return connection.run_commands(commands=commands, check_rc=check_rc)
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc))


def get_config(module, flags=None):
    flags = [] if flags is None else flags

    # Not all modules include the 'passwords' key.
    passwords = module.params.get("passwords", False)
    if passwords:
        cmd = "more system:running-config"
    else:
        cmd = "show running-config "
        cmd += " ".join(flags)
        cmd = cmd.strip()

    try:
        return _DEVICE_CONFIGS[cmd]
    except KeyError:
        conn = get_connection(module)
        out = conn.get(cmd)
        cfg = to_text(out, errors="surrogate_then_replace").strip()
        _DEVICE_CONFIGS[cmd] = cfg
        return cfg


def load_config(module, config):
    try:
        conn = get_connection(module)
        conn.edit_config(config)
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc))


def get_defaults_flag(module):
    rc, out, err = exec_command(module, "show running-config ?")
    out = to_text(out, errors="surrogate_then_replace")

    commands = set()
    for line in out.splitlines():
        if line:
            commands.add(line.strip().split()[0])

    if "all" in commands:
        return "all"
    else:
        return "full"
