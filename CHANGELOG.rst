==================================
Cisco Asa Collection Release Notes
==================================

.. contents:: Topics

v6.1.0
======

Minor Changes
-------------

- cisco.asa.asa - add support to fetch hardware specific information in facts
- cisco.asa.asa_acls - add support for specifying object-group as protocol

Bugfixes
--------

- cisco.asa - fixed Cliconf.edit_config() got an unexpected keyword argument 'candidate' error
- cisco.asa.asa_acls - fixed ace parsing when source is object-group and its name contains dots
- cisco.asa.asa_acls - fixed acl modification commands order if object/group name contains `no`

Documentation Changes
---------------------

- Includes a new support related section in the README.

v6.0.0
======

Release Summary
---------------

With this release, the minimum required version of `ansible-core` for this collection is `2.15.0`. The last version known to be compatible with `ansible-core` versions below `2.15` is v5.0.1.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

v5.0.1
======

Bugfixes
--------

- Prevents module_defaults from were being incorrectly applied to the platform action, instead of the concerned module.

v5.0.0
======

Release Summary
---------------

Starting from this release, the minimum `ansible-core` version this collection requires is `2.14.0`. The last known version compatible with ansible-core<2.14 is `v4.0.3`.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

v4.0.3
======

Release Summary
---------------

Release with updated workflow and lint fixes.

v4.0.2
======

Documentation Changes
---------------------

- Replace all references to non-example address ranges in module documentation and tests.

v4.0.1
======

Release Summary
---------------

Release with bugfix fixing the import path coming from utils and netcommon lib.

v4.0.0
======

Major Changes
-------------

- Please use either of the following connection types - network_cli, httpapi or netconf.
- This includes the following modules:
- This release drops support for `connection: local` and provider dictionary.
- This release removes all deprecated plugins that have reached their end-of-life.
- Use of connection: local and the provider option are no longer valid on any modules in this collection.
- asa_acl
- asa_og

v3.1.0
======

Release Summary
---------------

Releasing 3.1.0 with bugfix.

Bugfixes
--------

- Fix service-object port range rendering
- Fixes asa_ogs port object range issue and duplicate service cmd (https://github.com/ansible-collections/cisco.asa/issues/165, https://github.com/ansible-collections/cisco.asa/issues/166).
- Unit TC for svc src/dst port range

v3.0.0
======

Major Changes
-------------

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.

Bugfixes
--------

- Fixes asa_ogs services object and port object issue ((https://github.com/ansible-collections/cisco.asa/issues/152).

v2.1.0
======

Release Summary
---------------

Releasing 2.1.0 with updated readme with changelog link, minor change, and bugfix.

Minor Changes
-------------

- Fixes asa_ogs service object where complete params were not supported and added with the PR ((https://github.com/ansible-collections/cisco.asa/issues/100).

Bugfixes
--------

- Fixes asa_acls to add the support for service object group under destination option ((https://github.com/ansible-collections/cisco.asa/issues/100).

v2.0.3
======

Bugfixes
--------

- Fix TypeError argument of type 'NoneType' is not iterable in service-group when service-group does not exists.
- Fixes asa_ogs protocol object to except protocol number as input (https://github.com/ansible-collections/cisco.asa/issues/116).
- Fixes description for "passwords" parameter in documentation (https://github.com/ansible-collections/cisco.asa/issues/132).
- Implement the replace block mode that is described in the docs for asa_acl (https://github.com/ansible-collections/cisco.asa/issues/97).
- To fix asa_acls port range implementation, (https://github.com/ansible-collections/cisco.asa/issues/120, https://github.com/ansible-collections/cisco.asa/issues/121, https://github.com/ansible-collections/cisco.asa/issues/122).
- To fix asa_ogs for empty object traceback failure, (https://github.com/ansible-collections/cisco.asa/issues/124).
- To fix asa_ogs for parsing network object with ipv6 host address as expected (https://github.com/ansible-collections/cisco.asa/issues/128).

v2.0.2
======

Bugfixes
--------

- To fix Cisco ASA network_object object config which wasn't working as expected.
- To fix asa_acls where ipv6 with host wasn't getting rendered as expected and facts was skipping.

v2.0.1
======

Minor Changes
-------------

- Add ignore-2.12.txt (https://github.com/ansible-collections/cisco.asa/pull/102).
- Remove tests/sanity/requirements.txt (https://github.com/ansible-collections/cisco.asa/pull/94).

Bugfixes
--------

- Added save_when param support in asa_config module (https://github.com/ansible-collections/cisco.asa/pull/75).
- To fix Cisco ASA network_object object config which wasn't working as expected (https://github.com/ansible-collections/cisco.asa/pull/103).

v2.0.0
======

Major Changes
-------------

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>` for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

Minor Changes
-------------

- Adds support for single_user_mode command output caching. (https://github.com/ansible-collections/cisco.ios/pull/204).

Bugfixes
--------

- To fix ASA acls module where replace wasn't working as expected (https://github.com/ansible-collections/cisco.asa/pull/92).

v1.0.4
======

Bugfixes
--------

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- To fix ASA OGs module where delete by name was not resulting to an expected behaviour (https://github.com/ansible-collections/cisco.asa/pull/77).
- Update asa acls RM to use newer RM design approach and addeed support for any4/any6 feature (https://github.com/ansible-collections/cisco.asa/pull/64).

v1.0.3
======

Bugfixes
--------

- Unexpected set of CMDs fired when source and destination were both set to hosts acl (https://github.com/ansible-collections/cisco.asa/pull/69).

v1.0.2
======

Release Summary
---------------

Re-releasing 1.0.1 with updated changelog.

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

- asa_acls - Access-Lists resource module
- asa_command - Run arbitrary commands on Cisco ASA devices
- asa_config - Manage configuration sections on Cisco ASA devices
- asa_facts - Collect facts from remote devices running Cisco ASA
- asa_ogs - Object Group resource module
