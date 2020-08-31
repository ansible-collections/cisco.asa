#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The asa_acls class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import copy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.facts.facts import (
    Facts,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    remove_empties,
    dict_merge,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.utils.utils import (
    new_dict_to_set,
)


class Acls(ConfigBase):
    """
    The asa_acls class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["acls"]

    def __init__(self, module):
        super(Acls, self).__init__(module)

    def get_acls_facts(self, data=None):
        """ Get the 'facts' (the current configuration)
        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources, data=data
        )
        acls_facts = facts["ansible_network_resources"].get("acls")
        if not acls_facts:
            return []

        return acls_facts

    def execute_module(self):
        """ Execute the module
        :rtype: A dictionary
        :returns: The result from moduel execution
        """
        result = {"changed": False}
        commands = list()
        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_acls_facts = self.get_acls_facts()
        else:
            existing_acls_facts = []

        if self.state in self.ACTION_STATES or self.state == "rendered":
            commands.extend(self.set_config(existing_acls_facts))

        if commands and self.state in self.ACTION_STATES:
            if not self._module.check_mode:
                self._connection.edit_config(commands)
            result["changed"] = True

        if self.state in self.ACTION_STATES:
            result["commands"] = commands

        if self.state in self.ACTION_STATES or self.state == "gathered":
            changed_acls_facts = self.get_acls_facts()
        elif self.state == "rendered":
            result["rendered"] = commands
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed"
                )
            result["parsed"] = self.get_acls_facts(data=running_config)
        else:
            changed_acls_facts = []

        if self.state in self.ACTION_STATES:
            result["before"] = existing_acls_facts
            if result["changed"]:
                result["after"] = changed_acls_facts
        elif self.state == "gathered":
            result["gathered"] = changed_acls_facts

        result["warnings"] = warnings

        return result

    def set_config(self, existing_acls_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the deisred configuration
        """
        want = self._module.params["config"]
        have = existing_acls_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the deisred configuration
        """
        commands = []

        state = self._module.params["state"]
        if (
            state in ("overridden", "merged", "replaced", "rendered")
            and not want
        ):
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state
                )
            )

        if state == "overridden":
            commands = self._state_overridden(want, have)
        elif state == "deleted":
            commands = self._state_deleted(want, have)
        elif state == "merged" or state == "rendered":
            commands = self._state_merged(want, have)
        elif state == "replaced":
            commands = self._state_replaced(want, have)

        return commands

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the deisred configuration
        """
        commands = []

        for config_want in want:
            for acls_want in config_want.get("acls"):
                if acls_want.get("rename"):
                    commands.extend(
                        self.common_rename_config(
                            acls_want.get("name"),
                            acls_want.get("rename"),
                            have,
                        )
                    )
                    rename = True
                else:
                    rename = False
                    for ace_want in acls_want.get("aces"):
                        check = False
                        for config_have in have:
                            for acls_have in config_have.get("acls"):
                                for ace_have in acls_have.get("aces"):
                                    if (
                                        acls_want.get("name")
                                        == acls_have.get("name")
                                        and ace_want.get("line")
                                        == ace_have.get("line")
                                        and ace_have.get("source")
                                    ):
                                        ace_want = remove_empties(ace_want)
                                        acls_want = remove_empties(acls_want)
                                        set_cmd = self._set_config(
                                            ace_want, ace_have, acls_want
                                        )
                                        commands = self.add_config_cmd(
                                            set_cmd, commands
                                        )
                                        check = True
                                    elif not ace_want.get(
                                        "line"
                                    ) and ace_have.get("source"):
                                        if acls_want.get(
                                            "name"
                                        ) == acls_have.get("name"):
                                            ace_want = remove_empties(ace_want)
                                            set_cmd, check = self.common_condition_check(
                                                ace_want,
                                                ace_have,
                                                acls_want,
                                                config_want,
                                                check,
                                                acls_have,
                                            )
                                            if (
                                                acls_have.get("acl_type")
                                                == "standard"
                                            ):
                                                check = True
                                            commands = self.add_config_cmd(
                                                set_cmd, commands
                                            )
                                    if set_cmd:
                                        for temp_acls_have in config_have.get(
                                            "acls"
                                        ):
                                            for (
                                                temp_ace_have
                                            ) in temp_acls_have.get("aces"):
                                                if acls_want.get(
                                                    "name"
                                                ) == temp_acls_have.get(
                                                    "name"
                                                ) and temp_ace_have.get(
                                                    "source"
                                                ):
                                                    clear_cmd = self._clear_config(
                                                        temp_ace_have,
                                                        temp_acls_have,
                                                    )
                                                    commands = self.add_config_cmd(
                                                        clear_cmd, commands
                                                    )
                                        commands = self.add_config_cmd(
                                            set_cmd, commands
                                        )
                                        set_cmd = []
                                        check = True
                                if check:
                                    break
                            if check:
                                break
                        if not check:
                            # For configuring any non-existing want config
                            ace_want = remove_empties(ace_want)
                            set_cmd = self._set_config(ace_want, {}, acls_want)
                            commands = self.add_config_cmd(set_cmd, commands)
        if not rename:
            # Arranging the cmds suct that all delete cmds are fired before all set cmds
            # and reversing the negate/no access-list as otherwise if deleted from top the
            # next ace takes the line position of deleted ace from top and results in unexpected output
            commands = [each for each in commands if "no" in each][::-1] + [
                each for each in commands if "no" not in each
            ]

        return commands

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        # Creating a copy of want, so that want dict is intact even after delete operation
        # performed during override want n have comparison
        temp_want = copy.deepcopy(want)

        rename = False
        for config_want in temp_want:
            for acls_want in config_want.get("acls"):
                if acls_want.get("rename"):
                    commands.extend(
                        self.common_rename_config(
                            acls_want.get("name"),
                            acls_want.get("rename"),
                            have,
                        )
                    )
                    rename = True
        if not rename:
            for config_have in have:
                for acls_have in config_have.get("acls"):
                    for ace_have in acls_have.get("aces"):
                        check = False
                        for config_want in temp_want:
                            for acls_want in config_want.get("acls"):
                                for ace_want in acls_want.get("aces"):
                                    if acls_want.get("name") == acls_have.get(
                                        "name"
                                    ) and ace_have.get("source"):
                                        ace_want = remove_empties(ace_want)
                                        acls_want = remove_empties(acls_want)
                                        set_cmd = self._set_config(
                                            ace_want, ace_have, acls_want
                                        )
                                        if set_cmd:
                                            for (
                                                temp_acls_have
                                            ) in config_have.get("acls"):
                                                for (
                                                    temp_ace_have
                                                ) in temp_acls_have.get(
                                                    "aces"
                                                ):
                                                    if acls_want.get(
                                                        "name"
                                                    ) == temp_acls_have.get(
                                                        "name"
                                                    ):
                                                        clear_cmd = self._clear_config(
                                                            temp_ace_have,
                                                            temp_acls_have,
                                                        )
                                                        commands = self.add_config_cmd(
                                                            clear_cmd, commands
                                                        )
                                            commands = self.add_config_cmd(
                                                set_cmd, commands
                                            )
                                        check = True
                                        del config_want.get("acls")[0].get(
                                            "aces"
                                        )[0]
                            if check:
                                break
                        if not check:
                            # Delete the config not present in want config
                            if ace_have.get("source"):
                                clear_cmd = self._clear_config(
                                    ace_have, acls_have
                                )
                                commands = self.add_config_cmd(
                                    clear_cmd, commands
                                )
                # For configuring any non-existing want config
                for config_want in temp_want:
                    for acls_want in config_want.get("acls"):
                        for ace_want in acls_want.get("aces"):
                            ace_want = remove_empties(ace_want)
                            set_cmd = self._set_config(ace_want, {}, acls_want)
                            commands = self.add_config_cmd(set_cmd, commands)

            # Arranging the cmds such that all delete cmds are fired before all set cmds
            # and reversing the negate/no access-list as otherwise if deleted from top the
            # next ace takes the line position of deleted ace from top and results in unexpected output
            commands = [each for each in commands if "no" in each][::-1] + [
                each for each in commands if "no" not in each
            ]

        return commands

    def _state_merged(self, want, have):
        """ The command generator when state is merged
        :param want: the additive configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []

        for config_want in want:
            for acls_want in config_want.get("acls"):
                if acls_want.get("rename"):
                    commands.extend(
                        self.common_rename_config(
                            acls_want.get("name"),
                            acls_want.get("rename"),
                            have,
                        )
                    )
                else:
                    for ace_want in acls_want.get("aces"):
                        check = False
                        for config_have in have:
                            for acls_have in config_have.get("acls"):
                                for ace_have in acls_have.get("aces"):
                                    if (
                                        acls_want.get("name")
                                        == acls_have.get("name")
                                        and ace_want.get("line")
                                        == ace_have.get("line")
                                        and ace_have.get("source")
                                    ):
                                        ace_want = remove_empties(ace_want)
                                        ace_want = dict_merge(
                                            ace_have, ace_want
                                        )
                                        set_cmd = self._set_config(
                                            ace_want, ace_have, acls_want
                                        )
                                        if set_cmd:
                                            commands.extend(
                                                self._clear_config(
                                                    ace_have, acls_have
                                                )
                                            )
                                        commands = self.add_config_cmd(
                                            set_cmd, commands
                                        )
                                        check = True
                                    elif not ace_want.get("line"):
                                        if acls_want.get(
                                            "name"
                                        ) == acls_have.get("name"):
                                            ace_want = remove_empties(ace_want)
                                            ace_want = dict_merge(
                                                ace_have, ace_want
                                            )
                                            cmd, check = self.common_condition_check(
                                                ace_want,
                                                ace_have,
                                                acls_want,
                                                config_want,
                                                check,
                                                acls_have,
                                            )
                                            if (
                                                acls_have.get("acl_type")
                                                == "standard"
                                            ):
                                                check = True
                                            commands = self.add_config_cmd(
                                                cmd, commands
                                            )
                                if check:
                                    break
                            if check:
                                break
                        if not check:
                            # For configuring any non-existing want config
                            ace_want = remove_empties(ace_want)
                            set_cmd = self._set_config(ace_want, {}, acls_want)
                            commands = self.add_config_cmd(set_cmd, commands)

        return commands

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted
        :param want: the objects from which the configuration should be removed
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []

        if want:
            for config_want in want:
                for acls_want in config_want.get("acls"):
                    for config_have in have:
                        for acls_have in config_have.get("acls"):
                            for ace_have in acls_have.get("aces"):
                                if acls_want.get("name") == acls_have.get(
                                    "name"
                                ) and ace_have.get("source"):
                                    commands.extend(
                                        self._clear_config(ace_have, acls_have)
                                    )
        else:
            for config_have in have:
                for acls_have in config_have.get("acls"):
                    for ace_have in acls_have.get("aces"):
                        if ace_have.get("source"):
                            clear_cmd = self._clear_config(ace_have, acls_have)
                            commands = self.add_config_cmd(clear_cmd, commands)
        # Reversing the negate/no access-list as otherwise if deleted from top the
        # next ace takes the line position of deleted ace from top and only one ace
        # will be deleted instead of expected aces and results in unexpected output
        commands = commands[::-1]

        return commands

    def add_config_cmd(self, cmd, commands):
        # To set the passed config
        if cmd and cmd[0] not in commands:
            commands.extend(cmd)
        return commands

    def common_rename_config(self, want_name, new_want_name, have):
        """ Fn used to generate the rename cmd if user need to rename the
            existing ACLs name with new
        :param want_name: acl want name
        :param new_want_name: acl want new name that need to be replaced with existing
        :param have: have config
        :rtype: A list
        :returns: cmd generated for renaming
        """
        cmd = []
        for config_have in have:
            for acls_have in config_have.get("acls"):
                have_name = acls_have.get("name")
                if want_name == have_name:
                    cmd.append(
                        "access-list {0} rename {1}".format(
                            want_name, new_want_name
                        )
                    )
                elif new_want_name == have_name:
                    return cmd

        return cmd

    def common_condition_check(
        self, ace_want, ace_have, acls_want, config_want, check, state=""
    ):
        """ The command formatter from the generated command
        :param ace_want: ace want config
        :param ace_have: ace have config
        :param acls_want: acl want config
        :param config_want: want config list
        :param check: for same acl in want and have config, check=True
        :param state: operation state
        :rtype: A list
        :returns: commands generated from want n have config diff
        """
        commands = []
        if (
            ace_want.get("destination")
            and ace_have.get("destination")
            or ace_want.get("source").get("address")
            and ace_have.get("source")
        ):
            if (
                ace_want.get("destination").get("address")
                and ace_want.get("destination").get("address")
                == ace_have.get("destination").get("address")
            ) and (
                ace_want.get("source").get("address")
                and ace_want.get("source").get("address")
                == ace_have.get("source").get("address")
            ):
                cmd = self._set_config(ace_want, ace_have, acls_want)
                commands.extend(cmd)
                check = True
            elif (
                ace_want.get("destination").get("any")
                == ace_have.get("destination").get("any")
                and (
                    ace_want.get("source").get("address")
                    and ace_want.get("source").get("address")
                    == ace_have.get("source").get("address")
                    or ace_want.get("source").get("host")
                    == ace_have.get("source").get("host")
                )
                and ace_want.get("destination").get("any")
            ):
                cmd = self._set_config(ace_want, ace_have, acls_want)
                commands.extend(cmd)
                check = True
            elif (
                (
                    ace_want.get("destination").get("address")
                    and ace_want.get("destination").get("address")
                    == ace_have.get("destination").get("address")
                    or ace_want.get("destination").get("host")
                    == ace_have.get("destination").get("host")
                )
                and ace_want.get("source").get("any")
                == ace_have.get("source").get("any")
                and ace_want.get("source").get("any")
            ):
                cmd = self._set_config(ace_want, ace_have, acls_want)
                commands.extend(cmd)
                check = True
            elif (
                ace_want.get("destination").get("any")
                and ace_want.get("destination").get("any")
                == ace_have.get("destination").get("any")
            ) and (
                ace_want.get("source").get("any")
                and ace_want.get("source").get("any")
                == ace_have.get("source").get("any")
            ):
                cmd = self._set_config(ace_want, ace_have, acls_want)
                commands.extend(cmd)
                check = True

        return commands, check

    def source_dest_config(self, config, cmd, protocol_option):
        """ Function to populate source/destination address and port protocol options
        :param config: want and have diff config
        :param cmd: source/destination command
        :param protocol_option: source/destination protocol option
        :rtype: A list
        :returns: the commands generated based on input source/destination params
        """
        address = config.get("address")
        netmask = config.get("netmask")
        any = config.get("any")
        host = config.get("host")
        interface = config.get("interface")
        object_group_network = config.get("object_group_network")
        if address and netmask:
            cmd = cmd + " {0} {1}".format(address, netmask)
        elif address:
            cmd = cmd + " {0}".format(address.lower())
        elif any:
            cmd = cmd + " {0}".format("any")
        elif host:
            cmd = cmd + " host {0}".format(host)
        elif interface:
            cmd = cmd + " interface {0}".format(interface)
        elif object_group_network:
            cmd = cmd + " object-group {0}".format(object_group_network)
        port_protocol = config.get("port_protocol")
        if port_protocol and ("tcp" in cmd or "udp" in cmd):
            cmd = cmd + " {0} {1}".format(
                list(port_protocol)[0], list(port_protocol.values())[0]
            )
        elif port_protocol and ("tcp" not in cmd or "udp" not in cmd):
            self._module.fail_json(
                msg="Port Protocol option is valid only with TCP/UDP Protocol option!"
            )

        return cmd

    def common_config_cmd(self, want, acl_want, cmd):
        """ Common Function that prepares the acls config cmd based on the want config
        :param want: want ace config
        :param acl_want: want acl config
        :param cmd: cmd passed
        :rtype: string
        :returns: the commands generated based on input ace want/acl want params
        """
        line = want.get("line")
        if line:
            cmd = cmd + " line {0}".format(line)
        remark = want.get("remark")
        if remark:
            cmd = cmd + " remark {0}".format(remark)
        acl_type = acl_want.get("acl_type")
        if acl_type:
            cmd = cmd + " {0}".format(acl_type)
        # Get all of aces option values from diff dict
        grant = want.get("grant")
        source = want.get("source")
        destination = want.get("destination")
        protocol = want.get("protocol")
        po = want.get("protocol_options")
        log = want.get("log")
        time_range = want.get("time_range")
        inactive = want.get("inactive")

        if grant:
            cmd = cmd + " {0}".format(grant)
        if protocol:
            cmd = cmd + " {0}".format(protocol)
        po_val = None
        if po and isinstance(po, dict):
            if not protocol:
                po_key = list(po)[0]
                cmd = cmd + " {0}".format(po_key)
            if po.get("icmp"):
                po_val = po.get("icmp")
            elif po.get("icmp6"):
                po_val = po.get("igmp")
        if source:
            cmd = self.source_dest_config(source, cmd, po)
        if destination:
            cmd = self.source_dest_config(destination, cmd, po)
        if po_val and list(po_val)[0] != "set":
            cmd = cmd + " {0}".format(list(po_val)[0].replace("_", "-"))
        if log:
            cmd = cmd + " log {0}".format(log)
        if time_range:
            cmd = cmd + " time-range {0}".format(time_range)
        if inactive:
            cmd = cmd + " inactive"

        return cmd

    def _set_config(self, want, have, acl_want):
        """ Function that sets the acls config based on the want and have config
        :param want: want config
        :param have: have config
        :param acl_want: want acl config
        :param afi: acl afi type
        :rtype: A list
        :returns: the commands generated based on input want/have params
        """
        commands = []

        # To change the want IPV6 address to lower case, as Cisco ASA configures the IPV6
        # access-list always in Lowercase even if the input is given in Uppercase
        if (
            want.get("destination")
            and want.get("destination").get("address")
            and ":" in want.get("destination").get("address")
        ):
            want["destination"]["address"] = (
                want.get("destination").get("address").lower()
            )
        # Convert the want and have dict to its respective set for taking the set diff
        want_set = set()
        have_set = set()
        new_dict_to_set(want, [], want_set)
        new_dict_to_set(have, [], have_set)
        diff = want_set - have_set

        # Populate the config only when there's a diff b/w want and have config
        if diff:
            name = acl_want.get("name")
            cmd = "access-list {0}".format(name)
            cmd = self.common_config_cmd(want, acl_want, cmd)

            commands.append(cmd)

        return commands

    def _clear_config(self, ace, acl):
        """ Function that deletes the acl config based on the want and have config
        :param acl: acl config
        :param config: config
        :rtype: A list
        :returns: the commands generated based on input acl/config params
        """
        commands = []
        name = acl.get("name")
        cmd = "no access-list {0}".format(name)
        cmd = self.common_config_cmd(ace, acl, cmd)

        commands.append(cmd)

        return commands
