.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.8.2 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_8_2:

3.8.2 Release notes - 31 January 2019
=====================================

This section shows the most relevant fixes in version 3.8.2. A complete list of changes is provided in the `change log <https://github.com/fortishield/fortishield/blob/v3.8.2/CHANGELOG.md>`_.

Fortishield manager
-------------

- Fixed a bug crashing Analysisd when accumulating logs. This bug affected decoders that use the option ``<accumulate>``, like the decoder for OpenLDAP logs, provided out of the box.
- Some fields of alerts related to Windows Eventchannel logs included unwanted backslashes (``\``) and trailing whitespaces. This was due to a log cleaning issue in the manager.

Fortishield agent
-----------

- Prevent Modulesd from crashing when the configuration contained a ``<wodle name="command">`` stanza without an explicit ``<tag>`` option.
