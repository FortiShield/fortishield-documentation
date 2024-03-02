.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.9.2 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_9_2:

3.9.2 Release notes - 10 June 2019
==================================

This section shows the most relevant improvements and fixes in version 3.9.2. More details about these changes are provided in each component changelog:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.9.2/CHANGELOG.md>`_
- `fortishield/fortishield-ruleset <https://github.com/fortishield/fortishield-ruleset/blob/v3.9.2/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v3.9.2-7.1.1/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v3.9.2-7.3.0/CHANGELOG.md>`_


Fortishield core
----------

- Fixed configuration request for whitelists when the block was empty.
- Fixed error deleting temporary files during cluster synchronization.
- Changes wrong permissions on agent groups files when they are synchronized by the cluster.
- Memory errors fixed in CIS-CAT module.
- Fixed error checking agent version in remote upgrades.
- Fixed race condition in analysis daemon when decoding SCA events. Using reentrant functions in order to maintain context between successive calls.
- Fixed a file descriptor leak in modulesd. This bug appeared when the timeout was exceeded when executing a command.
- Fixed invalid content handling RedHat feed, causes unexpected exit in Fortishield modules daemon.
- Prevent the agent from stopping if it fails to resolve the manager hostname on startup.

Fortishield apps
----------

- Fixed visualization in agent overview dashboard.
- Fix adding API data in an invalid format.
- Adapt request executed in DevTool to the API standards.
- Get same metrics security events dashboard that in the agents overview.
- Fixed SCA policy checks table.
- Added missing dependency for Discover.


Fortishield ruleset
-------------

- Fixed Windows rule about audit log.
- Fixed invalid check of the Solaris 11 SCA policy.
