# -*- coding: utf-8 -*-
# Copyright 2025 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The asa asa_objects fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.rm_templates.asa_objects import (
    Asa_objectsTemplate,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.argspec.asa_objects.asa_objects import (
    Asa_objectsArgs,
)

class Asa_objectsFacts(object):
    """ The asa asa_objects facts class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Asa_objectsArgs.argument_spec

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Asa_objects network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []

        if not data:
            # in ASA object and object nat configurations are in different sections
            data = connection.get("sh running-config object") + "\n" + connection.get("sh running-config nat | exclude ^nat")

        # parse native config using the Asa_objects template
        asa_objects_parser = Asa_objectsTemplate(lines=data.splitlines(), module=self._module)
        # objs = list(asa_objects_parser.parse().values())
        current = asa_objects_parser.parse()
        if current.get("objects"):
            for k, v in iteritems(current.get("objects")):
                obj = {}
                config_dict = {}
                config_dict["object_type"] = k
                config_dict["objects"] = []
                for each in iteritems(v):
                    obj["name"] = each[1].pop("name")
                    each[1].pop("object_type")
                    if each[1].get("description"):
                        obj["description"] = each[1].pop("description")
                    if k == "network":
                        if each[1].get("host"):
                            obj["host"] = each[1].pop("host")
                        if each[1].get("subnet"):
                            obj["subnet"] = each[1].pop("subnet")
                        if each[1].get("range"):
                            obj["range"] = each[1].pop("range")
                        if each[1].get("fqdn"):
                            obj["fqdn"] = each[1].pop("fqdn")
                        if each[1].get("fqdn_v4"):
                            obj["fqdn_v4"] = each[1].pop("fqdn_v4")
                        if each[1].get("fqdn_v6"):
                            obj["fqdn_v6"] = each[1].pop("fqdn_v6")
                        if each[1].get("nat"):
                            obj["nat"] = each[1].pop("nat")
                    else:
                        if each[1].get("service"):
                            obj["service"] = each[1].pop("service")
                    config_dict["objects"].append(obj)
                    obj = {}
                config_dict["objects"] = sorted(
                    config_dict["objects"],
                    key=lambda k, sk="name": str(k[sk]),
                )
                objs.append(config_dict)

        # sort the object group list of dict by object_type
        objs = sorted(objs, key=lambda i: i["object_type"])

        # ansible_facts['ansible_network_resources'].pop('asa_objects', None)

        params = utils.remove_empties(
            asa_objects_parser.validate_config(self.argument_spec, {"config": objs}, redact=True)
        )

        facts['asa_objects'] = params.get('config')
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts
