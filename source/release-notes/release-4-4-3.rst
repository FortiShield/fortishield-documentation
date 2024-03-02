.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.4.3 has been released. Check out our release notes to discover the changes and additions of this release.

4.4.3 Release notes - 25 May 2023
=================================

This section lists the changes in version 4.4.3. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Agent
^^^^^
- `#16521 <https://github.com/fortishield/fortishield/pull/16521>`_ Added support for Apple Silicon processors to the macOS agent.
- `#2211 <https://github.com/fortishield/fortishield-packages/pull/2211>`_ Prevented the installer from checking the old users ``ossecm`` and ``ossecr`` on upgrade.
- `#17195 <https://github.com/fortishield/fortishield/pull/17195>`_ Changed the deployment variables capture on macOS.

Ruleset
^^^^^^^
- `#17202 <https://github.com/fortishield/fortishield/pull/17202>`_ Unified the SCA policy names.

Resolved issues
---------------

This release resolves known issues as the following: 

Agent
^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#2217 <https://github.com/fortishield/fortishield-packages/pull/2217>`_      Removed the temporary file "ossec.confre" after upgrade on macOS. 
`#2208 <https://github.com/fortishield/fortishield-packages/pull/2208>`_      Prevented the installer from corrupting the agent configuration on macOS when deployment variables were defined on upgrade.
`#2218 <https://github.com/fortishield/fortishield-packages/pull/2218>`_      Fixed the installation on macOS by removing calls to launchctl.
==============================================================    =============

Fortishield dashboard
^^^^^^^^^^^^^^^

==============================================================================================================================     =============
Reference                                                                                                                          Description
==============================================================================================================================     =============
`#5481 <https://github.com/fortishield/fortishield-kibana-app/pull/5481>`_ `#5484 <https://github.com/fortishield/fortishield-kibana-app/pull/5484>`_      Fixed command to install the macOS agent on the agent wizard. 
`#5470 <https://github.com/fortishield/fortishield-kibana-app/pull/5470>`_                                                                     Fixed command to start the macOS agent on the agent wizard.  
==============================================================================================================================     =============

Fortishield Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================================================================================     =============
Reference                                                                                                                          Description
==============================================================================================================================     =============
`#5481 <https://github.com/fortishield/fortishield-kibana-app/pull/5481>`_ `#5484 <https://github.com/fortishield/fortishield-kibana-app/pull/5484>`_      Fixed command to install the macOS agent on the agent wizard. 
`#5470 <https://github.com/fortishield/fortishield-kibana-app/pull/5470>`_                                                                     Fixed command to start the macOS agent on the agent wizard.  
==============================================================================================================================     =============


Fortishield Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================================================================================     =============
Reference                                                                                                                          Description
==============================================================================================================================     =============
`#5481 <https://github.com/fortishield/fortishield-kibana-app/pull/5481>`_ `#5484 <https://github.com/fortishield/fortishield-kibana-app/pull/5484>`_      Fixed command to install the macOS agent on the agent wizard. 
`#5470 <https://github.com/fortishield/fortishield-kibana-app/pull/5470>`_                                                                     Fixed command to start the macOS agent on the agent wizard.  
==============================================================================================================================     =============

Fortishield Splunk app
^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#1407 <https://github.com/fortishield/fortishield-splunk/pull/1407>`_        Fixed macOS agent install and restart command.  
==============================================================    =============


Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.4.3/CHANGELOG.md>`_
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-kibana-app/blob/v4.4.3-2.6.0/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.10.2 <https://github.com/fortishield/fortishield-kibana-app/blob/v4.4.3-7.10.2/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.17.x <https://github.com/fortishield/fortishield-kibana-app/blob/v4.4.3-7.17.9/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.4.3-8.2/CHANGELOG.md>`_
- `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.4.3>`_