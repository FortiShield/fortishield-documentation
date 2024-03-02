.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.0.1 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_4_0_1:

4.0.1 Release notes - 11 November 2020
======================================

This section lists the changes in version 4.0.1. More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.0.1/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v4.0.1-7.9.3/CHANGELOG.md>`_
- `fortishield/ruleset <https://github.com/fortishield/fortishield-ruleset/blob/4.0.1/CHANGELOG.md>`_

Fortishield core
----------

Changed
^^^^^^^

**Framework**

- Updated Python cryptography library to version ``3.2.1``.

Fixed
^^^^^

**API**

- Added missing ``agent:group`` resource to the RBAC catalog. This prevented the Fortishield Kibana plugin from obtaining the correct information from the RBAC catalog.
- Changed ``limit`` parameter behavior in ``GET sca/{agent_id}/checks/{policy_id}`` endpoint and fixed some information loss when paginating ``wdb``.
- Fixed an error with ``GET /security/users/me`` when logged in with ``run_as``. This endpoint must return the permissions and information of the user who makes the request. However, when the user was authenticated through ``auth_context``, this endpoint did not return the permissions granted by this method.

**Framework**

- Fixed zip files compression and handling in cluster integrity synchronization.

**Core**

- Fixed version matching when assigning a feed in the Vulnerability Detector.
- Improved permissions on Windows agent. Users with limited privileges will now be unable to read the contents of the Fortishield agent folder.
- Fixed a bug that may lead the agent to crash when reading an invalid Logcollector configuration.

Fortishield Kibana plugin
-------------------

Added
^^^^^

- Support for Fortishield v4.0.1.

Fixed
^^^^^

- Fixed icons that did not align correctly in ``Modules > Events``.
- Fixed statistics visualizations that did not show data.
- Fixed error on loading CSS files.
- Fixed search filter in the search bar in ``Module/SCA`` that was not working.

Fortishield ruleset
-------------

Fixed
^^^^^

- Removed duplicated Windows rules for ``EventChannel``.  These extra rules were preventing certain events from triggering alerts.
