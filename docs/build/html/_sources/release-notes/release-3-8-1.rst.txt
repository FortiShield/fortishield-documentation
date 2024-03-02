.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.8.1 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_8_1:

3.8.1 Release notes - 24 January 2019
=====================================

This section shows the most relevant improvements and fixes in version 3.8.1. More details about these changes are provided in each component changelog:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.8.1/CHANGELOG.md>`_
- `fortishield/fortishield-api <https://github.com/fortishield/fortishield-api/blob/v3.8.1/CHANGELOG.md>`_

Fortishield core
----------

- Fixed memory leak in Logcollector when reading Windows eventchannel.
- Fixed version comparisons on Red Hat systems in vulnerability detector module.

Fortishield API
---------

- Fixed an issue with the log rotation module which may makes the Fortishield API unavailable on Debian systems.
- Fixed improper error handling. Prevented internal paths to be printed in error output.
