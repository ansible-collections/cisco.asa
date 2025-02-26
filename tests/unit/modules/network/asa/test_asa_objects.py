#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.cisco.asa.plugins.modules import asa_objects
from ansible_collections.cisco.asa.tests.unit.modules.utils import set_module_args

from .asa_module import TestAsaModule, load_fixture


class TestAsaObjectsModule(TestAsaModule):
    module = asa_objects

    def setUp(self):
        super(TestAsaObjectsModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base."
            "get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_edit_config = patch(
            "ansible_collections.cisco.asa.plugins.module_utils.network.asa.providers.providers.CliProvider.edit_config",
        )
        self.edit_config = self.mock_edit_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.asa.plugins.module_utils.network.asa.facts.objects.objects."
            "ObjectsFacts.get_objects_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestAsaObjectsModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_edit_config.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli"):
        def load_from_file(*args, **kwargs):
            return load_fixture("asa_objects_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_asa_objects_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_type="network",
                        objects=[
                            dict(
                                description="a test fqdn v4 object",
                                fqdn_v4="microsoft.com",
                                name="test_fqdn_obj",
                            ),
                            dict(
                                description="a test range object",
                                name="test_range_obj",
                                range="10.0.0.1 10.0.0.10",
                            ),
                            dict(
                                description="another test host object",
                                host="1.2.3.4",
                                name="test_host_obj_1",
                            ),
                            dict(
                                name="test_nat_obj",
                            ),
                        ],
                    ),
                    dict(
                        object_type="service",
                        objects=[
                            dict(
                                name="test_tcp_source_range_obj",
                                service=dict(
                                    protocol="tcp",
                                    source_port=dict(
                                        range=dict(
                                            end="5672",
                                            start="5671",
                                        ),
                                    ),
                                ),
                            ),
                            dict(
                                name="test_tcp_eq_obj",
                                service=dict(
                                    destination_port=dict(
                                        eq="https",
                                    ),
                                    protocol="tcp",
                                ),
                            ),
                            dict(
                                name="test_icmp_echo_obj",
                                service=dict(
                                    icmpopt=dict(
                                        name="echo",
                                        code="8",
                                    ),
                                    protocol="icmp",
                                ),
                            ),
                        ],
                    ),
                ],
                state="replaced",
            )
        )

        result = self.execute_module(changed=True)
        commands = [
            "object network test_fqdn_obj",
            "description a test fqdn v4 object",
            "fqdn v4 microsoft.com",
            "object network test_host_obj_1",
            "description another test host object",
            "host 1.2.3.4",
            "object network test_nat_obj",
            "no description a test nat object",
            "no nat (any,any) static 5.6.7.8 net-to-net",
            "object service test_icmp_echo_obj",
            "service icmp echo 8",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_asa_objects_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_type="network",
                        objects=[
                            dict(
                                description="a test fqdn object",
                                fqdn="google.com",
                                name="test_fqdn_obj",
                            ),
                            dict(
                                description="a test range object",
                                name="test_range_obj",
                                range="10.0.0.1 10.0.0.10",
                            ),
                            dict(
                                description="a test host object",
                                host="1.2.3.4",
                                name="test_host_obj",
                            ),
                            dict(
                                name="test_nat_obj",
                                description="a test nat object",
                                nat=dict(
                                    mapped_if="any",
                                    real_if="any",
                                    static=dict(
                                        name="5.6.7.8",
                                        net_to_net=True,
                                    ),
                                ),

                            ),
                        ],
                    ),
                    dict(
                        object_type="service",
                        objects=[
                            dict(
                                name="test_tcp_source_range_obj",
                                service=dict(
                                    protocol="tcp",
                                    source_port=dict(
                                        range=dict(
                                            end="5672",
                                            start="5671",
                                        ),
                                    ),
                                ),
                            ),
                            dict(
                                name="test_tcp_eq_obj",
                                service=dict(
                                    destination_port=dict(
                                        eq="https",
                                    ),
                                    protocol="tcp",
                                ),
                            ),
                            dict(
                                name="test_icmp_echo_obj",
                                service=dict(
                                    icmpopt=dict(
                                        name="echo",
                                    ),
                                    protocol="icmp",
                                ),
                            ),
                        ],
                    ),
                ],
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_objects_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_type="network",
                        objects=[
                            dict(
                                description="a modified test fqdn object",
                                fqdn_v4="microsoft.com",
                                name="test_fqdn_obj",
                            ),
                            dict(
                                description="a test subnet object",
                                name="test_subnet_obj",
                                subnet="10.0.0.0 255.255.255.0",
                            ),
                            dict(
                                description="a test range object",
                                name="test_range_another_obj",
                                range="10.0.10.1 10.0.10.10",
                            ),
                        ],
                    ),
                    dict(
                        object_type="service",
                        objects=[
                            dict(
                                name="test_gre_obj",
                                service=dict(
                                    protocol="gre",
                                ),
                            ),
                        ],
                    ),
                ],
                state="overridden",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            "no object network test_host_obj",
            "no object network test_nat_obj",
            "no object network test_range_obj",
            "no object service test_icmp_echo_obj",
            "no object service test_icmp_echo_repl_code_obj",
            "no object service test_tcp_eq_obj",
            "no object service test_tcp_range_obj",
            "no object service test_tcp_source_eq_obj",
            "no object service test_tcp_source_range_obj",
            "object network test_fqdn_obj",
            "description a modified test fqdn object",
            "fqdn v4 microsoft.com",
            "object network test_range_another_obj",
            "description a test range object",
            "range 10.0.10.1 10.0.10.10",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_asa_objects_overridden_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_type="network",
                        objects=[
                            dict(
                                description="a test fqdn object",
                                fqdn="google.com",
                                name="test_fqdn_obj",
                            ),
                            dict(
                                description="a test host object",
                                host="1.2.3.4",
                                name="test_host_obj",
                            ),
                            dict(
                                description="a test nat object",
                                host="1.2.3.4",
                                name="test_nat_obj",
                                nat=dict(
                                    mapped_if="any",
                                    real_if="any",
                                    static=dict(
                                        name="5.6.7.8",
                                        net_to_net=True,
                                    ),
                                ),
                            ),
                            dict(
                                description="a test range object",
                                name="test_range_obj",
                                range="10.0.0.1 10.0.0.10",
                            ),
                            dict(
                                description="a test subnet object",
                                name="test_subnet_obj",
                                subnet="10.0.0.0 255.255.255.0",
                            ),
                        ],
                    ),
                    dict(
                        object_type="service",
                        objects=[
                            dict(
                                name="test_gre_obj",
                                service=dict(
                                    protocol="gre",
                                ),
                            ),
                            dict(
                                name="test_icmp_echo_obj",
                                service=dict(
                                    icmpopt=dict(
                                        name="echo",
                                    ),
                                    protocol="icmp",
                                ),
                            ),
                            dict(
                                name="test_icmp_echo_repl_code_obj",
                                service=dict(
                                    icmpopt=dict(
                                        code="0",
                                        name="echo-reply",
                                    ),
                                    protocol="icmp",
                                ),
                            ),
                            dict(
                                name="test_tcp_eq_obj",
                                service=dict(
                                    destination_port=dict(
                                        eq="https",
                                    ),
                                    protocol="tcp",
                                )
                            ),
                            dict(
                                name="test_tcp_range_obj",
                                service=dict(
                                    destination_port=dict(
                                        range=dict(
                                            end="https",
                                            start="www",
                                        ),
                                    ),
                                    protocol="tcp",
                                ),
                            ),
                            dict(
                                name="test_tcp_source_eq_obj",
                                service=dict(
                                    protocol="tcp",
                                    source_port=dict(
                                        eq="5671",
                                    ),
                                ),
                            ),
                            dict(
                                name="test_tcp_source_range_obj",
                                service=dict(
                                    protocol="tcp",
                                    source_port=dict(
                                        range=dict(
                                            end="5672",
                                            start="5671",
                                        ),
                                    ),
                                ),
                            ),
                        ],
                    ),
                ],
                state="overridden",
            )
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_objects_delete_by_name(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_type="network",
                        objects=[
                            dict(name="test_range_obj"),
                            dict(name="test_non_existent_obj"),
                        ],
                    ),
                    dict(
                        object_type="service",
                        objects=[
                            dict(name="test_icmp_echo_obj",),
                        ],
                    ),
                ],
                state="deleted",
            ),
        )
        result = self.execute_module(changed=True)
        commands = [
            "no object network test_range_obj",
            "no object service test_icmp_echo_obj",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_objects_deleted_all(self):
        set_module_args(dict(state="deleted"))
        result = self.execute_module(changed=True)
        commands = [
            "no object network test_fqdn_obj",
            "no object network test_host_obj",
            "no object network test_nat_obj",
            "no object network test_range_obj",
            "no object network test_subnet_obj",
            "no object service test_gre_obj",
            "no object service test_icmp_echo_obj",
            "no object service test_icmp_echo_repl_code_obj",
            "no object service test_tcp_eq_obj",
            "no object service test_tcp_range_obj",
            "no object service test_tcp_source_eq_obj",
            "no object service test_tcp_source_range_obj",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_asa_objects_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        object_type="network",
                        objects=[
                            dict(
                                description="a test fqdn object",
                                fqdn="google.com",
                                name="test_fqdn_obj",
                            ),
                            dict(
                                description="a test host object",
                                host="1.2.3.4",
                                name="test_host_obj",
                            ),
                            dict(
                                description="a test nat object",
                                host="1.2.3.4",
                                name="test_nat_obj",
                                nat=dict(
                                    mapped_if="any",
                                    real_if="any",
                                    static=dict(
                                        name="5.6.7.8",
                                        net_to_net=True,
                                    ),
                                ),
                            ),
                            dict(
                                description="a test range object",
                                name="test_range_obj",
                                range="10.0.0.1 10.0.0.10",
                            ),
                            dict(
                                description="a test subnet object",
                                name="test_subnet_obj",
                                subnet="10.0.0.0 255.255.255.0",
                            ),
                        ],
                    ),
                    dict(
                        object_type="service",
                        objects=[
                            dict(
                                name="test_gre_obj",
                                service=dict(
                                    protocol="gre",
                                ),
                            ),
                            dict(
                                name="test_icmp_echo_obj",
                                service=dict(
                                    icmpopt=dict(
                                        name="echo",
                                    ),
                                    protocol="icmp",
                                ),
                            ),
                            dict(
                                name="test_icmp_echo_repl_code_obj",
                                service=dict(
                                    icmpopt=dict(
                                        code="0",
                                        name="echo-reply",
                                    ),
                                    protocol="icmp",
                                ),
                            ),
                            dict(
                                name="test_tcp_eq_obj",
                                service=dict(
                                    destination_port=dict(
                                        eq="https",
                                    ),
                                    protocol="tcp",
                                )
                            ),
                            dict(
                                name="test_tcp_range_obj",
                                service=dict(
                                    destination_port=dict(
                                        range=dict(
                                            end="https",
                                            start="www",
                                        ),
                                    ),
                                    protocol="tcp",
                                ),
                            ),
                            dict(
                                name="test_tcp_source_eq_obj",
                                service=dict(
                                    protocol="tcp",
                                    source_port=dict(
                                        eq="5671",
                                    ),
                                ),
                            ),
                            dict(
                                name="test_tcp_source_range_obj",
                                service=dict(
                                    protocol="tcp",
                                    source_port=dict(
                                        range=dict(
                                            end="5672",
                                            start="5671",
                                        ),
                                    ),
                                ),
                            ),
                        ],
                    ),
                ],
                state="rendered",
            )
        )
        commands = [
            "object network test_fqdn_obj",
            "description a test fqdn object",
            "fqdn google.com",
            "object network test_host_obj",
            "description a test host object",
            "host 1.2.3.4",
            "object network test_nat_obj",
            "description a test nat object",
            "host 1.2.3.4",
            "nat (any,any) static 5.6.7.8 net-to-net",
            "object network test_range_obj",
            "description a test range object",
            "range 10.0.0.1 10.0.0.10",
            "object network test_subnet_obj",
            "description a test subnet object",
            "subnet 10.0.0.0 255.255.255.0",
            "object service test_gre_obj",
            "service gre",
            "object service test_icmp_echo_obj",
            "service icmp echo",
            "object service test_icmp_echo_repl_code_obj",
            "service icmp echo-reply 0",
            "object service test_tcp_eq_obj",
            "service tcp destination eq https",
            "object service test_tcp_range_obj",
            "service tcp destination range www https",
            "object service test_tcp_source_eq_obj",
            "service tcp source eq 5671",
            "object service test_tcp_source_range_obj",
            "service tcp source range 5671 5672",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))
