.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield 4.8.0 has been released. Check out our release notes to discover the changes and additions of this release.

4.8.0 Release notes - TBD
=========================

This section lists the changes in version 4.8.0. Every update of the Fortishield solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Manager
^^^^^^^

- `#21201 <https://github.com/fortishield/fortishield/pull/21201>`__ Refactored vulnerability detection capability.
- `#16058 <https://github.com/fortishield/fortishield/pull/16058>`__ Added new ``rollback`` query to ``fortishield-db``.
- `#18476 <https://github.com/fortishield/fortishield/pull/18476>`__ Improved ``fortishield-db`` detection of deleted database files.
- `#16893 <https://github.com/fortishield/fortishield/pull/16893>`__ Added ``timeout`` and ``retry`` parameters to the VirusTotal integration.
- `#18988 <https://github.com/fortishield/fortishield/pull/18988>`__ Extended ``fortishield-analysisd`` EPS metrics with events dropped by overload and remaining credits in the previous cycle.
- `#19819 <https://github.com/fortishield/fortishield/pull/19819>`__ Replaced Filebeat date index name processor to ensure the indices are identifiable by the index alias for auto-rollover.
- `#18466 <https://github.com/fortishield/fortishield/pull/18466>`__ Updated API and framework packages installation commands to use ``pip`` instead of direct invocation of ``setuptools``.
- `#17015 <https://github.com/fortishield/fortishield/pull/17015>`__ Refactored how cluster status dates are treated in the cluster.
- `#21602 <https://github.com/fortishield/fortishield/pull/21602>`__ The log message about file rotation and signature from fortishield-monitord has been updated.

Agent
^^^^^

- `#15740 <https://github.com/fortishield/fortishield/pull/15740>`__ Added snap package manager support to Syscollector.
- `#18574 <https://github.com/fortishield/fortishield/pull/18574>`__ Disabled host's IP query by Logcollector when ``ip_update_interval=0``.
- `#17932 <https://github.com/fortishield/fortishield/pull/17932>`__ Added event size validation for the external integrations.
- `#17623 <https://github.com/fortishield/fortishield/pull/17623>`__ Refactored and modularized the AWS integration code.
- `#19064 <https://github.com/fortishield/fortishield/pull/19064>`__ Added multiple tenants support to the MS Graph integration module.
- `#16200 <https://github.com/fortishield/fortishield/pull/16200>`__ FIM now buffers the Linux audit events for who-data to prevent side effects in other components.
- `#19720 <https://github.com/fortishield/fortishield/pull/19720>`__ The sub-process execution implementation has been improved.
- `#20649 <https://github.com/fortishield/fortishield/pull/20649>`__ Added geolocation mapping for the AWS WAF events.
- `#21530 <https://github.com/fortishield/fortishield/pull/21530>`__ Added a validation to reject unsupported regions when using the inspector service.
- `#21561 <https://github.com/fortishield/fortishield/pull/21561>`__ Added additional information on some AWS integration errors.

RESTful API
^^^^^^^^^^^

- `#19952 <https://github.com/fortishield/fortishield/pull/19952>`__ Added new ``GET /manager/version/check`` API endpoint to obtain information about new releases of Fortishield.
- `#20119 <https://github.com/fortishield/fortishield/pull/20119>`__ Removed ``PUT /vulnerability``, ``GET /vulnerability/{agent_id}``, ``GET /vulnerability/{agent_id}/last_scan`` and ``GET /vulnerability/{agent_id}/summary/{field}`` API endpoints as they were deprecated in version 4.7.0. Use the Fortishield indexer REST API instead.
- `#20420 <https://github.com/fortishield/fortishield/pull/20420>`__ Added the ``auto`` option to the ``ssl_protocol`` setting in the API configuration. This option enables automatic negotiation of the TLS certificate.
- `#21572 <https://github.com/fortishield/fortishield/pull/21572>`__ Removed the ``compilation_date`` field from ``GET /cluster/{node_id}/info`` and ``GET /manager/info`` endpoints.

Ruleset
^^^^^^^

- `#19528 <https://github.com/fortishield/fortishield/pull/19528>`__ Added rules to detect IcedID attacks.
- `#17780 <https://github.com/fortishield/fortishield/pull/17780>`__ Added new SCA policy for Amazon Linux 2023.
- `#17784 <https://github.com/fortishield/fortishield/pull/17784>`__ Added new SCA policy for Rocky Linux 8.
- `#18721 <https://github.com/fortishield/fortishield/pull/18721>`__ Revised SCA policy for Ubuntu Linux 18.04.
- `#17515 <https://github.com/fortishield/fortishield/pull/17515>`__ Revised SCA policy for Ubuntu Linux 22.04.
- `#18440 <https://github.com/fortishield/fortishield/pull/18440>`__ Revised SCA policy for Red Hat Enterprise Linux 7.
- `#17770 <https://github.com/fortishield/fortishield/pull/17770>`__ Revised SCA policy for Red Hat Enterprise Linux 8.
- `#17412 <https://github.com/fortishield/fortishield/pull/17412>`__ Revised SCA policy for Red Hat Enterprise Linux 9.
- `#17624 <https://github.com/fortishield/fortishield/pull/17624>`__ Revised SCA policy for CentOS 7.
- `#18439 <https://github.com/fortishield/fortishield/pull/18439>`__ Revised SCA policy for CentOS 8.
- `#18010 <https://github.com/fortishield/fortishield/pull/18010>`__ Revised SCA policy for Debian 8.
- `#17922 <https://github.com/fortishield/fortishield/pull/17922>`__ Revised SCA policy for Debian 10.
- `#18695 <https://github.com/fortishield/fortishield/pull/18695>`__ Revised SCA policy for Amazon Linux 2.
- `#18985 <https://github.com/fortishield/fortishield/pull/18985>`__ Revised SCA policy for SUSE Linux Enterprise 15.
- `#19037 <https://github.com/fortishield/fortishield/pull/19037>`__ Revised SCA policy for macOS 13.0 Ventura.
- `#19515 <https://github.com/fortishield/fortishield/pull/19515>`__ Revised SCA policy for Microsoft Windows 10 Enterprise.
- `#20044 <https://github.com/fortishield/fortishield/pull/20044>`__ Revised SCA policy for Microsoft Windows 11 Enterprise.
- `#17518 <https://github.com/fortishield/fortishield/pull/17518>`__ Updated MITRE DB to v13.1.

Other
^^^^^

- `#20003 <https://github.com/fortishield/fortishield/pull/20003>`__ Upgraded external ``aiohttp`` library dependency version to ``3.8.5``.
- `#21055 <https://github.com/fortishield/fortishield/pull/21055>`__ Upgraded external ``cryptography`` library dependency version to ``41.0.7``.
- `#20003 <https://github.com/fortishield/fortishield/pull/20003>`__ Upgraded external ``numpy`` library dependency version to ``1.26.0``.
- `#20003 <https://github.com/fortishield/fortishield/pull/20003>`__ Upgraded external ``pyarrow`` library dependency version to ``14.0.1``.
- `#20003 <https://github.com/fortishield/fortishield/pull/20003>`__ Upgraded external ``grpcio`` library dependency version to ``1.58.0``.
- `#20630 <https://github.com/fortishield/fortishield/pull/20630>`__ Upgraded external ``urllib3`` library dependency version to ``1.26.18``.
- `#20741 <https://github.com/fortishield/fortishield/pull/20741>`__ Upgraded external ``SQLAlchemy`` library dependency version to ``2.0.23``.
- `#21684 <https://github.com/fortishield/fortishield/pull/21684>`__ Upgraded external ``Jinja2`` library dependency version to ``3.1.3``.
- `#20003 <https://github.com/fortishield/fortishield/pull/20003>`__ Upgraded embedded Python version to ``3.10.13``.

Fortishield dashboard
^^^^^^^^^^^^^^^

- `#5791 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/5791>`__ Added remember server address check.
- `#6093 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6093>`__ Added a notification about new Fortishield updates and a button to check their availability. `#6256 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6256>`__ `#6328 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6328>`__
- `#6083 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6083>`__ Added the ``ssl_agent_ca`` configuration to the **SSL Settings** form.
- `#5896 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/5896>`__ Added global vulnerability dashboards. `#6179 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6179>`__ `#6173 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6173>`__ `#6147 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6147>`__ `#6231 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6231>`__ `#6246 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6246>`__ `#6321 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6321>`__ `#6338 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6338>`__ `#6356 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6356>`__
- `#5840 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/5840>`__ Added an agent selector to the IT Hygiene module.
- `#5840 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/5840>`__ Moved the Fortishield menu into the side menu. `#6226 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6226>`__
- `#5840 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/5840>`__ Removed the ``disabled_roles`` and ``customization.logo.sidebar`` settings.
- `#5840 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/5840>`__ Removed module visibility configuration and removed the ``extensions.*`` settings.
- `#6106 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6106>`__ Added query results limit of 10000 hits.
- `#6035 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6035>`__ Improved the implementation of module dashboards.
- `#6067 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6067>`__ Reorganized tabs order in all modules.
- `#6174 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6174>`__ Removed the implicit filter of WQL language of the search bar UI.
- `#6176 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6176>`__ Added a redirection button to **Endpoint Summary** from **IT Hygiene** application.
- `#6176 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6176>`__ Removed the application menu in the **IT Hygiene** application.
- `#6373 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6373>`__ Changed the **API configuration** title to **API Connections**.
- `#6366 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6366>`__ Removed **Compilation date** field from the **Status** view.
- `#6361 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6361>`__ Removed ``FORTISHIELD_REGISTRATION_SERVER`` variable from Windows agent deployment command.
- `#6354 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6354>`__ Added a dash character and a tooltip element to **Run as** in the API configuration table to indicate it's been disabled.
- `#6364 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6364>`__ Added tooltip element to **Most active agent** in **Details** in the **Endpoint summary** view and renamed a label element.
- `#6379 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6379>`__ Changed overview home top KPIs.

Packages
^^^^^^^^

- `#2332 <https://github.com/fortishield/fortishield-packages/pull/2332>`_ Added check into the installation assistant to prevent the use of public IP addresses.
- `#2582 <https://github.com/fortishield/fortishield-packages/pull/2582>`_ Added the ISM init script to the Fortishield indexer package to handle the creation of ISM policies.
- `#2584 <https://github.com/fortishield/fortishield-packages/pull/2584>`_ Added ISM init script to the installation assistant.
- `#2365 <https://github.com/fortishield/fortishield-packages/pull/2365>`_ Removed the ``postProvision.sh`` script. It's no longer used in OVA generation.
- `#2364 <https://github.com/fortishield/fortishield-packages/pull/2364>`_ Added ``curl`` error messages in downloads.
- `#2469 <https://github.com/fortishield/fortishield-packages/pull/2469>`_ Improved debug output in the installation assistant.
- `#2300 <https://github.com/fortishield/fortishield-packages/pull/2300>`_ Added SCA policy for Rocky Linux 8 in SPECS.
- `#2557 <https://github.com/fortishield/fortishield-packages/pull/2557>`_ Added SCA policy for Amazon Linux 2023 in SPECS.
- `#2558 <https://github.com/fortishield/fortishield-packages/pull/2558>`_ Fortishield password tool now recognizes UI created users.
- `#2562 <https://github.com/fortishield/fortishield-packages/pull/2562>`_ Bumped Fortishield indexer to OpenSearch 2.10.0.
- `#2563 <https://github.com/fortishield/fortishield-packages/pull/2563>`_ Bumped Fortishield dashboard to OpenSearch Dashboards 2.10.0.
- `#2577 <https://github.com/fortishield/fortishield-packages/pull/2577>`_ Added APT and YUM lock logic to the Fortishield installation assistant.
- `#2553 <https://github.com/fortishield/fortishield-packages/pull/2553>`_ Added new role to grant ISM API permissions.
- `#2164 <https://github.com/fortishield/fortishield-packages/pull/2164>`_ Deprecated CentOS 6 and Debian 7 for the Fortishield manager compilation, while still supporting them in the Fortishield agent compilation.
- `#2588 <https://github.com/fortishield/fortishield-packages/pull/2588>`_ Added logic to the installation assistant to check for clean Fortishield central components removal.
- `#2615 <https://github.com/fortishield/fortishield-packages/pull/2615>`_ Added branding images to the header of Fortishield dashboard.
- `#2696 <https://github.com/fortishield/fortishield-packages/pull/2696>`_ Updated Filebeat module version to 0.4 in Fortishield installation assistant.
- `#2695 <https://github.com/fortishield/fortishield-packages/pull/2695>`_ Added content database in RPM and DEB packages.
- `#2669 <https://github.com/fortishield/fortishield-packages/pull/2669>`_ Upgraded ``botocore`` dependency in WPK package Docker containers.
- `#2738 <https://github.com/fortishield/fortishield-packages/pull/2738>`_ Added ``xz utils`` as requirement.
- `#2777 <https://github.com/fortishield/fortishield-packages/pull/2777>`_ Added support for refactored vulnerability detector in the installation assistant.
- `#2797 <https://github.com/fortishield/fortishield-packages/pull/2797>`_ The installation assistant now uses ``127.0.0.1`` instead of ``localhost`` in dashboard configuration.
- `#2801 <https://github.com/fortishield/fortishield-packages/pull/2801>`_ Added check into the installation assistant to ensure ``sudo`` package is installed.
- `#2792 <https://github.com/fortishield/fortishield-packages/pull/2792>`_ Improved certificates generation tool output.
- `#2804 <https://github.com/fortishield/fortishield-packages/pull/2804>`_ Added keystore tool creation for manager packages.
- `#2802 <https://github.com/fortishield/fortishield-packages/pull/2802>`_ Added fortishield-keystore in passwords tool.
- `#2809 <https://github.com/fortishield/fortishield-packages/pull/2809>`_ Upgrade scripts to support building Fortishield with OpenSSL 3.0.


Resolved issues
---------------

This release resolves known issues as the following:

Fortishield manager
^^^^^^^^^^^^^

==============================================================     =============
Reference                                                          Description
==============================================================     =============
`#17886 <https://github.com/fortishield/fortishield/pull/17886>`__             Updated cluster connection cleanup to remove temporary files when the connection between a worker and a master is broken.
==============================================================     =============

Agent
^^^^^

==============================================================     =============
Reference                                                          Description
==============================================================     =============
`#16839 <https://github.com/fortishield/fortishield/pull/16839>`__             Fixed process path retrieval in Syscollector on Windows XP.
`#16056 <https://github.com/fortishield/fortishield/pull/16056>`__             Fixed the OS version detection on Alpine Linux.
`#18642 <https://github.com/fortishield/fortishield/pull/18642>`__             Fixed Solaris 10 name not showing in the dashboard.
==============================================================     =============

RESTful API
^^^^^^^^^^^

==============================================================     =============
Reference                                                          Description
==============================================================     =============
`#20527 <https://github.com/fortishield/fortishield/pull/20527>`__             Fixed a warning from SQLAlchemy involving detached Roles instances in RBAC.
==============================================================     =============

Fortishield dashboard
^^^^^^^^^^^^^^^

=========================================================================    =============
Reference                                                                    Description
=========================================================================    =============
`#5840 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/5840>`__       Fixed a problem with the agent menu header when the side menu is docked.
`#6102 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6102>`__       Fixed how the query filters apply on the Security Alerts table.
`#6177 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6177>`__       Fixed exception in **IT-Hygiene** when an agent doesn't have policies.
`#6177 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6177>`__       Fixed exception in **Inventory** when agents don't have operating system information.
`#6177 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6177>`__       Fixed pinned agent state in URL.
`#6234 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6234>`__       Fixed invalid date format in **About** and **Agents** views.
`#6305 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6305>`__       Fixed issue with script to install agents on macOS if using the registration password deployment variable.
`#6327 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6327>`__       Fixed an issue preventing the use of a hostname as the **Server address** in **Deploy New Agent**.
`#6345 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6345>`__       Fixed unnecessary scrolling in the vulnerability **Inventory** table.
`#6342 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6342>`__       Fixed wrong **Queue Usage** values in **Server management** > **Statistics**.
`#6352 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6352>`__       Fixed **Statistics** view errors when cluster mode is disabled.
`#6374 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6374>`__       Fixed the help menu, to be consistent and avoid duplication.
`#6378 <https://github.com/fortishield/fortishield-dashboard-plugins/pull/6378>`__       Fixed the axis label visual bug from dashboards.
=========================================================================    =============

Packages
^^^^^^^^

=====================================================================     =============
Reference                                                                 Description
=====================================================================     =============
`#2381 <https://github.com/fortishield/fortishield-packages/pull/2381>`_              Fixed DNS validation in the Installation Assistant.
`#2401 <https://github.com/fortishield/fortishield-packages/pull/2401>`_              Fixed debug redirection in Installation Assistant.
=====================================================================     =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `fortishield/fortishield <https://github.com/fortishield/fortishield/blob/v4.8.0/CHANGELOG.md>`__
- `fortishield/fortishield-dashboard <https://github.com/fortishield/fortishield-dashboard-plugins/blob/v4.8.0-2.10.0/CHANGELOG.md>`__
- `fortishield/fortishield-packages <https://github.com/fortishield/fortishield-packages/releases/tag/v4.8.0>`__
