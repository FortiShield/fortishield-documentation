.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.3.8 has been released. Check out our release notes to discover the changes and additions of this release.

4.3.8 Release notes - 19 September 2022
=======================================

This section lists the changes in version 4.3.8. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Fortishield agent
^^^^^^^^^^^

- `#14842 <https://github.com/fortishield/fortishield/pull/14842>`_ Updated the WPK upgrade root CA certificate.


Resolved issues
---------------

This release resolves known issues as the following: 

Fortishield manager
^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#14752 <https://github.com/fortishield/fortishield/pull/14752>`_             A wrong field assignation in Audit decoders is now fixed.
`#14825 <https://github.com/fortishield/fortishield/pull/14825>`_             A performance problem when synchronizing files through the cluster is fixed. The multigroup folder in worker nodes is no longer cleaned upon node restart.
`#14772 <https://github.com/fortishield/fortishield/pull/14772>`_             A problem when using an invalid syntax with the ``if_sid`` label is fixed. Now the rule is ignored if the listed ``if_sid`` rules are not separated by spaces or commas.
==============================================================    =============

Fortishield agent
^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#14801 <https://github.com/fortishield/fortishield/pull/14801>`_             A path traversal flaw in Active Response affecting agents from v3.6.1 to v4.3.7 is fixed. Thanks to Roshan Guragain for reporting this vulnerability.
==============================================================    =============

Packages
^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#1798 <https://github.com/fortishield/fortishield-packages/pull/1798>`__     Improved error management and IP values extraction function in the ``fortishield-certs-tool.sh``.
`#1806 <https://github.com/fortishield/fortishield-packages/pull/1806>`__     An error while changing the password in the Fortishield dashboard configuration using ``fortishield-install.sh`` is now fixed.
==============================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.3.8/CHANGELOG.md>`_
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.8-1.2.0/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.10.2 <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.8-7.10.2/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.17.x <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.8-7.17.5/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.3.8-8.2.6/CHANGELOG.md>`_
- `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.3.8>`_
