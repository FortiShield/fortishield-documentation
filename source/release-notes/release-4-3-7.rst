.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.3.7 has been released. Check out our release notes to discover the changes and additions of this release.

4.3.7 Release notes -  24 August 2022
=====================================

This section lists the changes in version 4.3.7. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Fortishield manager
^^^^^^^^^^^^^

- `#14540 <https://github.com/fortishield/fortishield/pull/14540>`_ A cluster command to obtain custom ruleset files and their hash is added.

Fortishield agent
^^^^^^^^^^^

- `#13958 <https://github.com/fortishield/fortishield/pull/13958>`_ The logs of the Office365 integration module are improved.

RESTful API
^^^^^^^^^^^

- `#14551 <https://github.com/fortishield/fortishield/pull/14551>`_ The endpoint ``GET /cluster/ruleset/synchronization`` to check the status of the synchronization of the ruleset in a cluster is added.
- `#14208 <https://github.com/fortishield/fortishield/pull/14208>`_ The performance of framework functions for MITRE API endpoints is improved.

Ruleset
^^^^^^^

- `#13806 <https://github.com/fortishield/fortishield/pull/13806>`_ An SCA Policy for CIS Microsoft Windows 11 Enterprise Benchmark v1.0.0 is added.
- `#13879 <https://github.com/fortishield/fortishield/pull/13879>`_ The SCA Policy for CIS Microsoft Windows 10 Enterprise is updated with the benchmark v1.12.0 for the release 21H2.
- `#13843 <https://github.com/fortishield/fortishield/pull/13843>`_ An SCA policy for Red Hat Enterprise Linux 9 (RHEL9) is added.
- `#13899 <https://github.com/fortishield/fortishield/pull/13899>`_ An SCA policy for CIS Microsoft Windows Server 2022 Benchmark 1.0.0 is added.

Fortishield dashboard
^^^^^^^^^^^^^^^

- `#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_ The deprecated ``manager_host`` field in Fortishield API responses about agent information is no longer used.

Fortishield Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- `#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_ The deprecated ``manager_host`` field in Fortishield API responses about agent information is no longer used.

Fortishield Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- `#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_ The deprecated ``manager_host`` field in Fortishield API responses about agent information is no longer used.

Fortishield Splunk app
^^^^^^^^^^^^^^^^

- Fortishield Splunk app is now compatible with Fortishield 4.3.7.

Packages
^^^^^^^^

-  `#1737 <https://github.com/fortishield/fortishield-packages/pull/1737>`_ passwords-tool tests are added with the files ``passwords-tool.yml`` and ``tests-stack.sh``.
-  `#1742 <https://github.com/fortishield/fortishield-packages/pull/1742>`_ A port status check is added to the Fortishield installation assistant to avoid the installation ending up in failure if one of the Fortishield default ports is being used.
-  `#1754 <https://github.com/fortishield/fortishield-packages/pull/1754>`_ Skipping the OS check of the ``fortishield-install.sh`` script when downloading files is added.
-  `#1629 <https://github.com/fortishield/fortishield-packages/pull/1629>`_ The ``-tmp`` option is added to the the ``fortishield-certs-tool`` script in order to specify the ``tmp`` directory.
-  `#1685 <https://github.com/fortishield/fortishield-packages/pull/1685>`_ The RHEL 9 SCA files are added to the specs.
-  `#1734 <https://github.com/fortishield/fortishield-packages/pull/1734>`_ All Zypper references are removed from the unattended and test directories.
-  `#1753 <https://github.com/fortishield/fortishield-packages/pull/1753>`_ TLS versions lower than v1.2 are disabled to avoid using weak cipher suites.
-  `#1641 <https://github.com/fortishield/fortishield-packages/pull/1641>`_ Removed the revision variables from the Fortishield installation assistant.
-  `#1750 <https://github.com/fortishield/fortishield-packages/pull/1750>`_ The OVA generation scripts are modified to adapt them to the newest changes in ``fortishield-passwords-tool.sh``.
-  `#1769 <https://github.com/fortishield/fortishield-packages/pull/1769>`_ The path when copying Fedora SCA files is fixed with the new versions.


RPM revision 2
~~~~~~~~~~~~~~
-  `v4.3.7-2 <https://github.com/fortishield/fortishield-packages/releases/tag/v4.3.7-2>`_ A bug related to the installation of the SCA policy in RHEL8 is fixed. This error caused the RHEL 9 SCA policy to be installed in RHEL 8 machines instead of the correct one.


Resolved issues
---------------

This release resolves known issues as the following: 

Fortishield manager
^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#13956 <https://github.com/fortishield/fortishield/pull/13956>`_             A bug in Analysisd that may make it crash when decoding regexes with more than 14 subpatterns is fixed.
`#14366 <https://github.com/fortishield/fortishield/pull/14366>`_             The risk of a crash when Vulnerability Detector parses OVAL feeds is fixed.
`#14436 <https://github.com/fortishield/fortishield/pull/14436>`_             A busy-looping in ``fortishield-maild`` when monitoring ``alerts.json`` is fixed.
`#14417 <https://github.com/fortishield/fortishield/pull/14417>`_             A segmentation fault in ``fortishield-maild`` when parsing alerts exceeding the nesting limit is fixed.
==============================================================    =============

Fortishield agent
^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#14368 <https://github.com/fortishield/fortishield/pull/14368>`_             A code defect in the GitHub integration module reported by Coverity is fixed.
`#14518 <https://github.com/fortishield/fortishield/pull/14518>`_             An undefined behavior in the agent unit tests is fixed.
==============================================================    =============

Ruleset
^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#14513 <https://github.com/fortishield/fortishield/pull/14513>`_             A bug found in the regular expression used for check 5.1.1 (ID 19137) of the Ubuntu 20 SCA policy file that caused false positives is fixed.
`#14483 <https://github.com/fortishield/fortishield/pull/14483>`_             An error when a Fortishield agent runs an AWS Amazon Linux SCA policy is fixed.
`#13950 <https://github.com/fortishield/fortishield/pull/13950>`_             Amazon Linux 2 SCA policy is modified to resolve rules and conditions on control 1.5.2.
`#14481 <https://github.com/fortishield/fortishield/pull/14481>`_             Missing SCA files are added to the Fortishield manager installation.
`#14678 <https://github.com/fortishield/fortishield/pull/14678>`_             OS detection in Ubuntu 20.04 LTS SCA policy is now fixed. 
==============================================================    =============

Fortishield dashboard
^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4378 <https://github.com/fortishield/fortishield-kibana-app/pull/4378>`_    Link to web documentation and some grammatical errors in the file ``fortishield.yml`` are fixed. Also, the in-file documentation is improved.
`#4399 <https://github.com/fortishield/fortishield-kibana-app/pull/4399>`_    The ``config-equivalences`` file is moved to the ``common`` folder to make it available for the entire application.
`#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_    An error during the generation of a group's report, if the request to the Fortishield API fails, is fixed.
`#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_    A problem with the group's report, when the group has no agents, is fixed.
`#4352 <https://github.com/fortishield/fortishield-kibana-app/pull/4352>`_    A path in the logo customization section is fixed.
`#4362 <https://github.com/fortishield/fortishield-kibana-app/pull/4362>`_    A TypeError in a resource that fails in Chrome and Firefox browsers is fixed.
`#4358 <https://github.com/fortishield/fortishield-kibana-app/pull/4358>`_    An error creating PDF reports when using Kibana with X-Pack without authentication context is fixed.
`#4359 <https://github.com/fortishield/fortishield-kibana-app/pull/4359>`_    Module settings not persisting between updates is fixed.
`#4367 <https://github.com/fortishield/fortishield-kibana-app/pull/4367>`_    A search bar error on the SCA Inventory table is fixed.
`#4373 <https://github.com/fortishield/fortishield-kibana-app/pull/4373>`_    A routing loop when reinstalling the Fortishield indexer is fixed.
==============================================================    =============

Fortishield Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4378 <https://github.com/fortishield/fortishield-kibana-app/pull/4378>`_    Link to web documentation and some grammatical errors in the file ``fortishield.yml`` are fixed. Also, the in-file documentation is improved.
`#4399 <https://github.com/fortishield/fortishield-kibana-app/pull/4399>`_    The ``config-equivalences`` file is moved to the ``common`` folder to make it available for the entire application.
`#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_    An error during the generation of a group's report, if the request to the Fortishield API fails, is fixed.
`#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_    A problem with the group's report, when the group has no agents, is fixed.
`#4352 <https://github.com/fortishield/fortishield-kibana-app/pull/4352>`_    A path in the logo customization section is fixed.
`#4362 <https://github.com/fortishield/fortishield-kibana-app/pull/4362>`_    A TypeError in a resource that fails in Chrome and Firefox browsers is fixed.
`#4358 <https://github.com/fortishield/fortishield-kibana-app/pull/4358>`_    An error creating PDF reports when using Kibana with X-Pack without authentication context is fixed.
`#4359 <https://github.com/fortishield/fortishield-kibana-app/pull/4359>`_    The persistence of the plugin registry file between updates is fixed.
`#4367 <https://github.com/fortishield/fortishield-kibana-app/pull/4367>`_    A search bar error on the SCA Inventory table is fixed.
`#4373 <https://github.com/fortishield/fortishield-kibana-app/pull/4373>`_    A routing loop when reinstalling the Fortishield indexer is fixed.
==============================================================    =============

Fortishield Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4378 <https://github.com/fortishield/fortishield-kibana-app/pull/4378>`_    Link to web documentation and some grammatical errors in the file ``fortishield.yml`` are fixed. Also, the in-file documentation is improved.
`#4399 <https://github.com/fortishield/fortishield-kibana-app/pull/4399>`_    The ``config-equivalences`` file is moved to the ``common`` folder to make it available for the entire application.
`#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_    An error during the generation of a group's report, if the request to the Fortishield API fails, is fixed.
`#4350 <https://github.com/fortishield/fortishield-kibana-app/pull/4350>`_    A problem with the group's report, when the group has no agents, is fixed.
`#4352 <https://github.com/fortishield/fortishield-kibana-app/pull/4352>`_    A path in the logo customization section is fixed.
`#4362 <https://github.com/fortishield/fortishield-kibana-app/pull/4362>`_    A TypeError in a resource that fails in Chrome and Firefox browsers is fixed.
`#4358 <https://github.com/fortishield/fortishield-kibana-app/pull/4358>`_    An error creating PDF reports when using Kibana with X-Pack without authentication context is fixed.
`#4359 <https://github.com/fortishield/fortishield-kibana-app/pull/4359>`_    Module settings not persisting between updates is fixed.
`#4367 <https://github.com/fortishield/fortishield-kibana-app/pull/4367>`_    A search bar error on the SCA Inventory table is fixed.
`#4373 <https://github.com/fortishield/fortishield-kibana-app/pull/4373>`_    A routing loop when reinstalling the Fortishield indexer is fixed.
==============================================================    =============

Fortishield Splunk app
^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#1359 <https://github.com/fortishield/fortishield-splunk/pull/1359>`_        The API console suggestions were not working in version 4.3.6 and are now fixed.
==============================================================    =============

Packages
^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#1762 <https://github.com/fortishield/fortishield-packages/pull/1762>`__     The Fortishield GPG key is now removed when uninstalling all the Fortishield components using the installation assistant.
`#1765 <https://github.com/fortishield/fortishield-packages/pull/1765>`__     Handling of errors that might happen when downloading Filebeat files is added.
`#1766 <https://github.com/fortishield/fortishield-packages/pull/1766>`__     A check of the indentation of the ``config.yml`` file is added.
`#1731 <https://github.com/fortishield/fortishield-packages/pull/1731>`_      An error when installing every component of a distributed installation in the same host using the 127.0.0.1 IP address is fixed.
`#1619 <https://github.com/fortishield/fortishield-packages/pull/1619>`_      The code of the Fortishield installation assistant has been improved.
==============================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.3.7/CHANGELOG.md>`_
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.7-1.2.0/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.10.2 <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.7-7.10.2/CHANGELOG.md>`_
- `fortishield/fortishield-kibana-app 7.17.x <https://github.com/fortishield/fortishield-kibana-app/blob/v4.3.7-7.17.5/CHANGELOG.md>`_
- `fortishield/fortishield-splunk <https://github.com/fortishield/fortishield-splunk/blob/v4.3.7-8.2.6/CHANGELOG.md>`_
- `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.3.7>`_
