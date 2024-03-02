.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.6.1 has been released. Check out our release notes to discover the changes and additions of this release.
  
.. _release_3_6_1:

3.6.1 Release notes - 7 September 2018
======================================

This section shows the most relevant improvements and fixes in version 3.6.1. More details about these changes are provided in each component changelog.

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.6.1/CHANGELOG.md>`_
- `fortishield/fortishield-api <https://github.com/fortishield/fortishield-api/blob/v3.6.1/CHANGELOG.md>`_
- `fortishield/fortishield-ruleset <https://github.com/fortishield/fortishield-ruleset/blob/v3.6.1/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v3.6.1-6.4.1/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v3.6.1-7.1.3/CHANGELOG.md>`_

Fortishield core
----------

This release is a patch version that fixes some issues encountered in v3.6.0. Some of them are listed below:

- The *agent.name* field has been put back to the alerts in JSON format. On the other hand, we've fixed a problem in the *location* description of the plain-text alerts.
- Vulnerability Detector has been improved to support Debian Sid (the unstable version).
- We have also optimized the memory management on agents for AIX and HP-UX systems.
- The daemon start and stop list has been reordered in the agent service.
- We have corrected the actual recursion level limit in FIM real-time mode.
- We have improved the AWS integration parser and its capabilities.
- Some other fixes have been applied on this version.

Fortishield API
---------

In this version, the API makes it possible to send Active Response requests, including custom commands that are not declared in the configuration.

For instance:

.. code-block:: console

    curl -u foo:bar -X PUT -d '{"command":"restart-ossec0", "arguments": ["-", "null", "(from_the_server)", "(no_rule_id)"]}' -H 'Content-Type:application/json' "http://localhost:55000/active-response/001?pretty"

.. code-block:: json
    :class: output

    {
      "error": 0,
      "message": "Command sent."
    }
