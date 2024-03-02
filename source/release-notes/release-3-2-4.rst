.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.2.4 has been released. Check out our release notes to discover the changes and additions of this release.
  
.. _release_3_2_4:

3.2.4 Release notes - 1 June 2018
=================================

This section shows the most relevant improvements and fixes in version 3.2.4. More details about these changes are provided in each component changelog.

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.2.4/CHANGELOG.md>`_
- `fortishield/fortishield-api <https://github.com/fortishield/fortishield-api/blob/v3.2.4/CHANGELOG.md>`_
- `fortishield/fortishield-ruleset <https://github.com/fortishield/fortishield-ruleset/blob/v3.2.4/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v3.2.4-6.2.4/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-splunk <https://github.com/fortishield/fortishield-splunk/blob/v3.2.4-7.1.1/CHANGELOG.md>`_

Fortishield minor fixes
-----------------

Most of the bug fixes in this release are fairly minor, but a few fixes deserve special mention:

 - ``<queue_size>`` setting was not properly parsed by ``maild`` causing the termination of the process.
 - Python 3 incompatibilities in the framework that may affect the correct behavior of the cluster.

Fortishield app for Splunk
--------------------

This release includes:

 - New GDPR tab.
 - Multi-API support.
 - Multi-index support.
 - Several performance improvements and bug fixes.


Fortishield app for Kibana
--------------------

Relevant changes in the Fortishield app are:

 - New reporting feature: Generate reports from Overview and Agents tab.
 - New check included to warn about systems with low RAM (less than 3GB).
 - Several performance improvements and bug fixes.
