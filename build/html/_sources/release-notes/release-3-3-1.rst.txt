.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 3.3.1 has been released. Check out our release notes to discover the changes and additions of this release.
  
.. _release_3_3_1:

3.3.1 Release notes - 18 June 2018
==================================

This section shows the most relevant improvements and fixes in version 3.3.1. More details about these changes are provided in each component changelog.

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v3.3.1/CHANGELOG.md>`_
- `fortishield/fortishield-api <https://github.com/fortishield/fortishield-api/blob/v3.3.1/CHANGELOG.md>`_
- `fortishield/fortishield-ruleset <https://github.com/fortishield/fortishield-ruleset/blob/v3.3.1/CHANGELOG.md>`_

Fortishield core
----------

Most of the fixes introduced in this new version are focused on the user experience when dealing with the Fortishield management. Improving log messages and
configuration issues among other things. There are a few changes which are worth highlighting:

- Fixed a bug that prevented the remote upgrades for Ubuntu agents.
- An alert has been added to be aware when the process of unmerging the centralized configuration fails.
- Prevent interference between the Windows Defender antivirus and the Fortishield agent when managing temporary bookmark files.
- It is now possible to set up empty blocks of configuration for some modules. For example, the vulnerability detector module can be enabled by typing ``<wodle name="vulnerability-detector"/>``, applying it the default configuration for that module.

Fortishield API
---------

- The request to delete agents includes two new fields with the affected agents by the deletion request, as well as the failed IDs.
- Fixed error when trying to upgrade `Never connected` agents by the API.
