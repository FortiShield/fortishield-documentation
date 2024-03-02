.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.13.1 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_13_1:

3.13.1 Release notes - 15 July 2020
===================================

This section lists the changes in version 3.13.1. More details about these changes are provided in each component changelog:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.13.1/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/3.13.1-7.8.0/CHANGELOG.md>`_
- `fortishield/fortishield-api <https://github.com/fortishield/fortishield-api/blob/3.13/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/3.13-8.0/CHANGELOG.md>`_

Fortishield core
----------

- Added the settings ``<max_retries>`` and ``<retry_interval>`` to adjust the amount of connection retries and the agent failover interval.
- Fixed ``Modulesd`` crash caused by Vulnerability Detector when OS inventory is disabled for the agent.

Fortishield Kibana app
----------------

- Support for Fortishield v3.13.1.

Fortishield API
---------

- New validator added to the endpoint ``/sca/:agent_id/checks/:policy_id`` that allows using filter the SCA checks by ``reason``, ``status``, and ``command``.

Fortishield Splunk
------------

- Support for Fortishield v3.13.1.
- Support for Splunk v8.0.4.
- Updated references of the field ``vulnerability.reference`` to ``vulnerability.references``.
- Fixed ``fortishield-monitoring`` indices on Splunk 8.0+ version.
