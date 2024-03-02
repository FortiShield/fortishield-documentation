.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.5.2 has been released. Check out our release notes to discover the changes and additions of this release.

4.5.2 Release notes - 6 September 2023
======================================

This section lists the changes in version 4.5.2. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This version includes new features or improvements, such as the following:

Manager
^^^^^^^

-  `#18085 <https://github.com/fortishield/fortishield/pull/18085>`__ ``fortishield-remoted`` now allows connection overtaking if the older agent doesn't respond for a while.
-  `#18468 <https://github.com/fortishield/fortishield/pull/18468>`__ ``fortishield-remoted`` now prints the connection family when an unknown client gets connected.
-  `#18437 <https://github.com/fortishield/fortishield/pull/18437>`__ The manager stops restricting the possible package formats in the inventory, to increase compatibility.
-  `#18545 <https://github.com/fortishield/fortishield/pull/18545>`__ The manager stops blocking updates by WPK to macOS agents on ARM64, allowing custom updates.
-  `#18770 <https://github.com/fortishield/fortishield/pull/18770>`__ Vulnerability Detector now fetches the Debian feeds in BZ2 compressed format.

Packages
^^^^^^^^

-  `#2337 <https://github.com/fortishield/fortishield-packages/pull/2337>`__ Provided port number option to ``fortishield-install.sh`` script.

Resolved issues
---------------

This release resolves known issues as the following: 

Manager
^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#18472 <https://github.com/fortishield/fortishield/pull/18472>`__            Fixed a bug in ``fortishield-csyslogd`` that causes it to consume 100% of CPU while expecting new alerts.
==============================================================    =============

Fortishield dashboard
^^^^^^^^^^^^^^^

===============================================================    =============
Reference                                                          Description
===============================================================    =============
`#5764 <https://github.com/fortishield/fortishield-kibana-app/pull/5764>`__    Fixed an error with the commands in **Deploy new agent** for **Oracle Linux 6+** agents.
`#5796 <https://github.com/fortishield/fortishield-kibana-app/pull/5796>`__    Fixed broken documentation links in **Management** > **Configuration**.
===============================================================    =============

Fortishield Kibana plugin for Kibana 7.10.2, 7.16.x, and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===============================================================    =============
Reference                                                          Description
===============================================================    =============
`#5764 <https://github.com/fortishield/fortishield-kibana-app/pull/5764>`__    Fixed an error with the commands in **Deploy new agent** for **Oracle Linux 6+** agents.
`#5796 <https://github.com/fortishield/fortishield-kibana-app/pull/5796>`__    Fixed broken documentation links in **Management** > **Configuration**.
===============================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

-  `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.5.2/CHANGELOG.md>`_
-  `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-kibana-app/blob/v4.5.2-2.6.0/CHANGELOG.md>`_
-  `fortishield/fortishield-kibana-app 7.10.2 <https://github.com/fortishield/fortishield-kibana-app/blob/v4.5.2-7.10.2/CHANGELOG.md>`_
-  `fortishield/fortishield-kibana-app 7.16.x <https://github.com/fortishield/fortishield-kibana-app/blob/v4.5.2-7.16.3/CHANGELOG.md>`_
-  `fortishield/fortishield-kibana-app 7.17.x <https://github.com/fortishield/fortishield-kibana-app/blob/v4.5.2-7.17.12/CHANGELOG.md>`_
-  `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.5.2-8.2/CHANGELOG.md>`_
-  `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.5.2>`_