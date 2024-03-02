.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.5.4 has been released. Check out our release notes to discover the changes and additions of this release.

4.5.4 Release notes - 23 October 2023
=====================================

This section lists the changes in version 4.5.4. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.


What's new
----------

This version includes new features or improvements, such as the following:

Manager
^^^^^^^

- `#19729 <https://github.com/fortishield/fortishield/pull/19729>`__ Added a timeout on requests between components through the cluster.


Resolved issues
---------------

This release resolves known issues as the following: 

Manager
^^^^^^^

========================================================    ========================================================================================================
Reference                                                   Description
========================================================    ========================================================================================================
`#19702 <https://github.com/fortishield/fortishield/pull/19702>`__      Fixed a bug that might leave some worker's services hanging if the connection to the master was broken.
`#19706 <https://github.com/fortishield/fortishield/pull/19706>`__      Fixed vulnerability scan on Windows agent when the OS version has no release data. 
========================================================    ========================================================================================================


Changelogs
----------

More details about these changes are provided in the changelog of each component:

-  `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.5.4/CHANGELOG.md>`_
-  `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-dashboard-plugins/blob/v4.5.4-2.6.0/CHANGELOG.md>`_
-  `fortishield/fortishield-dashboard-plugins 7.10.2 <https://github.com/fortishield/fortishield-dashboard-plugins/blob/v4.5.4-7.10.2/CHANGELOG.md>`_
-  `fortishield/fortishield-dashboard-plugins 7.16.x <https://github.com/fortishield/fortishield-dashboard-plugins/blob/v4.5.4-7.16.3/CHANGELOG.md>`_
-  `fortishield/fortishield-dashboard-plugins 7.17.x <https://github.com/fortishield/fortishield-dashboard-plugins/blob/v4.5.4-7.17.13/CHANGELOG.md>`_
-  `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.5.4-8.2/CHANGELOG.md>`_
-  `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.5.4>`_