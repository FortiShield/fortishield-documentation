.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.9.4 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_9_4:

3.9.4 Release notes - 7 August 2019
===================================

This section shows the most relevant improvements and fixes in version 3.9.4. More details about these changes are provided in each component changelog:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.9.4/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v3.9.4-7.2.0/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v3.9.4-7.3.0/CHANGELOG.md>`_

Fortishield agent
-----------

- Fixed a bug in FIM that made it apply a wrong configuration. This occurred when defining different options for nested directories.
- Fixed a bug in Logcollector that made it apply a wrong configuration. This happened when defining multiple stanzas for the same file with different options.
- Fixed a bug in the agent that could make it truncate its IP address within the control message.
- Fixed a bug in the Windows agent that produced a resource leak when monitoring directories in who-data mode.

Fortishield manager
-------------

- Fixed a bug in Analysisd that could potentially make it crash while handling JSON objects due to a race condition.
- Fixed a bug in Fortishield DB that could make it crash when closing database files due to a double free.
- Fixed a bug in Remoted that made it send data to an agent that has just disconnected in TCP mode.
- Prevent SCA from producing inconsistencies in the database on the manager side when policy IDs are duplicated.
- Fixed a race condition hazard between Clusterd and Remoted while synchronizing agent-related files.
- Fortishield DB did not remove a database file until was committed. Now, the database will be closed immediately.

Fortishield Apps
----------

- Allowed filtering by clicking a column in rules/decoders tables.
- Allowed open file in rules table clicking on the file column.
- Improved Kibana app performance.
- Removed path filter from custom rules and decoders.
- Now path column in rules and decoders is shown.
- Removed SCA overview dashboard.
- Disabled last custom column removal.
- Agents messages across sections have been unified.
- Fixed check stored APIs.
- Improved wz-table performance.
- Fixed inconsistent data between visualizations and tables in Overview Security Events.
- Timezone applied in cluster status.
- Fixed Overview Security Events report when fortishield.monitoring is disabled.
- Now duplicated visualization toast errors are handled.
- Fixed not properly updated breadcrumb in ruleset section.
- Implicit filters can't be destroyed now.
- Fixed windows agent dashboard that didn't show failure logon access.
- Scrollbars in file viewers have been fixed on Firefox.
- Fixed agent search filters lost when refreshing.
- Number of agents is now properly updated.
- Alerts of level 12 are now displayed on the Security Events table.
