.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The fortishield-control script is used to start, stop, configure, and check the status of Fortishield processes. Learn more about it in this section.
  
.. _fortishield-control:

fortishield-control
=============

The fortishield-control script is used to start, stop, configure, check on the status of Fortishield processes and enable the debug mode.

.. note::
    We recommend using the ``systemctl`` or ``service`` commands (depending on your OS) to **start**, **stop** or **restart** the Fortishield service. This will avoid inconsistencies between the *service* status and the *processes* status.

The ``-j`` option is used for enabling JSON output format, but only in Fortishield server installations.

+-------------+---------------------------------------------------------------------------------------------------------+
| **start**   | Start the Fortishield processes.                                                                              |
+-------------+---------------------------------------------------------------------------------------------------------+
| **stop**    | Stop the Fortishield processes.                                                                               |
+-------------+---------------------------------------------------------------------------------------------------------+
| **restart** | Restart the Fortishield processes.                                                                            |
+-------------+---------------------------------------------------------------------------------------------------------+
| **reload**  | Restart all Fortishield processes except fortishield-execd.                                                         |
|             |                                                                                                         |
|             | This allows an agent to reload without losing active response status.                                   |
|             |                                                                                                         |
|             | This option is not available on a local Fortishield installation.                                             |
+-------------+---------------------------------------------------------------------------------------------------------+
| **status**  | Determine which Fortishield processes are running.                                                            |
+-------------+---------------------------------------------------------------------------------------------------------+
| **info**    | Prints the Fortishield installation type, version, and revision in environment variables format.              |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+
| **info**    |    [-v -r -t]   | Only one option at the time, prints the value of: version, revision or type.          |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+
| **enable**  |  debug          | Run all Fortishield daemons in debug mode.                                                  |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+
| **disable** | debug           | Turn off debug mode.                                                                  |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+

.. note::
    To use the database option, Database support must be compiled in during initial installation.
