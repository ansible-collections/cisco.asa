==================================
Cisco Asa Collection Release Notes
==================================

.. contents:: Topics

v1.0.4
======

Release Summary
---------------

- Releasing 1.0.4 with updated readme with changelog link, galaxy description, and bugfix.

Bugfixes
--------

- Update asa acls RM to use newer RM design approach and addeed support for any4/any6 feature (https://github.com/ansible-collections/cisco.asa/pull/64).
- Add version key to galaxy.yaml to work around ansible-galaxy bug
- To fix ASA OGs module where delete by name was not resulting to an expected behaviour (https://github.com/ansible-collections/cisco.asa/pull/77).

v1.0.3
======

Release Summary
---------------

- Releasing 1.0.3 with updated readme with changelog link, galaxy description, and bugfix.

Bugfixes
--------

- Unexpected set of CMDs fired when source and destination were both set to hosts acl. (https://github.com/ansible-collections/cisco.asa/pull/69).

v1.0.2
======

Release Summary
---------------

- Re-releasing 1.0.1 with updated changelog.

v1.0.1
======

Minor Changes
-------------

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
