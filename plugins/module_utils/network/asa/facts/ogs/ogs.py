#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The asa_og fact class
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
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.argspec.ogs.ogs import (
    OGsArgs,
)


class OGsFacts(object):
    """ The asa_og fact class
    """

    def __init__(self, module, subspec='config', options='options'):

        self._module = module
        self.argument_spec = OGsArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_og_data(self, connection):
        return connection.get('sh running-config object-group')

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for ogs
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        objs = []
        if not data:
            data = self.get_og_data(connection)
        # operate on a collection of resource x
        config = data.split('object-group ')
<<<<<<< HEAD

=======
>>>>>>> 936b102 (asa_ogs update)
        for conf in config:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
                if obj:
                    objs.append(obj)
        facts = {}

        if objs:
            facts['ogs'] = []
            params = utils.validate_config(self.argument_spec, {'config': objs})
            for cfg in params['config']:
                facts['ogs'].append(utils.remove_empties(cfg))
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts


    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values
        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)

        if conf:
            if conf.split(' ')[0] in ['network', 'protocol', 'security', 'service', 'user']:
                object = conf.split(' ')[0]
                name_object = utils.parse_conf_arg(conf, object)
                config['object'] = object
                config['name'] = name_object
            elif conf.split(' ')[0] == 'icmp-type':
                object = conf.split(' ')[0]
                name_object = utils.parse_conf_arg(conf, object)
                config['object'] = 'icmp_type'
                config['name'] = name_object
            description = utils.parse_conf_arg(conf, 'description')
            if description:
                config['description'] = description.rstrip()
            group_object = utils.parse_conf_arg(conf, 'group-object')
            if group_object:
                config['group_object'] = group_object.rstrip()
            icmp_object = re.findall('icmp-object (.+)', conf)
            if icmp_object:
                icmp_type = []
                for every in icmp_object:
                    icmp_type.append(every.rstrip())
                config['icmp_object'] = {'icmp_type': icmp_type}
<<<<<<< HEAD
                #config['icmp_object'] = ({'icmp_object': icmp_object})
            network_object = re.findall('network-object (.+)', conf)
            if network_object:
                for every in network_object:
                    host = utils.parse_conf_arg(every, 'host')
                    network = {}
                    if host:
                        network['host'] = True
                        network['ip_address'] = host
                    elif ':' in every:
                        network['ipv6_address'] = every
                    else:
                        network_object = every.split(' ')
                        network['ip_address'] = network_object[0]
                        network['ip_mask'] = network_object[1]
                    if config.get('network_object'):
                        config['network_object'].append(network)
                    else:
                        config['network_object'] = []
                        config['network_object'].append(network)
=======

            if utils.parse_conf_arg(conf, 'network'):
                host = re.findall('host (.+)', conf)
                all_address = re.findall('network-object (.+)', conf)
                address = [each for each in all_address if 'host' not in each and ':' not in each]
                ipv6_address = [each for each in all_address if ':' in each]
                config['network_object'] = {}
                if host:
                    config['network_object'].update({'host': host})
                if address:
                    config['network_object'].update({'address': address})
                if ipv6_address:
                    config['network_object'].update({'ipv6_address': ipv6_address})

>>>>>>> 936b102 (asa_ogs update)
            protocol_object = re.findall('protocol-object (.+)', conf)
            if protocol_object:
                protocol = []
                for every in protocol_object:
                    protocol.append(every.rstrip())
                config['protocol_object'] = {'protocol': protocol}
<<<<<<< HEAD
            security_group = re.findall('security-group (.+)', conf)
            if security_group:
                security = {}
                for every in security_group:
                    name = utils.parse_conf_arg(every, 'name')
                    tag = utils.parse_conf_arg(every, 'tag')
                    if name:
                        security['name'] = name
                    if tag:
                        security['tag'] = int(tag)
                if config.get('security_group'):
                    config['security_group'].append(security)
                else:
                    config['security_group'] = []
                    config['security_group'].append(security)
=======

            if utils.parse_conf_arg(conf, 'security'):
                security_group_name = re.findall('name (.+)', conf)
                security_group_tag = re.findall('tag (.+)', conf)
                config['security_group'] = {}
                if security_group_name:
                    config['security_group'].update({'name': security_group_name})
                if security_group_tag:
                    security_group_tag = [int(each) for each in security_group_tag]
                    config['security_group'].update({'tag': security_group_tag})
>>>>>>> 936b102 (asa_ogs update)
            service_object = re.findall('service-object (.+)', conf)
            if service_object:
                protocol = []
                for every in service_object:
                    protocol.append(every.rstrip())
<<<<<<< HEAD
                config['service_object'] = {'protocol': protocol}
            user_group = utils.parse_conf_arg(conf, 'user-object')
            if user_group:
                name = utils.parse_conf_arg(security_group, 'name')
                user = {}
                if name:
                    user['name'] = name
                if config.get('user_group'):
                    config['user_group'].append(user)
                else:
                    config['user_group'] = []
                    config['user_group'].append(user)
=======
                if object and protocol:
                    config['service_object'] = {'protocol': protocol, 'object': object}
                elif object and not protocol:
                    config['service_object'] = {'object': object}
                elif not object and protocol:
                    config['service_object'] = {'protocol': protocol}
            user_object = utils.parse_conf_arg(conf, 'user')
            if user_object:
                users = re.findall('user (.+)', conf)
                users = [each.split('LOCAL\\')[1] for each in users if 'LOCAL' in each]
                user_groups = re.findall('user-group (.+)', conf)
                if users and user_groups:
                    config['user_object'] = {'user': users, 'user_group': user_groups}
                elif users and not user_groups:
                    config['user_object'] = {'user': users}
                elif not users and user_groups:
                    config['user_object'] = {'user_group': user_groups}
>>>>>>> 936b102 (asa_ogs update)

        return utils.remove_empties(config)