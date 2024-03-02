.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.12.1 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_12_1:

3.12.1 Release notes - 8 April 2020
===================================

This section lists the changes in version 3.12.1. More details about these changes are provided in each component changelog:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.12.1/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v3.12.1-7.6.2/CHANGELOG.md>`_
- `fortishield/fortishield-ruleset <https://github.com/fortishield/fortishield-ruleset/blob/v3.12.1/CHANGELOG.md>`_
- `fortishield/splunk <https://github.com/fortishield/fortishield-splunk/blob/v3.12.1-8.0.2/CHANGELOG.md>`_

Fortishield core
----------

- Updated MSU catalog on 31/03/2020.
- Fixed XML validation with paths ending in ``\``.
- Fixed compatibility with the Vulnerability Detector feeds for Ubuntu from Canonical, that are available in a compressed format.
- Added missing field ``database`` to the FIM on-demand configuration report.
- Fixed a bug in Logcollector that made it forward a log to an external socket infinite times.
- Fixed a buffer overflow when receiving large messages from Syslog over TCP connections.
- Fixed a malfunction in the Integrator module when analyzing events without a certain field.
- Removed support for Ubuntu 12.04 (Precise) in Vulneratiliby Detector as its feed is no longer available.

Fortishield Kibana App
----------------

- Support Fortishield 3.12.1
- Added new FIM settings on configuration on demand.
- Updated agent's variable names in deployment guides.
- Pagination is now displayed as tables.

Fortishield ruleset
-------------

- Fixed the Dropbear brute force rule entrypoint.

Fortishield Splunk
------------

- Support for Fortishield v3.12.1.
- Added new FIM settings on configuration on demand.
