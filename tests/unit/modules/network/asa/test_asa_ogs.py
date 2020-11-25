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
from ansible_collections.cisco.asa.plugins.modules import asa_ogs
from ansible_collections.cisco.asa.tests.unit.modules.utils import (
    set_module_args,
)
from .asa_module import TestAsaModule, load_fixture


class TestAsaOGsModule(TestAsaModule):
    module = asa_ogs

    def setUp(self):
        super(TestAsaOGsModule, self).setUp()

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
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module."
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
            "ansible_collections.cisco.asa.plugins.module_utils.network.asa.facts.ogs.ogs."
            "OGsFacts.get_og_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestAsaOGsModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_edit_config.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli"):
        def load_from_file(*args, **kwargs):
            return load_fixture("asa_ogs_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_asa_ogs_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_groups=[
                            dict(
                                name="test_network_og",
                                description="test network og",
                                network_object=dict(
                                    host=["192.0.3.1", "192.0.3.2"],
                                    ipv6_address=["2001:db8:0:3::/64"],
                                ),
                            )
                        ],
                        object_type="network",
                    )
                ],
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            "object-group network test_network_og",
            "description test network og",
            "network-object host 192.0.3.1",
            "network-object host 192.0.3.2",
            "network-object 2001:db8:0:3::/64",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_ogs_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_groups=[
                            dict(
                                description="test_og_network",
                                name="test_og_network",
                                network_object=dict(
                                    host=["192.0.2.1"],
                                    address=["192.0.2.0 255.255.255.0"],
                                ),
                            )
                        ],
                        object_type="network",
                    ),
                    dict(
                        object_groups=[
                            dict(
                                name="test_og_service",
                                service_object=dict(
                                    protocol=["ipinip", "tcp-udp"]
                                ),
                            )
                        ],
                        object_type="service",
                    ),
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_ogs_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_groups=[
                            dict(
                                name="test_og_network",
                                description="test_og_network_replace",
                                network_object=dict(
                                    host=["192.0.3.1"],
                                    address=["192.0.3.0 255.255.255.0"],
                                ),
                            )
                        ],
                        object_type="network",
                    )
                ],
                state="replaced",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            "object-group network test_og_network",
            "description test_og_network_replace",
            "no network-object 192.0.2.0 255.255.255.0",
            "network-object 192.0.3.0 255.255.255.0",
            "no network-object host 192.0.2.1",
            "network-object host 192.0.3.1",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_ogs_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_groups=[
                            dict(
                                description="test_og_network",
                                name="test_og_network",
                                network_object=dict(
                                    host=["192.0.2.1"],
                                    address=["192.0.2.0 255.255.255.0"],
                                ),
                            )
                        ],
                        object_type="network",
                    ),
                    dict(
                        object_groups=[
                            dict(
                                name="test_og_service",
                                service_object=dict(
                                    protocol=["ipinip", "tcp-udp"]
                                ),
                            )
                        ],
                        object_type="service",
                    ),
                ],
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_ogs_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_groups=[
                            dict(
                                name="test_og_network",
                                description="test_og_network_override",
                                network_object=dict(
                                    host=["192.0.3.1"],
                                    address=["192.0.3.0 255.255.255.0"],
                                ),
                            )
                        ],
                        object_type="network",
                    )
                ],
                state="overridden",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            "no object-group service test_og_service",
            "object-group network test_og_network",
            "description test_og_network_override",
            "no network-object 192.0.2.0 255.255.255.0",
            "network-object 192.0.3.0 255.255.255.0",
            "no network-object host 192.0.2.1",
            "network-object host 192.0.3.1",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_ogs_overridden_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_groups=[
                            dict(
                                description="test_og_network",
                                name="test_og_network",
                                network_object=dict(
                                    host=["192.0.2.1"],
                                    address=["192.0.2.0 255.255.255.0"],
                                ),
                            )
                        ],
                        object_type="network",
                    ),
                    dict(
                        object_groups=[
                            dict(
                                name="test_og_service",
                                service_object=dict(
                                    protocol=["ipinip", "tcp-udp"]
                                ),
                            )
                        ],
                        object_type="service",
                    ),
                ],
                state="overridden",
            )
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_ogs_delete_by_name(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_groups=[dict(name="test_og_network")],
                        object_type="network",
                    )
                ],
                state="deleted",
            )
        )
        result = self.execute_module(changed=True)
        commands = ["no object-group network test_og_network"]
        self.assertEqual(result["commands"], commands)

    def test_asa_ogs_deleted_all(self):
        set_module_args(dict(state="deleted"))
        result = self.execute_module(changed=True)
        commands = [
            "no object-group network test_og_network",
            "no object-group service test_og_service",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_ogs_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_groups=[
                            dict(
                                description="test_og_network",
                                name="test_og_network",
                                network_object=dict(
                                    host=["192.0.2.1"],
                                    address=["192.0.2.0 255.255.255.0"],
                                ),
                            )
                        ],
                        object_type="network",
                    ),
                    dict(
                        object_groups=[
                            dict(
                                name="test_og_service",
                                service_object=dict(
                                    protocol=["ipinip", "tcp-udp"]
                                ),
                            )
                        ],
                        object_type="service",
                    ),
                ],
                state="rendered",
            )
        )
        commands = [
            "object-group network test_og_network",
            "description test_og_network",
            "network-object 192.0.2.0 255.255.255.0",
            "network-object host 192.0.2.1",
            "object-group service test_og_service",
            "service-object ipinip",
            "service-object tcp-udp",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(result["rendered"], commands)
