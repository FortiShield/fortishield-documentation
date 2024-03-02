.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.4.1 has been released. Check out our release notes to discover the changes and additions of this release.

4.4.1 Release notes - 12 April 2023
===================================

This section lists the changes in version 4.4.1. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Fortishield manager
^^^^^^^^^^^^^
- `#15883 <https://github.com/fortishield/fortishield/pull/15883>`_ Improved ``FortishieldDB`` performance by avoiding synchronizing existing agent keys and removing deprecated agent databases from ``var/db/agents``.

RESTful API
^^^^^^^^^^^
- `#16541 <https://github.com/fortishield/fortishield/pull/16541>`_ Changed API limits protection to allow uploading new configuration files if ``limit`` is not modified.

Ruleset
^^^^^^^
- `#16017 <https://github.com/fortishield/fortishield/pull/16017>`_ Added Debian Linux 11 SCA policy.
- `#16016 <https://github.com/fortishield/fortishield/pull/16016>`_ SCA policy for Red Hat Enterprise Linux 9 rework.

Other
^^^^^
- `#16472 <https://github.com/fortishield/fortishield/pull/16472>`_ Updated embedded Python interpreter to 3.9.16. 
- `#16492 <https://github.com/fortishield/fortishield/pull/16492>`_ Updated ``setuptools`` to 65.5.1.

Packages
^^^^^^^^
- `#2150 <https://github.com/fortishield/fortishield-packages/pull/2150>`_ The Fortishield dashboard is now based on OpenSearch dashboards 2.6.0.
- `#2150 <https://github.com/fortishield/fortishield-packages/pull/2150>`_ The Fortishield indexer is now based on OpenSearch 2.6.0.
- `#2147 <https://github.com/fortishield/fortishield-packages/pull/2147>`_ Added Debian 11 SCA files to specs.

Resolved issues
---------------

This release resolves known issues as the following: 

Fortishield manager
^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#16546 <https://github.com/fortishield/fortishield/pull/16546>`_             Reverted the addition of some mapping fields in the Fortishield template, causing a bug with expanded search.
==============================================================    =============

Fortishield dashboard
^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#5196 <https://github.com/fortishield/fortishield-kibana-app/pull/5196>`_    Fixed the search in the agent inventory data tables.
`#5334 <https://github.com/fortishield/fortishield-kibana-app/pull/5334>`_    Fixed the `Top 5 users` table overflow in the FIM dashboard.
`#5337 <https://github.com/fortishield/fortishield-kibana-app/pull/5337>`_    Fixed a visual error in the **About** section.
`#5329 <https://github.com/fortishield/fortishield-kibana-app/pull/5329>`_    Fixed the Anomaly and malware detection link.
`#5341 <https://github.com/fortishield/fortishield-kibana-app/pull/5341>`_    Fixed an issue that did not allow closing the time picker when pressing the button multiple times in **Agents** and **Management/Statistics**.
==============================================================    =============

Fortishield Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#5196 <https://github.com/fortishield/fortishield-kibana-app/pull/5196>`_    Fixed the search in the agent inventory data tables.
`#5329 <https://github.com/fortishield/fortishield-kibana-app/pull/5329>`_    Fixed the Anomaly and malware detection link.
`#5341 <https://github.com/fortishield/fortishield-kibana-app/pull/5341>`_    Fixed an issue that did not allow closing the time picker when pressing the button multiple times in **Agents** and **Management/Statistics**.
==============================================================    =============

Fortishield Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#5196 <https://github.com/fortishield/fortishield-kibana-app/pull/5196>`_    Fixed the search in the agent inventory data tables.
`#5329 <https://github.com/fortishield/fortishield-kibana-app/pull/5329>`_    Fixed the Anomaly and malware detection link.
`#5341 <https://github.com/fortishield/fortishield-kibana-app/pull/5341>`_    Fixed an issue that did not allow closing the time picker when pressing the button multiple times in **Agents** and **Management/Statistics**.
==============================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.4.1/CHANGELOG.md>`_
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-kibana-app/blob/v4.4.1-2.6.0/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.10.2 <https://github.com/fortishield/fortishield-kibana-app/blob/v4.4.1-7.10.2/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.17.x <https://github.com/fortishield/fortishield-kibana-app/blob/v4.4.1-7.17.9/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.4.1-8.2/CHANGELOG.md>`_
- `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.4.1>`_
