#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The asa_og class
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
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.utils.utils import (
    new_dict_to_set,
)


class OGs(ConfigBase):
    """
    The asa_og class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ogs',
    ]

    def __init__(self, module):
        super(OG, self).__init__(module)

    def get_og_facts(self, data=None):
        """ Get the 'facts' (the current configuration)
        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources, data=data)
        og_facts = facts['ansible_network_resources'].get('ogs')
        if not og_facts:
            return []

        return og_facts

    def execute_module(self):
        """ Execute the module
        :rtype: A dictionary
        :returns: The result from moduel execution
        """
        result = {'changed': False}
        commands = list()
        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_og_facts = self.get_og_facts()
        else:
            existing_og_facts = []

        if self.state in self.ACTION_STATES or self.state == 'rendered':
            commands.extend(self.set_config(existing_og_facts))

        if commands and self.state in self.ACTION_STATES:
            if not self._module.check_mode:
                self._connection.edit_config(commands)
            result['changed'] = True

        if self.state in self.ACTION_STATES:
            result['commands'] = commands

        if self.state in self.ACTION_STATES or self.state == 'gathered':
            changed_og_facts = self.get_og_facts()
        elif self.state == 'rendered':
            result['rendered'] = commands
        elif self.state == 'parsed':
            running_config = self._module.params['running_config']
            if not running_config:
                self._module.fail_json(msg="value of running_config parameter must not be empty for state parsed")
            result['parsed'] = self.get_og_facts(data=running_config)
        else:
            changed_og_facts = []

        if self.state in self.ACTION_STATES:
            result['before'] = existing_og_facts
            if result['changed']:
                result['after'] = changed_og_facts
        elif self.state == 'gathered':
            result['gathered'] = changed_og_facts

        result['warnings'] = warnings

        return result

    def set_config(self, existing_og_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the deisred configuration
        """
        want = self._module.params['config']
        have = existing_og_facts
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

        if state == 'overridden':
            commands = self._state_overridden(want, have)
        elif state == 'deleted':
            commands = self._state_deleted(want, have)
        elif state == 'merged' or state == "rendered":
            commands = self._state_merged(want, have)
        elif state == 'replaced':
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

        for interface in want:
            for each in have:
                if each['name'] == interface['name']:
                    break
            else:
                continue
            commands.extend(self._clear_config(interface, each, 'replaced'))
            commands.extend(self._set_config(interface, each))
        # Remove the duplicate interface call
        commands = remove_duplicate_interface(commands)

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
        for each in have:
            for interface in want:
                if each['name'] == interface['name']:
                    break
            else:
                # We didn't find a matching desired state, which means we can
                # pretend we recieved an empty desired state.
                interface = dict(name=each['name'])
                commands.extend(self._clear_config(interface, each))
                continue
            commands.extend(self._clear_config(interface, each, 'overridden'))
            commands.extend(self._set_config(interface, each))
        # Remove the duplicate interface call
        commands = remove_duplicate_interface(commands)

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

        for each_want in want:
            for each_have in have:
                if each_want.get('name') == each_have.get('name'):
                    break
            else:
                commands.extend(self._set_config(remove_empties(each_want), dict()))
                continue
            commands.extend(self._set_config(remove_empties(each_want), each_have))
        q(commands)
        commands=[]
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
            for each_want in want:
                for each_have in have:
                    if each_want['name'] == each_have['name']:
                        break
                else:
                    continue
                commands.extend(self._clear_config(remove_empties(each_want), each_have))
        else:
            for each in have:
                commands.extend(self._clear_config(dict(), each))

        return commands

    def add_command_to_config_list(self, cmd, commands):
        if cmd not in commands:
            commands.append(cmd)

    def _set_config(self, want, have):
        """ Function that sets the ogs config based on the want and have config
        :param want: want config
        :param have: have config
        :param og_want: want ogs config
        :rtype: A list
        :returns: the commands generated based on input want/have params
        """
        commands = []

        # Populate the config only when there's a diff b/w want and have config
        # Convert the want and have dict to its respective set for taking the set diff
        want_set = set()
        have_set = set()
        new_dict_to_set(want, [], want_set)
        if have:
            new_dict_to_set(have, [], have_set)
        diff = want_set - have_set
        q(want, have, want_set, have_set, diff)
        # check for protocol options by creating an individual sets for both want and have
        if len(diff) == 1 and dict(diff).get('protocol'):
            diff = set(dict(want_set).get('protocol')) - set(dict(have_set).get('protocol'))

        if diff:
            og_name = want.get('name')
            og_object = want.get('object')
            cmd = 'object-group {0} {1}'.format(og_object, og_name)
            self.add_command_to_config_list(cmd, commands)
            try:
                each = dict(diff)
            except ValueError:
                pass
                # each = {}
                # for every in diff:
                #     each.update(dict(every))
            # if each.get('description'):
            #     description = 'description {0}'.format(each['description'])
            #     self.add_command_to_config_list(description, commands)
            # if og_object == 'network':
            #     if each.get('host'):
            #         if each.get('ip_address'):
            #             cmd = 'network-object host {0}'.format(each['ip_address'])
            #             self.add_command_to_config_list(cmd, commands)
            #         else:
            #             self._module.fail_json(msg='IP address is needed for Network-Object host to be configured '
            #                                        'as expected!')
            #     elif each.get('ip_mask'):
            #         if each.get('ip_address'):
            #             cmd = 'network-object {0} {1}'.format(each['ip_address'], each['ip_mask'])
            #             self.add_command_to_config_list(cmd, commands)
            #         else:
            #             self._module.fail_json(msg='IP address is required for Network-Object to be configured '
            #                                        'as expected!')
            #     elif each.get('ip_address') and dict(want_set).get('host'):
            #         cmd = 'network-object host {0}'.format(each['ip_address'])
            #         self.add_command_to_config_list(cmd, commands)
            # elif og_object == 'icmp_type':
            #     icmp_object = each.get('icmp_object')
            #     if icmp_object:
            #         for every in icmp_object:
            #             cmd = 'icmp-object {0}'.format(every)
            #             self.add_command_to_config_list(cmd, commands)
            # elif og_object == 'protocol':
            #     protocol_object = each.get('protocol')
            #     if protocol_object:
            #         for every in protocol_object:
            #             cmd = 'protocol-object {0}'.format(every)
            #             self.add_command_to_config_list(cmd, commands)
            # elif og_object == 'security':
            #     name = each.get('name')
            #     tag = each.get('tag')
            #     if name:
            #         cmd = 'security-group name {0}'.format(name)
            #         self.add_command_to_config_list(cmd, commands)
            #     if tag:
            #         cmd = 'security-group tag {0}'.format(tag)
            #         self.add_command_to_config_list(cmd, commands)
            # elif og_object == 'service':
            #     service_object = each.get('protocol')
            #     if service_object:
            #         for every in service_object:
            #             cmd = 'service-object {0}'.format(every)
            #             self.add_command_to_config_list(cmd, commands)
            # elif og_object == 'user' and not each.get('object'):
            #     name = each.get('name')
            #     q(name, each.get('user_group'))
            #     if name:
            #         cmd = 'user-group name {0}'.format(name)
            #         self.add_command_to_config_list(cmd, commands)
            # if 'group_object' in each:
            #     description = 'group-object {0}'.format(each['group_object'])
            #     self.add_command_to_config_list(description, commands)

        return commands

    def remove_command_from_config_list(self, cmd, commands):
        # To delete the passed config
        if cmd not in commands:
            commands.append('no %s' % cmd)

    def _clear_config(self, want, have):
        """ Function that deletes the acl config based on the want and have config
        :param acl: acl config
        :param config: config
        :rtype: A list
        :returns: the commands generated based on input acl/config params
        """
        commands = []

        if want:
            object = want.get('object')
            if object == 'icmp_type':
                object = 'icmp-type'
            name = want.get('name')
        else:
            object = have.get('object')
            if object == 'icmp_type':
                object = 'icmp-type'
            name = have.get('name')
        top_cmd = "object-group {0} {1}".format(object, name)

        granular_delete = False
        if want.get('icmp_object') and have.get('icmp_object'):
            w_icmp_object = want.get('icmp_object')
            h_icmp_object = have.get('icmp_object')

            if h_icmp_object.get('icmp_type'):
                granular_delete = True
                for each in h_icmp_object.get('icmp_type'):
                    for every in w_icmp_object.get('icmp_type'):
                        if every == each:
                            cmd = 'icmp-object {0}'.format(every)
                            self.remove_command_from_config_list(cmd, commands)
        elif want.get('network_object') and have.get('network_object'):
            w_network_object = want.get('network_object')
            h_network_object = have.get('network_object')

            if h_network_object:
                granular_delete = True
                for each in h_network_object:
                    for every in w_network_object:
                        if every.get('host') and every.get('host') == each.get('host') and \
                                every.get('ip_address') == each.get('ip_address'):
                            cmd = "network-object host {0}".format(every.get('ip_address'))
                            self.remove_command_from_config_list(cmd, commands)
                            break
                        if every.get('ip_address') and every.get('ip_address') == each.get('ip_address') and \
                                every.get('ip_mask') == each.get('ip_mask'):
                            cmd = "network-object {0} {1}".format(every.get('ip_address'), every.get('ip_mask'))
                            self.remove_command_from_config_list(cmd, commands)
                            break
                        if every.get('ipv6_address') == each.get('ipv6_address') and every.get('ipv6_address'):
                            cmd = "network-object {0}".format(every.get('ipv6_address'))
                            self.remove_command_from_config_list(cmd, commands)
                            break
                        if every.get('object') and every.get('object') == each.get('object'):
                            cmd = "network-object object {0}".format(every.get('object'))
                            self.remove_command_from_config_list(cmd, commands)
                            break
        elif want.get('protocol_object') and have.get('protocol_object'):
            w_protocol_object = want.get('protocol_object')
            h_protocol_object = have.get('protocol_object')

            if h_protocol_object.get('protocol'):
                granular_delete = True
                for each in h_protocol_object.get('protocol'):
                    for every in w_protocol_object.get('protocol'):
                        if every == each:
                            cmd = 'protocol-object {0}'.format(every)
                            self.remove_command_from_config_list(cmd, commands)
                            break
        elif want.get('security_group') and have.get('security_group'):
            w_security_group = want.get('security_group')
            h_security_group = have.get('security_group')

            if h_security_group.get('name'):
                granular_delete = True
                for each in h_security_group:
                    for every in w_security_group:
                        if every.get('name') == each.get('name'):
                            cmd = "security-group name {0}".format(every.get('name'))
                            self.remove_command_from_config_list(cmd, commands)
                            break
                        if every.get('tag') == each.get('tag'):
                            cmd = "security-group tag {0}".format(every.get('tag'))
                            self.remove_command_from_config_list(cmd, commands)
                            break
        elif want.get('service_object') and have.get('service_object'):
            w_service_object = want.get('service_object')
            h_service_object = have.get('service_object')

            if h_service_object.get('protocol'):
                granular_delete = True
                for each in h_service_object.get('protocol'):
                    for every in w_service_object.get('protocol'):
                        if every == each:
                            cmd = 'service-object {0}'.format(every)
                            self.remove_command_from_config_list(cmd, commands)
                            break
        elif want.get('user_group') and have.get('user_group'):
            w_user_group = want.get('user_group')
            h_user_group = have.get('user_group')
            if h_user_group.get('name') and w_user_group.get('name') == h_user_group.get('name'):
                granular_delete = True
                for each in h_user_group.get('name'):
                    for every in w_user_group.get('name'):
                        if every == each:
                            cmd = 'user-group {0}'.format(every)
                            self.remove_command_from_config_list(cmd, commands)
                            break

        if granular_delete:
            if len(commands) > 0:
                commands.insert(0, top_cmd)
        elif want or have and not granular_delete:
            self.remove_command_from_config_list(top_cmd, commands)


        return commands