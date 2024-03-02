.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.3.0 has been released. Check out our release notes to discover the changes and additions of this release.
  
.. _release_3_3_0:

3.3.0 Release notes - 8 June 2018
=================================

This section shows the most relevant improvements and fixes in version 3.3.0. More details about these changes are provided in each component changelog.

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.3.0/CHANGELOG.md>`_
- `fortishield/fortishield-api <https://github.com/fortishield/fortishield-api/blob/v3.3.0/CHANGELOG.md>`_
- `fortishield/fortishield-ruleset <https://github.com/fortishield/fortishield-ruleset/blob/v3.3.0/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v3.3.0-6.2.4/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-splunk <https://github.com/fortishield/fortishield-splunk/blob/v3.3.0-7.1.1/CHANGELOG.md>`_

Fortishield core
----------

Logcollector now supports socket connection for log output mirroring. This feature allows to send the same event to the Fortishield manager and to a 3rd party log processor like Fluent Bit. You can find more information :ref:`here <reference_ossec_socket>`.

The analysis engine includes new options for the :ref:`plugin decoders <decoders_syntax>` to set the input offset with respect to the prematch expression or the parent decoder. See an example about this on :ref:`this section <json_decoder_example_3.3>`. In addition, plugin decoders and multi-regex decoders can be used together.

We have also introduced an :ref:`event formatter <ossec_localfile_out_format>` in the log collector to build custom events, this allows to add some data into the event.

As of this version, the timestamp of the alerts in JSON format will include milliseconds.

The implementation of the Agentless daemon has been improved for enhanced security.

Some other fixes and improvements have been introduced in the Framework and the Cluster.

Fortishield API
---------

The API now has filters by group on the ``GET /agents`` call and by status on the ``GET /agents/groups/:group_id`` and ``GET /agents/groups/:group_id`` calls.

Now the ``limit`` parameter has been modified to retrieve all items using ``limit=0``.

In addition to this, several bugfixes and performance improvements for the API have been added.

Fortishield app for Kibana
--------------------

- New design for the *Overview* and *Agents* tabs, following a breadcrumbs-based navigability to change between different sections.
- New Reporting option, for generating logs about the current state of the visualizations on the *Overview* and *Agents* tabs.
- New filters for agent version and cluster node on the *Agents Preview* tab.
- Added a warning when your system doesn't have more than 3GB of RAM.
- Several bugfixes and performance improvements.

Fortishield app for Splunk
--------------------

- Added monitoring for collecting periodical agent status data.
- Now the ``.fortishield`` index will be the default one if no one is selected.
- Several bugfixes and performance improvements.
