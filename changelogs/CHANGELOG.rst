==================================
Cisco Asa Collection Release Notes
==================================

.. contents:: Topics

v1.0.2
======

Release Summary
---------------

- Re-releasing 1.0.2 with updated changelog.

v1.0.1
======

Minor Changes
-------------

- Add changelogs for 1.0.0 release (https://github.com/ansible-collections/cisco.asa/pull/48)
- Removes Cisco ASA sanity ignores and sync for argspec and docstring (https://github.com/ansible-collections/cisco.asa/pull/59).
- Updated docs.

Bugfixes
--------

- Make `src`, `backup` and `backup_options` in asa_config work when module alias is used (https://github.com/ansible-collections/cisco.asa/pull/61).

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- asa - Use asa cliconf to run command on Cisco ASA platform

New Modules
-----------

- asa_acl - (deprecated, removed after 2022-06-01) Manage access-lists on a Cisco ASA
- asa_acls - Access-Lists resource module
- asa_command - Run arbitrary commands on Cisco ASA devices
- asa_config - Manage configuration sections on Cisco ASA devices
- asa_facts - Collect facts from remote devices running Cisco ASA
- asa_og - (deprecated, removed after 2022-06-01) Manage object groups on a Cisco ASA
- asa_ogs - Object Group resource module
