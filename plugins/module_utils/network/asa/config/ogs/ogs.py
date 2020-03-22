#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The asa_ogs class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import copy
from ansible.module_utils.six import iteritems
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
    remove_duplicate_cmd,
)


class OGs(ConfigBase):
    """
    The asa_ogs class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ogs',
    ]

    def __init__(self, module):
        super(OGs, self).__init__(module)

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

        for each_want in want:
            for each_have in have:
                if each_have['name'] == each_want['name']:
                    break
            else:
                commands.extend(self._set_config(remove_empties(each_want), dict()))
                continue
            commands.extend(self._clear_config(remove_empties(each_want), each_have, 'replaced'))
            commands.extend(self._set_config(remove_empties(each_want), each_have))
            # Remove duplicate object-group cmd if any
            commands = remove_duplicate_cmd('object-group', commands)

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
        temp_want = copy.copy(want)

        for each_have in have:
            for each_want in temp_want:
                count = 0
                if each_want['name'] == each_have['name']:
                    break
                count += 1
            else:
                # We didn't find a matching desired state, which means we can
                # pretend we recieved an empty desired state.
                commands.extend(self._clear_config(dict(), each_have, 'overridden'))
                continue
            commands.extend(self._clear_config(remove_empties(each_want), each_have, 'overridden'))
            commands.extend(self._set_config(remove_empties(each_want), each_have))
            # Remove duplicate object-group cmd if any
            commands = remove_duplicate_cmd('object-group', commands)
            # as the pre-existing interface are now configured by
            # above set_config call, deleting the respective
            # interface entry from the want list
            del temp_want[count]

        # Iterating through want list which now only have new interfaces to be
        # configured
        for each in temp_want:
            commands.extend(self._set_config(remove_empties(each), dict()))

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
                commands.extend(self._clear_config(remove_empties(each_want), each_have, 'deleted'))
        else:
            for each in have:
                commands.extend(self._clear_config(dict(), each))
        # Remove duplicate object-group cmd if any
        commands = remove_duplicate_cmd('object-group', commands)

        return commands

    def add_command_to_config_list(self, cmd, commands):
        if cmd not in commands:
            commands.append(cmd)

    def new_dict_to_set(self, input_dict, temp_list, test_set, count=0):
        # recursive function to convert input dict to set for comparision
        test_dict = dict()
        if isinstance(input_dict, dict):
            input_dict_len = len(input_dict)
            for k, v in sorted(iteritems(input_dict)):
                count += 1
                if isinstance(v, list):
                    temp_list.append(k)
                    for each in v:
                        if isinstance(each, dict):
                            if [True for i in each.values() if type(i) == list]:
                                self.new_dict_to_set(each, temp_list, test_set, count)
                            else:
                                self.new_dict_to_set(each, temp_list, test_set, 0)
                if isinstance(v, dict):
                    if tuple(iteritems(test_dict)) not in test_set:
                        test_set.add(tuple(iteritems(test_dict)))
                    self.new_dict_to_set(v, temp_list, test_set, 0)
                else:
                    if v is not None:
                        if isinstance(v, list):
                            test_dict.update({k: tuple(v)})
                        else:
                            test_dict.update({k: v})
                    if (
                            tuple(iteritems(test_dict)) not in test_set
                            and count == input_dict_len
                    ):
                        test_set.add(tuple(iteritems(test_dict)))
                        count = 0

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
        self.new_dict_to_set(want, [], want_set)
        temp = {}
        if have:
            self.new_dict_to_set(have, [], have_set)
            for each in want_set:
                for every in have_set:
                    want_keys = dict(each).keys()
                    have_keys = dict(every).keys()
                    if any(elem in have_keys for elem in want_keys) and (dict(each).get('object_type') == dict(every).get('object_type')):
                        diff = set(each) - set(every)
                        if diff:
                            for k, v in dict(each).items():
                                if k == 'description':
                                    temp.update({k: v})
                                elif dict(every).get(k):
                                    temp_diff = set(v) - set(dict(every).get(k))
                                    if temp_diff:
                                        temp.update({k: tuple(temp_diff)})
                                else:
                                    temp.update({k: v})
        else:
            for each in want_set:
                # In case of security_group object, since the temp dict might
                # have colliding duplicate name param it's a condition to get the
                # security object name param and store it as security_name in the
                # temp dict instead of overriding the value with one-another
                if 'object_type' not in dict(each):
                    if 'name' in dict(each) or 'tag' in dict(each):
                        temp['security_name'] = dict(each).get('name')
                        temp['tag'] = dict(each).get('tag')
                    else:
                        temp.update(dict(each))
                else:
                    temp.update(dict(each))

        if temp:
            og_name = want.get('name')
            og_object = want.get('object_type')
            cmd = 'object-group {0} {1}'.format(og_object, og_name)
            self.add_command_to_config_list(cmd, commands)
            description = temp.get('description')
            if description:
                cmd = 'description {0}'.format(description)
                self.add_command_to_config_list(cmd, commands)
            if og_object == 'icmp-type':
                icmp_type = temp.get('icmp_type')
                if icmp_type:
                    for each in icmp_type:
                        cmd = 'icmp-object {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)
            elif og_object == 'network':
                host = temp.get('host')
                address = temp.get('address')
                ipv6_address = temp.get('ipv6_address')
                group_object = temp.get('group_object')
                if host:
                    for each in host:
                        cmd = 'network-object host {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)
                if address:
                    for each in address:
                        cmd = 'network-object {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)
                if ipv6_address:
                    for each in ipv6_address:
                        cmd = 'network-object {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)
                if group_object:
                    cmd = 'group-object {0}'.format(group_object)
                    self.add_command_to_config_list(cmd, commands)
            elif og_object == 'protocol':
                protocol = temp.get('protocol')
                if protocol:
                    for each in protocol:
                        cmd = 'protocol-object {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)
            elif og_object == 'security':
                security_name = temp.get('security_name')
                if security_name:
                    name = security_name
                elif temp.get('name') != want.get('name'):
                    name = temp.get('name')
                else:
                    name = []
                tag = temp.get('tag')
                if name:
                    for each in name:
                        cmd = 'security-group name {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)
                if tag:
                    for each in tag:
                        cmd = 'security-group tag {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)
            elif og_object == 'service':
                protocol = temp.get('protocol')
                for each in protocol:
                    cmd = 'service-object {0}'.format(each)
                    self.add_command_to_config_list(cmd, commands)
            elif og_object == 'user':
                user = temp.get('user')
                user_group = temp.get('user_group')
                if user:
                    for each in user:
                        cmd = 'user {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)
                if user_group:
                    for each in user_group:
                        cmd = 'user-group {0}'.format(each)
                        self.add_command_to_config_list(cmd, commands)

        return commands

    def remove_command_from_config_list(self, cmd, commands):
        # To delete the passed config
        if cmd not in commands:
            commands.append('no %s' % cmd)

    def common_config_compute(self, want, have, object, commands, state, key=False):
        # Common code used to delete objects from available object-groups
        cmd = ''
        valid_state = False
        for k, v in iteritems(want):
            if have.get(k):
                if all(elem in have.get(k) for elem in want[k]):
                    for each in want[k]:
                        if key and k != 'address' and k != 'ipv6_address':
                            cmd = '{0} {1} {2}'.format(object, k, each)
                        else:
                            cmd = '{0} {1}'.format(object, each)
                        self.remove_command_from_config_list(cmd, commands)
                elif state == 'replaced' or state == 'overridden':
                    valid_state = True
        return cmd, valid_state

    def _clear_config(self, want, have, state=''):
        """ Function that deletes the acl config based on the want and have config
        :param acl: acl config
        :param config: config
        :rtype: A list
        :returns: the commands generated based on input acl/config params
        """
        commands = []

        if want:
            object = want.get('object_type')
            name = want.get('name')
        else:
            object = have.get('object_type')
            name = have.get('name')
        top_cmd = "object-group {0} {1}".format(object, name)

        valid_state = False
        granular_delete = False
        cmd = ''
        w_description = want.get('description')
        h_description = have.get('description')
        if w_description and h_description and (w_description != h_description or state == 'deleted'):
            cmd = 'description {0}'.format(w_description)
            commands.insert(0, top_cmd)
            self.remove_command_from_config_list(cmd, commands)
            granular_delete = True

        if want.get('icmp_object') and have.get('icmp_object'):
            w_icmp_object = want.get('icmp_object')
            h_icmp_object = have.get('icmp_object')
            if w_icmp_object != h_icmp_object:
                cmd, valid_state = self.common_config_compute(w_icmp_object, h_icmp_object, 'icmp-object', commands, state, False)
            granular_delete = True
        elif want.get('network_object') and have.get('network_object'):
            w_network_object = want.get('network_object')
            h_network_object = have.get('network_object')
            if w_network_object != h_network_object:
                cmd, valid_state = self.common_config_compute(w_network_object, h_network_object, 'network-object', commands, state, True)
            granular_delete = True
        elif want.get('protocol_object') and have.get('protocol_object'):
            w_protocol_object = want.get('protocol_object')
            h_protocol_object = have.get('protocol_object')
            if w_protocol_object != h_protocol_object:
                cmd, valid_state = self.common_config_compute(w_protocol_object, h_protocol_object, 'protocol-object', commands, state, False)
            granular_delete = True
        elif want.get('security_group') and have.get('security_group'):
            w_security_group = want.get('security_group')
            h_security_group = have.get('security_group')
            if w_security_group != h_security_group:
                cmd, valid_state = self.common_config_compute(w_security_group, h_security_group, 'security-group', commands, state, True)
            granular_delete = True
        elif want.get('service_object') and have.get('service_object'):
            w_service_object = want.get('service_object')
            h_service_object = have.get('service_object')
            if w_service_object != h_service_object:
                cmd, valid_state = self.common_config_compute(w_service_object, h_service_object, 'service-object', commands, state, False)
            granular_delete = True
        elif want.get('user_object') and have.get('user_object'):
            w_user_object = want.get('user_object')
            h_user_object = have.get('user_object')
            if w_user_object != h_user_object:
                for k, v in iteritems(w_user_object):
                    if h_user_object.get(k):
                        if all(elem in h_user_object.get(k) for elem in w_user_object[k]):
                            for each in w_user_object[k]:
                                cmd = '{0} {1}'.format(k, each)
                                self.remove_command_from_config_list(cmd, commands)
                        elif state == 'replaced' or state == 'overridden':
                            valid_state = True
            granular_delete = True

        if cmd:
            if len(commands) > 0:
                commands.insert(0, top_cmd)
        elif (want or have) and not granular_delete:
            commands = []
            self.remove_command_from_config_list(top_cmd, commands)
        elif valid_state and (state == 'replaced' or state == 'overridden'):
            if commands:
                commands = []
            self.remove_command_from_config_list(top_cmd, commands)

        return commands
