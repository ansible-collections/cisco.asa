#
# -*- coding: utf-8 -*-
# Copyright 2025 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The asa_objects config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
    to_list,
    get_from_dict,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.facts.facts import (
    Facts,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.rm_templates.objects import (
    ObjectsTemplate,
)


class Objects(ResourceModule):
    """
    The asa_objects config class
    """

    def __init__(self, module):
        super(Objects, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="objects",
            tmplt=ObjectsTemplate(),
        )
        self.parsers = [
            "obj_name",
            "description",
            "obj_host",
            "obj_subnet",
            "obj_range",
            "obj_fqdn_v4",
            "obj_fqdn_v6",
            "obj_fqdn",
            "obj_service",
            "obj_nat",
        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """

        obj = {}
        for v in self.want:
            for each in v.get("objects"):
                obj[each.get("name")] = each
                obj[each.get("name")]["object_type"] = v.get("object_type")
        wantd = obj

        obj = {}
        for v in self.have:
            for each in v.get("objects"):
                obj[each.get("name")] = each
                obj[each.get("name")]["object_type"] = v.get("object_type")
        haved = obj

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {
                k: v for k, v in iteritems(haved) if k in wantd or not wantd
            }
            wantd = {}

        # remove superfluous config for overridden and deleted
        if self.state in ["overridden", "deleted"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    self._compare(want={}, have=have)

        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}))

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Asa_objects network resource.
        """
        # import epdb; epdb.serve()

        # self.compare(parsers=self.parsers, want=want, have=have)
        # changing object type is only possible by removal old object first
        if get_from_dict(want, "object_type") != get_from_dict(have, "object_type"):
            self.addcmd(have, "obj_name", True)
            have = {}

        # need to add `object` command only once
        obj_cmd_added = False

        for parser in to_list(self.parsers):
            compval = self._tmplt.get_parser(parser).get("compval")
            if not compval:
                compval = parser

            inw = get_from_dict(want, compval)
            inh = get_from_dict(have, compval)

            if isinstance(inw, dict) and inw.get("set") is False and not inh:
                continue

            # remove description and nat if they're no longer wanted
            if parser in ["description", "obj_nat"] and inw is None and inh is not None:
                # need to prepend command set with `object obj_type obj_name` command
                if not obj_cmd_added:
                    self.addcmd(want, "obj_name", False)
                    obj_cmd_added = True
                self.addcmd(have, parser, True)

            if inw is not None and inw != inh:
                # need to prepend command set with `object obj_type obj_name` command
                if not obj_cmd_added:
                    self.addcmd(want, "obj_name", False)
                    obj_cmd_added = True
                # don't need negate commands as they overwrite one another
                if isinstance(inw, bool):
                    if inw is False and inh is None:
                        continue
                    self.addcmd(want, parser, not inw)
                else:
                    self.addcmd(want, parser, False)
