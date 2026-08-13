#
# (c) 2026, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent
from unittest.mock import patch

from ansible_collections.cisco.asa.plugins.modules import asa_banner
from ansible_collections.cisco.asa.tests.unit.modules.utils import set_module_args

from .asa_module import TestAsaModule


class TestAsaBannerModule(TestAsaModule):
    module = asa_banner

    def setUp(self):
        super(TestAsaBannerModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.cisco.asa.plugins.modules.asa_banner.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.cisco.asa.plugins.modules.asa_banner.load_config",
        )
        self.load_config = self.mock_load_config.start()

    def tearDown(self):
        super(TestAsaBannerModule, self).tearDown()
        self.mock_get_config.stop()
        self.mock_load_config.stop()

    def test_asa_banner_create(self):
        self.get_config.return_value = ""
        set_module_args(
            dict(
                banner="motd",
                text="this is my motd banner\nthat has a multiline\nstring",
            ),
        )
        commands = [
            "banner motd this is my motd banner",
            "banner motd that has a multiline",
            "banner motd string",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_asa_banner_replace(self):
        self.get_config.return_value = dedent(
            """\
            banner motd the old banner
            """,
        )
        set_module_args(dict(banner="motd", text="the new banner"))
        commands = ["no banner motd", "banner motd the new banner"]
        self.execute_module(changed=True, commands=commands)

    def test_asa_banner_idempotent(self):
        self.get_config.return_value = dedent(
            """\
            banner motd this is my motd banner
            banner motd that has a multiline
            banner motd string
            """,
        )
        set_module_args(
            dict(
                banner="motd",
                text="this is my motd banner\nthat has a multiline\nstring",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_asa_banner_repeated_lines_preserved(self):
        """Repeated separator lines are distinct banner commands on ASA."""
        self.get_config.return_value = ""
        set_module_args(dict(banner="motd", text="+---+\ntext\n+---+"))
        commands = [
            "banner motd +---+",
            "banner motd text",
            "banner motd +---+",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_asa_banner_blank_line(self):
        self.get_config.return_value = ""
        set_module_args(dict(banner="login", text="first line\n\nthird line"))
        commands = [
            "banner login first line",
            "banner login",
            "banner login third line",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_asa_banner_blank_line_idempotent(self):
        self.get_config.return_value = dedent(
            """\
            banner login first line
            banner login
            banner login third line
            """,
        )
        set_module_args(dict(banner="login", text="first line\n\nthird line"))
        self.execute_module(changed=False, commands=[])

    def test_asa_banner_delete(self):
        self.get_config.return_value = dedent(
            """\
            banner motd this is my motd banner
            """,
        )
        set_module_args(dict(banner="motd", state="absent"))
        commands = ["no banner motd"]
        self.execute_module(changed=True, commands=commands)

    def test_asa_banner_delete_idempotent(self):
        self.get_config.return_value = ""
        set_module_args(dict(banner="motd", state="absent"))
        self.execute_module(changed=False, commands=[])
