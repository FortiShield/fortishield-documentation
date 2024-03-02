.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.9.0 has been released. Check out our release notes to discover the changes and additions of this release.

4.9.0 Release notes - TBD
=========================

This section lists the changes in version 4.9.0. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Fortishield manager
^^^^^^^^^^^^^

- `#17306 <https://github.com/fortishield/fortishield/pull/17306>`__ Added alert forwarding to Fluentd.
- `#20285 <https://github.com/fortishield/fortishield/pull/20285>`__ Changed logging level of  fortishield-db ``recv()`` messages from error to debug.

Fortishield agent
^^^^^^^^^^^

- `#19753 <https://github.com/fortishield/fortishield/pull/19753>`__ Removed the directory ``/boot`` from the default FIM settings for AIX.

Ruleset
^^^^^^^

- `#19754 <https://github.com/fortishield/fortishield/pull/19754>`__ Clarified the description for rule ID ``23502`` about solved vulnerabilities.

Fortishield dashboard
^^^^^^^^^^^^^^^

- `#6145 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6145>`__ Added AngularJS dependencies.
- `#6120 <https://github.com/fortishield/fortishield-dashboard-plugins/issues/6120>`__ Removed embedded discover component. `#6235 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6235>`__ `#6254 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6254>`__ `#6285 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6285>`__
- `#6227 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6227>`__ Added support for a new index for the FIM module.
- `#6250 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6250>`__ Added agent groups edition to **Endpoints Summary**.

Resolved issues
---------------

This release resolves known issues as the following: 

Fortishield manager
^^^^^^^^^^^^^

==============================================================     =============
Reference                                                          Description
==============================================================     =============
`#20505 <https://github.com/fortishield/fortishield/pull/20505>`__             Fixed compilation issue for local installation.
==============================================================     =============

Fortishield agent
^^^^^^^^^^^

==============================================================     =============
Reference                                                          Description
==============================================================     =============
`#19146 <https://github.com/fortishield/fortishield/pull/19146>`__             Fixed command monitoring on Windows to support UTF-8 characters.
==============================================================     =============

Other
^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#19794 <https://github.com/fortishield/fortishield/pull/19794>`__            Fixed a buffer overflow hazard in HMAC internal library.
==============================================================    =============

Fortishield dashboard
^^^^^^^^^^^^^^^

=========================================================================    =============
Reference                                                                    Description
=========================================================================    =============
`#6237 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6237>`__       Fixed disappearing scripted fields when index pattern fields refreshed.
=========================================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.9.0/CHANGELOG.md>`__
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-dashboard-plugins/blob/v4.9.0-2.11.0/CHANGELOG.md>`__
- `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.9.0>`__
