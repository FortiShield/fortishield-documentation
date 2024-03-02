.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.12.3 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_12_3:

3.12.3 Release notes - 30 April 2020
====================================

This section lists the changes in version 3.12.3. More details about these changes are provided in each component changelog:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.12.3/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app <https://github.com/fortishield/fortishield-kibana-app/blob/v3.12.3-7.6.2/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v3.12.3-8.0.2/CHANGELOG.md>`_

Fortishield core
----------

    - Disabled WAL in databases handled by Fortishield DB to save disk space.
    - Fixed a bug in Remoted that could prevent agents from connecting in UDP mode.
    - Fixed a bug in the shared library that caused that daemons could not find the ossec group.
    - Prevented Syscollector from falling into an infinite loop when failed to collect the Windows hotfixes.
    - Fixed a memory leak in the system scan by Rootcheck on Windows.
    - Fixed a bug in Logcollector that caused that the ``out_format`` option did not apply for the targeted agent.
    - Fixed a bug that caused FIM could not handle large inode numbers correctly.
    - Fixed a bug that made ossec-dbd crash due to a bad mutex initialization.


Fortishield Kibana App
----------------

- Support for Fortishield v3.12.3


Fortishield Splunk
------------

- Support for Fortishield v3.12.3

