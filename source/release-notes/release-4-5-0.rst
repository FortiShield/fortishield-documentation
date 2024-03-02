.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.5.0 has been released. Check out our release notes to discover the changes and additions of this release.

4.5.0 Release notes - 10 August 2023
====================================

This section lists the changes in version 4.5.0. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This version includes new features or improvements, such as the following:

Manager
^^^^^^^

- `#17954 <https://github.com/fortishield/fortishield/pull/17954>`_ Vulnerability Detector now fetches the NVD feed from `https://feed.fortishield.com`, based on the NVD API 2.0.

   - The ``<update_from_year>`` option has been deprecated.

RESTful API
^^^^^^^^^^^

- `#17703 <https://github.com/fortishield/fortishield/pull/17703>`_ Modified the API integration tests to include Nginx LB logs in case of test failures.

Resolved issues
---------------

This release resolves known issues as the following: 

Manager
^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#17656 <https://github.com/fortishield/fortishield/pull/17656>`_             Fixed an error in the installation commands of the API and Framework modules when upgrading from sources.
`#18123 <https://github.com/fortishield/fortishield/issues/18123>`_           Fixed embedded Python interpreter to remove old Fortishield packages from it.
==============================================================    =============

RESTful API
^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#17703 <https://github.com/fortishield/fortishield/pull/17703>`_             Fixed an error in the Nginx LB entrypoint of the API integration tests.
==============================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.5.0/CHANGELOG.md>`_
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-kibana-app/blob/v4.5.0-2.6.0/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.10.2 <https://github.com/fortishield/fortishield-kibana-app/blob/v4.5.0-7.10.2/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.17.x <https://github.com/fortishield/fortishield-kibana-app/blob/v4.5.0-7.17.9/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.5.0-8.2/CHANGELOG.md>`_
- `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.5.0>`_