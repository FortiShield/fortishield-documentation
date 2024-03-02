.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
      :description: Fortishield 4.2.6 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_4_2_6:

4.2.6 Release notes - 28 March 2022
===================================

This section lists the changes in version 4.2.6. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements.

Fortishield Kibana plugin
^^^^^^^^^^^^^^^^^^^

- Fortishield Kibana plugin is now compatible with Fortishield 4.2.6.

Fortishield Splunk app
^^^^^^^^^^^^^^^^

- Fortishield Splunk app is now compatible with Fortishield 4.2.6.



Resolved issues
---------------

This release resolves known issues. 

Manager
^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#11974 <https://github.com/fortishield/fortishield/pull/11974>`_             This release resolves an integer overflow hazard in ``fortishield-remoted`` that caused it to drop incoming data after receiving 2^31 messages.
==============================================================    =============


Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.2.6/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v4.2.6-7.10.2/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.2.6-8.2.2/CHANGELOG.md>`_
