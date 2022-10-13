# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Copyright: (c) 2016, Peter Sprygada <psprygada@ansible.com>
# Copyright: (c) 2016, Patrick Ogenstad <@ogenstad>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


class ModuleDocFragment(object):

    # Standard files documentation fragment
    DOCUMENTATION = r"""options:
  authorize:
    description:
    - B(Deprecated)
    - 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and
      C(become: yes).'
    - For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).
    - HORIZONTALLINE
    - Instructs the module to enter privileged mode on the remote device before sending
      any commands.  If not specified, the device will attempt to execute all commands
      in non-privileged mode. If the value is not specified in the task, the value
      of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.
    type: bool
  context:
    description:
    - Specifies which context to target if you are running in the ASA in multiple
      context mode. Defaults to the current context you login to.
    type: str
  passwords:
    description:
    - Saves running-config passwords in clear-text when set to True.
      Defaults to False
    type: bool
notes:
- For more information on using Ansible to manage network devices see the :ref:`Ansible
  Network Guide <network_guide>`
"""
