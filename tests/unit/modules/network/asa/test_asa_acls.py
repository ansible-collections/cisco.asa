#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import sys

import pytest

# These tests and/or the module under test are unstable on Python 3.5.
# See: https://app.shippable.com/github/ansible/ansible/runs/161331/15/tests
# This is most likely due to CPython 3.5 not maintaining dict insertion order.
pytestmark = pytest.mark.skipif(
    sys.version_info[:2] == (3, 5),
    reason="Tests and/or module are unstable on Python 3.5.",
)

from ansible_collections.cisco.asa.tests.unit.compat.mock import patch
from ansible_collections.cisco.asa.plugins.modules import asa_acls
from ansible_collections.cisco.asa.tests.unit.modules.utils import (
    set_module_args,
)
from .asa_module import TestAsaModule, load_fixture


class TestAsaAclsModule(TestAsaModule):
    module = asa_acls

    def setUp(self):
        super(TestAsaAclsModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config"
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base."
            "get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts."
            "get_resource_connection"
        )
        self.get_resource_connection_facts = (
            self.mock_get_resource_connection_facts.start()
        )

        self.mock_edit_config = patch(
            "ansible_collections.cisco.asa.plugins.module_utils.network.asa.providers.providers.CliProvider.edit_config"
        )
        self.edit_config = self.mock_edit_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.asa.plugins.module_utils.network.asa.facts.acls.acls."
            "AclsFacts.get_acls_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestAsaAclsModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_edit_config.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli"):
        def load_from_file(*args, **kwargs):
            return load_fixture("asa_acls_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_asa_acls_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        acls=[
                            dict(
                                name="test_global_access",
                                acl_type="extended",
                                aces=[
                                    dict(
                                        destination=dict(
                                            any="true",
                                            port_protocol=dict(eq="www"),
                                        ),
                                        grant="deny",
                                        line=1,
                                        log="errors",
                                        protocol="tcp",
                                        protocol_options=dict(tcp="true"),
                                        source=dict(any="true"),
                                    )
                                ],
                            )
                        ]
                    ),
                    dict(
                        acls=[
                            dict(
                                name="merge_v6_acl",
                                aces=[
                                    dict(
                                        destination=dict(
                                            address="2001:fc8:0:6::/64",
                                            port_protocol=dict(eq="telnet"),
                                        ),
                                        grant="deny",
                                        inactive="true",
                                        protocol="tcp",
                                        protocol_options=dict(tcp="true"),
                                        source=dict(
                                            address="2001:db8:0:5::/64",
                                            port_protocol=dict(eq="www"),
                                        ),
                                    )
                                ],
                            )
                        ]
                    ),
                    dict(
                        acls=[
                            dict(
                                name="test_access",
                                aces=[
                                    dict(
                                        source=dict(host="192.0.2.2"),
                                        line=2,
                                        remark="test_merge_host",
                                    )
                                ],
                            )
                        ]
                    ),
                ],
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            "access-list test_global_access line 1 extended deny tcp any any eq www log errors",
            "access-list merge_v6_acl deny tcp 2001:db8:0:5::/64 eq www 2001:fc8:0:6::/64 eq telnet inactive",
            "no access-list test_access line 2 remark host1 extended deny tcp host 192.0.2.1 any eq www log default",
            "access-list test_access line 2 remark test_merge_host deny tcp host 192.0.2.2 any eq www log default",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_acls_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        acls=[
                            dict(
                                aces=[
                                    dict(
                                        destination=dict(
                                            address="192.0.3.0",
                                            netmask="255.255.255.0",
                                            port_protocol=dict(eq="www"),
                                        ),
                                        grant="deny",
                                        line=1,
                                        log="default",
                                        protocol="tcp",
                                        protocol_options=dict(tcp="true"),
                                        source=dict(
                                            address="192.0.2.0",
                                            netmask="255.255.255.0",
                                        ),
                                    ),
                                    dict(
                                        destination=dict(
                                            any="true",
                                            port_protocol=dict(eq="www"),
                                        ),
                                        grant="deny",
                                        line=2,
                                        log="default",
                                        protocol="tcp",
                                        protocol_options=dict(tcp="true"),
                                        remark="host1",
                                        source=dict(host="192.0.2.1"),
                                    ),
                                    dict(
                                        destination=dict(any="true"),
                                        grant="permit",
                                        line=3,
                                        protocol="ip",
                                        protocol_options=dict(ip="true"),
                                        remark="host2",
                                        source=dict(host="192.0.2.2"),
                                    ),
                                ],
                                name="test_access",
                                acl_type="extended",
                            )
                        ]
                    )
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_acls_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        acls=[
                            dict(
                                name="test_access",
                                acl_type="extended",
                                aces=[
                                    dict(
                                        destination=dict(
                                            address="198.51.110.0",
                                            netmask="255.255.255.0",
                                        ),
                                        grant="deny",
                                        line=1,
                                        log="default",
                                        protocol="igrp",
                                        protocol_options=dict(igrp="true"),
                                        source=dict(
                                            address="198.51.100.0",
                                            netmask="255.255.255.0",
                                        ),
                                        time_range="temp",
                                    )
                                ],
                            )
                        ]
                    )
                ],
                state="replaced",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            "no access-list test_access line 3 remark host2 extended permit ip host 192.0.2.2 any",
            "no access-list test_access line 2 remark host1 extended deny tcp host 192.0.2.1 any eq www log default",
            "no access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default",
            "access-list test_access line 1 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log default time-range temp",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_acls_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        acls=[
                            dict(
                                name="test_access",
                                acl_type="extended",
                                aces=[
                                    dict(
                                        destination=dict(
                                            address="192.0.3.0",
                                            netmask="255.255.255.0",
                                            port_protocol=dict(eq="www"),
                                        ),
                                        grant="deny",
                                        line=1,
                                        log="default",
                                        protocol="tcp",
                                        protocol_options=dict(tcp="true"),
                                        source=dict(
                                            address="192.0.2.0",
                                            netmask="255.255.255.0",
                                        ),
                                    )
                                ],
                            )
                        ]
                    )
                ],
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_acls_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        acls=[
                            dict(
                                name="test_global_access",
                                acl_type="extended",
                                aces=[
                                    dict(
                                        destination=dict(
                                            any="true",
                                            port_protocol=dict(eq="www"),
                                        ),
                                        grant="deny",
                                        line=1,
                                        log="errors",
                                        protocol="tcp",
                                        protocol_options=dict(tcp="true"),
                                        source=dict(any="true"),
                                    )
                                ],
                            )
                        ]
                    )
                ],
                state="overridden",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            "no access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive",
            "no access-list test_access line 3 remark host2 extended permit ip host 192.0.2.2 any",
            "no access-list test_access line 2 remark host1 extended deny tcp host 192.0.2.1 any eq www log default",
            "no access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default",
            "access-list test_global_access line 1 extended deny tcp any any eq www log errors",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_acls_deleted_all(self):
        set_module_args(dict(state="deleted"))
        result = self.execute_module(changed=True)
        commands = [
            "no access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive",
            "no access-list test_access line 3 remark host2 extended permit ip host 192.0.2.2 any",
            "no access-list test_access line 2 remark host1 extended deny tcp host 192.0.2.1 any eq www log default",
            "no access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 eq www log default",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_acls_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        acls=[
                            dict(
                                name="test_access",
                                acl_type="extended",
                                aces=[
                                    dict(
                                        destination=dict(
                                            address="192.0.3.0",
                                            netmask="255.255.255.0",
                                        ),
                                        grant="deny",
                                        line=1,
                                        log="default",
                                        protocol="tcp",
                                        protocol_options=dict(tcp="true"),
                                        source=dict(
                                            address="192.0.2.0",
                                            netmask="255.255.255.0",
                                        ),
                                    )
                                ],
                            )
                        ]
                    )
                ],
                state="rendered",
            )
        )
        commands = [
            "access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 192.0.3.0 255.255.255.0 log default"
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(result["rendered"], commands)
