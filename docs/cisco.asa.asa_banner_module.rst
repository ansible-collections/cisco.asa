.. _cisco.asa.asa_banner_module:


********************
cisco.asa.asa_banner
********************

**Module to configure multiline banners.**


Version added: 7.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This will configure the asdm, exec, login and motd banners on remote devices running Cisco ASA. It allows playbooks to add or remove banner text from the active running configuration.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>banner</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>asdm</li>
                                    <li>exec</li>
                                    <li>login</li>
                                    <li>motd</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies which banner should be configured on the remote device.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>context</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies which context to target if you are running in the ASA in multiple context mode. Defaults to the current context you login to.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passwords</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Saves running-config passwords in clear-text when set to True. Defaults to False</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies whether or not the configuration is present in the current devices active running configuration.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The banner text that should be present in the remote device running configuration. Each line of the text becomes a separate <code>banner</code> command, which is how the ASA stores a multiline banner. Requires <em>state=present</em>.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Cisco ASA Version 9.20.
   - This module works with connection ``network_cli``.
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`



Examples
--------

.. code-block:: yaml

    # Using state: present

    # Before state:
    # -------------
    # asa#show running-config banner
    # asa#

    - name: Configure the motd banner
      cisco.asa.asa_banner:
        banner: motd
        text: |
          this is my motd banner
          that has a multiline
          string
        state: present

    # Task Output:
    # ------------
    # commands:
    # - banner motd this is my motd banner
    # - banner motd that has a multiline
    # - banner motd string

    # After state:
    # ------------
    # asa#show running-config banner
    # banner motd this is my motd banner
    # banner motd that has a multiline
    # banner motd string

    # Using state: absent

    # Before state:
    # -------------
    # asa#show running-config banner
    # banner motd this is my motd banner

    - name: Remove the motd banner
      cisco.asa.asa_banner:
        banner: motd
        state: absent

    # Task Output:
    # ------------
    # commands:
    # - no banner motd

    # After state:
    # ------------
    # asa#show running-config banner
    # asa#



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The list of configuration mode commands to send to the device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;banner motd this is my motd banner&#x27;, &#x27;banner motd that has a multiline&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Jørgen Spange (@jorgenspange)
