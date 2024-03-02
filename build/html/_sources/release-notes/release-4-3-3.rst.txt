.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
      :description: Fortishield 4.3.3 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_4_3_3:

4.3.3 Release notes - 1 June 2022
=================================

This section lists the changes in version 4.3.3. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements.

Fortishield Kibana plugin
^^^^^^^^^^^^^^^^^^^

- Fortishield Kibana plugin is now compatible with Fortishield 4.3.3.

Fortishield Splunk app
^^^^^^^^^^^^^^^^

- Fortishield Splunk app is now compatible with Fortishield 4.3.3. 


Resolved issues
---------------

This release resolves known issues. 

Manager
^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#13651 <https://github.com/fortishield/fortishield/pull/13651>`_             Avoid creating duplicated ``<client>`` configuration blocks during deployment. 
==============================================================    =============


Agent
^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#13642 <https://github.com/fortishield/fortishield/pull/13642>`_             Prevent `Agentd` from resetting its configuration on ``<client>`` block re-definition.
==============================================================    =============


Fortishield dashboard
^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4151 <https://github.com/fortishield/fortishield-kibana-app/pull/4151>`_    The Fortishield dashboard troubleshooting URL is now fixed. 
==============================================================    =============

Fortishield Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4150 <https://github.com/fortishield/fortishield-kibana-app/pull/4150>`_    The Fortishield Kibana plugin troubleshooting URL is now fixed.
==============================================================    =============

Fortishield Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4146 <https://github.com/fortishield/fortishield-kibana-app/pull/4146>`_    A bug that prevented removing implicit filters in modules is now fixed.  
`#4150 <https://github.com/fortishield/fortishield-kibana-app/pull/4150>`_    The Fortishield Kibana plugin troubleshooting URL is now fixed. 
==============================================================    =============



Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.3.3/CHANGELOG.md>`_
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.3-1.2.0-wzd/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.3-7.17.3/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.3.3-8.2.6/CHANGELOG.md>`_