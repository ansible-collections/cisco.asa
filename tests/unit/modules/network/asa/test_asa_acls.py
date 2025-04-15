#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent
from unittest.mock import patch

from ansible_collections.cisco.asa.plugins.modules import asa_acls
from ansible_collections.cisco.asa.tests.unit.modules.utils import set_module_args

from .asa_module import TestAsaModule


class TestAsaAclsModule(TestAsaModule):
    module = asa_acls

    def setUp(self):
        super(TestAsaAclsModule, self).setUp()

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
            "ansible_collections.cisco.asa.plugins.module_utils.network.asa.facts.acls.acls."
            "AclsFacts.get_acls_config",
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

    def test_asa_acls_merged(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                config=dict(
                    acls=[
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        object_group="test_network_og",
                                        port_protocol=dict(eq="www"),
                                    ),
                                    grant="deny",
                                    line=2,
                                    log="default",
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        object_group="test_og_network",
                                    ),
                                ),
                            ],
                            acl_type="extended",
                            name="test_global_access",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        any="true",
                                        service_object_group="O-UNIX-TCP",
                                    ),
                                    grant="permit",
                                    line=2,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(object_group="O-Environments"),
                                ),
                            ],
                            acl_type="extended",
                            name="MyACL",
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        result = self.execute_module(changed=True)
        commands = [
            "access-list test_global_access line 2 extended deny tcp object-group test_og_network object-group test_network_og eq www log default",
            "access-list MyACL line 2 extended permit tcp object-group O-Environments any object-group O-UNIX-TCP",
        ]
        self.assertEqual(result["commands"], commands)

    def test_asa_acls_merged_idempotent(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                config=dict(
                    acls=[
                        dict(
                            aces=[
                                dict(line=1, remark="HostA"),
                                dict(
                                    destination=dict(any4=True),
                                    grant="deny",
                                    line=2,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(host="192.0.5.1"),
                                ),
                            ],
                            acl_type="extended",
                            name="ansible_test",
                        ),
                        dict(
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
                                ),
                                dict(line=2, remark="test global remark"),
                            ],
                            acl_type="extended",
                            name="test_global_access",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.100.0",
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
                                        address="198.51.110.0",
                                        netmask="255.255.255.0",
                                    ),
                                    grant="deny",
                                    line=2,
                                    log="errors",
                                    protocol="igrp",
                                    protocol_options=dict(igrp="true"),
                                    source=dict(
                                        address="198.51.100.0",
                                        netmask="255.255.255.0",
                                    ),
                                ),
                                dict(
                                    destination=dict(any="true"),
                                    grant="permit",
                                    line=3,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(host="192.0.2.2"),
                                ),
                            ],
                            acl_type="extended",
                            name="test_access",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.100.0",
                                        netmask="255.255.255.0",
                                        port_protocol=dict(eq="100"),
                                    ),
                                    grant="permit",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        host="198.51.100.5",
                                        port_protocol=dict(
                                            range=dict(end=65535, start=49152),
                                        ),
                                    ),
                                ),
                                dict(
                                    destination=dict(
                                        object_group="ALLSERV.12",
                                        port_protocol=dict(eq="9389"),
                                    ),
                                    grant="permit",
                                    line=2,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        address="198.51.101.0",
                                        netmask="255.255.255.0",
                                    ),
                                ),
                                dict(
                                    destination=dict(host="192.0.2.1"),
                                    grant="permit",
                                    line=3,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(any4=True),
                                ),
                            ],
                            acl_type="extended",
                            name="management_in",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        any="true",
                                        service_object_group="O-Windows-TCP",
                                    ),
                                    grant="permit",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(object_group="O-Environments"),
                                ),
                            ],
                            acl_type="extended",
                            name="MyACL",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="2001:fc8:0:4::/64",
                                        port_protocol=dict(eq="telnet"),
                                    ),
                                    grant="deny",
                                    inactive="true",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        address="2001:db8:0:3::/64",
                                        port_protocol=dict(eq="www"),
                                    ),
                                ),
                                dict(
                                    destination=dict(any6=True),
                                    grant="permit",
                                    line=2,
                                    protocol="ip",
                                    protocol_options=dict(ip=True),
                                    source=dict(host="2001:db8::1"),
                                ),
                            ],
                            acl_type="extended",
                            name="test_R1_traffic",
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_acls_replaced(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                config=dict(
                    acls=[
                        dict(
                            name="test_access",
                            acl_type="extended",
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.102.0",
                                        netmask="255.255.255.0",
                                    ),
                                    grant="deny",
                                    line=1,
                                    log="default",
                                    protocol="igrp",
                                    protocol_options=dict(igrp="true"),
                                    source=dict(
                                        address="198.51.101.0",
                                        netmask="255.255.255.0",
                                    ),
                                    time_range="temp",
                                ),
                            ],
                        ),
                        dict(
                            aces=[
                                dict(line=1, remark="HostA0"),
                                dict(
                                    destination=dict(any4=True),
                                    grant="deny",
                                    line=2,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(host="192.0.5.1"),
                                ),
                            ],
                            acl_type="extended",
                            name="ansible_test",
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        result = self.execute_module(changed=True)
        commands = [
            "no access-list ansible_test line 1 remark HostA",
            "no access-list test_access line 3 extended permit ip host 192.0.2.2 any",
            "no access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors",
            "no access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default",
            "access-list test_access line 1 extended deny igrp 198.51.101.0 255.255.255.0 198.51.102.0 255.255.255.0 log default time-range temp",
            "access-list ansible_test line 1 remark HostA0",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_asa_acls_replaced_idempotent(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                config=dict(
                    acls=[
                        dict(
                            aces=[
                                dict(line=1, remark="HostA"),
                                dict(
                                    destination=dict(any4=True),
                                    grant="deny",
                                    line=2,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(host="192.0.5.1"),
                                ),
                            ],
                            acl_type="extended",
                            name="ansible_test",
                        ),
                        dict(
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
                                ),
                                dict(line=2, remark="test global remark"),
                            ],
                            acl_type="extended",
                            name="test_global_access",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.100.0",
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
                                        address="198.51.110.0",
                                        netmask="255.255.255.0",
                                    ),
                                    grant="deny",
                                    line=2,
                                    log="errors",
                                    protocol="igrp",
                                    protocol_options=dict(igrp="true"),
                                    source=dict(
                                        address="198.51.100.0",
                                        netmask="255.255.255.0",
                                    ),
                                ),
                                dict(
                                    destination=dict(any="true"),
                                    grant="permit",
                                    line=3,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(host="192.0.2.2"),
                                ),
                            ],
                            acl_type="extended",
                            name="test_access",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.100.0",
                                        netmask="255.255.255.0",
                                        port_protocol=dict(eq="100"),
                                    ),
                                    grant="permit",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        host="198.51.100.5",
                                        port_protocol=dict(
                                            range=dict(end=65535, start=49152),
                                        ),
                                    ),
                                ),
                                dict(
                                    destination=dict(
                                        object_group="ALLSERV.12",
                                        port_protocol=dict(eq="9389"),
                                    ),
                                    grant="permit",
                                    line=2,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        address="198.51.101.0",
                                        netmask="255.255.255.0",
                                    ),
                                ),
                                dict(
                                    destination=dict(host="192.0.2.1"),
                                    grant="permit",
                                    line=3,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(any4=True),
                                ),
                            ],
                            acl_type="extended",
                            name="management_in",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        any="true",
                                        service_object_group="O-Windows-TCP",
                                    ),
                                    grant="permit",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(object_group="O-Environments"),
                                ),
                            ],
                            acl_type="extended",
                            name="MyACL",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="2001:fc8:0:4::/64",
                                        port_protocol=dict(eq="telnet"),
                                    ),
                                    grant="deny",
                                    inactive="true",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        address="2001:db8:0:3::/64",
                                        port_protocol=dict(eq="www"),
                                    ),
                                ),
                                dict(
                                    destination=dict(any6=True),
                                    grant="permit",
                                    line=2,
                                    protocol="ip",
                                    protocol_options=dict(ip=True),
                                    source=dict(host="2001:db8::1"),
                                ),
                            ],
                            acl_type="extended",
                            name="test_R1_traffic",
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_acls_overridden(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                config=dict(
                    acls=[
                        dict(
                            name="test_global_access",
                            acl_type="extended",
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.110.0",
                                        netmask="255.255.255.0",
                                        port_protocol=dict(eq="www"),
                                    ),
                                    grant="deny",
                                    line=1,
                                    log="errors",
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        address="198.51.100.0",
                                        netmask="255.255.255.0",
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
                state="overridden",
            ),
        )
        result = self.execute_module(changed=True)
        commands = [
            "no access-list test_global_access line 2 remark test global remark",
            "no access-list test_global_access line 1 extended deny tcp any any eq www log errors",
            "no access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4",
            "no access-list ansible_test line 1 remark HostA",
            "no access-list test_access line 3 extended permit ip host 192.0.2.2 any",
            "no access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors",
            "no access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default",
            "no access-list management_in line 3 extended permit ip any4 host 192.0.2.1",
            "no access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389",
            "no access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100",
            "no access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP",
            "no access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6",
            "no access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive",
            "access-list test_global_access line 1 extended deny tcp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 eq www log errors",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_asa_acls_overridden_idempotent(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                config=dict(
                    acls=[
                        dict(
                            aces=[
                                dict(line=1, remark="HostA"),
                                dict(
                                    destination=dict(any4=True),
                                    grant="deny",
                                    line=2,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(host="192.0.5.1"),
                                ),
                            ],
                            acl_type="extended",
                            name="ansible_test",
                        ),
                        dict(
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
                                ),
                                dict(line=2, remark="test global remark"),
                            ],
                            acl_type="extended",
                            name="test_global_access",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.100.0",
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
                                        address="198.51.110.0",
                                        netmask="255.255.255.0",
                                    ),
                                    grant="deny",
                                    line=2,
                                    log="errors",
                                    protocol="igrp",
                                    protocol_options=dict(igrp="true"),
                                    source=dict(
                                        address="198.51.100.0",
                                        netmask="255.255.255.0",
                                    ),
                                ),
                                dict(
                                    destination=dict(any="true"),
                                    grant="permit",
                                    line=3,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(host="192.0.2.2"),
                                ),
                            ],
                            acl_type="extended",
                            name="test_access",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.100.0",
                                        netmask="255.255.255.0",
                                        port_protocol=dict(eq="100"),
                                    ),
                                    grant="permit",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        host="198.51.100.5",
                                        port_protocol=dict(
                                            range=dict(end=65535, start=49152),
                                        ),
                                    ),
                                ),
                                dict(
                                    destination=dict(
                                        object_group="ALLSERV.12",
                                        port_protocol=dict(eq="9389"),
                                    ),
                                    grant="permit",
                                    line=2,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        address="198.51.101.0",
                                        netmask="255.255.255.0",
                                    ),
                                ),
                                dict(
                                    destination=dict(host="192.0.2.1"),
                                    grant="permit",
                                    line=3,
                                    protocol="ip",
                                    protocol_options=dict(ip="true"),
                                    source=dict(any4=True),
                                ),
                            ],
                            acl_type="extended",
                            name="management_in",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        any="true",
                                        service_object_group="O-Windows-TCP",
                                    ),
                                    grant="permit",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(object_group="O-Environments"),
                                ),
                            ],
                            acl_type="extended",
                            name="MyACL",
                        ),
                        dict(
                            aces=[
                                dict(
                                    destination=dict(
                                        address="2001:fc8:0:4::/64",
                                        port_protocol=dict(eq="telnet"),
                                    ),
                                    grant="deny",
                                    inactive="true",
                                    line=1,
                                    protocol="tcp",
                                    protocol_options=dict(tcp="true"),
                                    source=dict(
                                        address="2001:db8:0:3::/64",
                                        port_protocol=dict(eq="www"),
                                    ),
                                ),
                                dict(
                                    destination=dict(any6=True),
                                    grant="permit",
                                    line=2,
                                    protocol="ip",
                                    protocol_options=dict(ip=True),
                                    source=dict(host="2001:db8::1"),
                                ),
                            ],
                            acl_type="extended",
                            name="test_R1_traffic",
                        ),
                    ],
                ),
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[], sort=True)

    def test_asa_acls_delete_by_acl(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                config=dict(
                    acls=[
                        dict(name="test_global_access"),
                        dict(name="test_R1_traffic"),
                    ],
                ),
                state="deleted",
            ),
        )
        result = self.execute_module(changed=True)
        commands = [
            "no access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6",
            "no access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive",
            "no access-list test_global_access line 2 remark test global remark",
            "no access-list test_global_access line 1 extended deny tcp any any eq www log errors",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_asa_acls_deleted_all(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(dict(state="deleted"))
        result = self.execute_module(changed=True)
        commands = [
            "no access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6",
            "no access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive",
            "no access-list test_access line 3 extended permit ip host 192.0.2.2 any",
            "no access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors",
            "no access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default",
            "no access-list management_in line 3 extended permit ip any4 host 192.0.2.1",
            "no access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389",
            "no access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100",
            "no access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP",
            "no access-list test_global_access line 2 remark test global remark",
            "no access-list test_global_access line 1 extended deny tcp any any eq www log errors",
            "no access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4",
            "no access-list ansible_test line 1 remark HostA",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_asa_acls_rendered(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                config=dict(
                    acls=[
                        dict(
                            name="test_access",
                            acl_type="extended",
                            aces=[
                                dict(
                                    destination=dict(
                                        address="198.51.100.0",
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
                                ),
                            ],
                        ),
                    ],
                ),
                state="rendered",
            ),
        )
        commands = [
            "access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 log default",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(result["rendered"], commands)

    def test_asa_acls_gathered(self):
        self.execute_show_command.return_value = dedent(
            """\
            access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
                        alert-interval 300
            access-list test_global_access; 1 elements; name hash: 0xaa83124c
            access-list test_global_access line 1 extended deny tcp any any eq www log errors interval 300 (hitcnt=0) 0x849e9e8f
            access-list test_global_access line 2 remark test global remark
            access-list test_access; 2 elements; name hash: 0x96b5d78b
            access-list test_access line 1 extended deny tcp 192.0.2.0 255.255.255.0 198.51.100.0 255.255.255.0 eq www log default (hitcnt=0) 0xdc46eb6e
            access-list test_access line 2 extended deny igrp 198.51.100.0 255.255.255.0 198.51.110.0 255.255.255.0 log errors interval 300 (hitcnt=0) 0x831d8
            access-list test_access line 3 extended permit ip host 192.0.2.2 any interval 300 (hitcnt=0) 0x831d897d
            access-list test_R1_traffic; 1 elements; name hash: 0x2c20a0c
            access-list test_R1_traffic line 1 extended deny tcp 2001:db8:0:3::/64 eq www 2001:fc8:0:4::/64 eq telnet inactive (hitcnt=0) (inactive) 0x11821a52
            access-list test_R1_traffic line 2 extended permit ip host 2001:db8::1 any6 (hitcnt=0) 0x82a59c34
            access-list ansible_test; 1 elements; name hash: 0x1b2b1138
            access-list ansible_test line 1 remark HostA
            access-list ansible_test line 2 extended deny ip host 192.0.5.1 any4
            access-list management_in; 2 elements; name hash: 0x4acd1688
            access-list management_in line 1 extended permit tcp host 198.51.100.5 range 49152 65535 198.51.100.0 255.255.255.0 eq 100 (hitcnt=0) 0x53ec762f
            access-list management_in line 2 extended permit object-group MYSERV.11 object-group ALLSERV.12 eq 9389 (hitcnt=0) 0xc8881c8c
              access-list management_in line 2 extended permit tcp 198.51.101.0 255.255.255.0 1.1.1.1 1.1.1.1 eq 9389 (hitcnt=0) 0xd39d4f42
            access-list management_in line 3 extended permit ip any4 host 192.0.2.1
            access-list MyACL; 10 elements; name hash: 0x436611e8
            access-list MyACL line 1 extended permit tcp object-group O-Environments any object-group O-Windows-TCP (hitcnt=0) 0x61fe98bb
              access-list MyACL line 1 extended permit tcp 10.20.30.0 255.255.255.0 any eq 3389 (hitcnt=0) 0x69856097
              access-list MyACL line 1 extended permit tcp 10.20.31.0 255.255.255.0 any eq 3389 (hitcnt=0) 0xca48629c
            """,
        )
        set_module_args(
            dict(
                state="gathered",
            ),
        )
        facts = {
            "acls": [
                {
                    "name": "test_global_access",
                    "acl_type": "extended",
                    "aces": [
                        {
                            "grant": "deny",
                            "line": 1,
                            "protocol": "tcp",
                            "source": {"any": True},
                            "destination": {"any": True, "port_protocol": {"eq": "www"}},
                            "log": "errors",
                            "protocol_options": {"tcp": True},
                        },
                        {"line": 2, "remark": "test global remark"},
                    ],
                },
                {
                    "name": "test_access",
                    "acl_type": "extended",
                    "aces": [
                        {
                            "grant": "deny",
                            "line": 1,
                            "protocol": "tcp",
                            "source": {"address": "192.0.2.0", "netmask": "255.255.255.0"},
                            "destination": {
                                "address": "198.51.100.0",
                                "netmask": "255.255.255.0",
                                "port_protocol": {"eq": "www"},
                            },
                            "log": "default",
                            "protocol_options": {"tcp": True},
                        },
                        {
                            "grant": "deny",
                            "line": 2,
                            "protocol": "igrp",
                            "source": {"address": "198.51.100.0", "netmask": "255.255.255.0"},
                            "destination": {"address": "198.51.110.0", "netmask": "255.255.255.0"},
                            "log": "errors",
                            "protocol_options": {"igrp": True},
                        },
                        {
                            "grant": "permit",
                            "line": 3,
                            "protocol": "ip",
                            "source": {"host": "192.0.2.2"},
                            "destination": {"any": True},
                            "protocol_options": {"ip": True},
                        },
                    ],
                },
                {
                    "name": "test_R1_traffic",
                    "acl_type": "extended",
                    "aces": [
                        {
                            "grant": "deny",
                            "line": 1,
                            "protocol": "tcp",
                            "source": {
                                "address": "2001:db8:0:3::/64",
                                "port_protocol": {"eq": "www"},
                            },
                            "destination": {
                                "address": "2001:fc8:0:4::/64",
                                "port_protocol": {"eq": "telnet"},
                            },
                            "inactive": True,
                            "protocol_options": {"tcp": True},
                        },
                        {
                            "grant": "permit",
                            "line": 2,
                            "protocol": "ip",
                            "source": {"host": "2001:db8::1"},
                            "destination": {"any6": True},
                            "protocol_options": {"ip": True},
                        },
                    ],
                },
                {
                    "name": "ansible_test",
                    "aces": [
                        {"line": 1, "remark": "HostA"},
                        {
                            "grant": "deny",
                            "line": 2,
                            "protocol": "ip",
                            "source": {"host": "192.0.5.1"},
                            "destination": {"any4": True},
                            "protocol_options": {"ip": True},
                        },
                    ],
                    "acl_type": "extended",
                },
                {
                    "name": "management_in",
                    "acl_type": "extended",
                    "aces": [
                        {
                            "grant": "permit",
                            "line": 1,
                            "protocol": "tcp",
                            "source": {
                                "host": "198.51.100.5",
                                "port_protocol": {"range": {"start": 49152, "end": 65535}},
                            },
                            "destination": {
                                "address": "198.51.100.0",
                                "netmask": "255.255.255.0",
                                "port_protocol": {"eq": "100"},
                            },
                            "protocol_options": {"tcp": True},
                        },
                        {
                            "grant": "permit",
                            "line": 2,
                            "protocol": "object-group MYSERV.11",
                            "source": {
                                "object_group": "ALLSERV.12",
                                "port_protocol": {"eq": "9389"},
                            },
                        },
                        {
                            "grant": "permit",
                            "line": 3,
                            "protocol": "ip",
                            "source": {"any4": True},
                            "destination": {"host": "192.0.2.1"},
                            "protocol_options": {"ip": True},
                        },
                    ],
                },
                {
                    "name": "MyACL",
                    "acl_type": "extended",
                    "aces": [
                        {
                            "grant": "permit",
                            "line": 1,
                            "protocol": "tcp",
                            "source": {"object_group": "O-Environments"},
                            "destination": {"any": True, "service_object_group": "O-Windows-TCP"},
                            "protocol_options": {"tcp": True},
                        },
                    ],
                },
            ],
        }
        result = self.execute_module(changed=False)
        self.assertEqual(result["gathered"], facts)
