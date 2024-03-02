.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.3.10 has been released. Check out our release notes to discover the changes and additions of this release.

4.3.10 Release notes - 16 November 2022
=======================================

This section lists the changes in version 4.3.10. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

Resolved issues
---------------

This release resolves known issues as the following: 

Fortishield manager
^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#15219 <https://github.com/fortishield/fortishield/pull/15219>`_             The Arch Linux feed URL in Vulnerability Detector is updated.
`#15197 <https://github.com/fortishield/fortishield/pull/15197>`_             A bug in Vulnerability Detector related to the internal database access is fixed.
`#15303 <https://github.com/fortishield/fortishield/pull/15303>`_             A crash hazard in Analysisd when parsing an invalid ``<if_sid>`` value in the ruleset is now fixed.
==============================================================    =============

Fortishield agent
^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#15259 <https://github.com/fortishield/fortishield/pull/15259>`_             The agent upgrade configuration has been restricted to local settings.
`#15262 <https://github.com/fortishield/fortishield/pull/15262>`_             An unwanted Windows agent configuration modification on upgrade is fixed.
==============================================================    =============

Fortishield dashboard
^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4815 <https://github.com/fortishield/fortishield-kibana-app/pull/4815>`_    An issue with logging out from Fortishield when SAML is enabled is now fixed.
==============================================================    =============

Fortishield Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4815 <https://github.com/fortishield/fortishield-kibana-app/pull/4815>`_    An issue with logging out from Fortishield when SAML is enabled is now fixed.
==============================================================    =============

Fortishield Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4815 <https://github.com/fortishield/fortishield-kibana-app/pull/4815>`_    An issue with logging out from Fortishield when SAML is enabled is now fixed.
==============================================================    =============

Packages
^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#1901 <https://github.com/fortishield/fortishield-packages/pull/1901>`__     Improved the ``config.yml`` template to prevent indentation issues.
`#1910 <https://github.com/fortishield/fortishield-packages/pull/1910>`__     Fixed the *clean* function in the WPK generation.
==============================================================    =============


Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.3.10/CHANGELOG.md>`_
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.10-1.2.0/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.10.2 <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.10-7.10.2/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.17.x <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.10-7.17.6/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.3.10-8.2.8/CHANGELOG.md>`_
- `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.3.10>`_
