.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The update-ruleset script updates decoders, rules, and rootchecks. Find out the arguments of this script in this section of the Fortishield documentation. 

.. _update_ruleset:

update_ruleset
=================

.. deprecated:: 4.2

The ``update-ruleset`` script updates decoders, rules, and rootchecks.

+--------+-------------------------------------------------------------------------+
| **-r** | Restart Fortishield when needed.                                              |
+--------+-------------------------------------------------------------------------+
| **-R** | Do not restart Fortishield.                                                   |
+--------+-------------------------------------------------------------------------+
| **-b** | Restore the last backup.                                                |
+--------+-------------------------------------------------------------------------+
| **-h** | Display the help message.                                               |
+--------+-------------------------------------------------------------------------+
| **-f** | Force Fortishield to update the ruleset.                                      |
+--------+-------------------------------------------------------------------------+
| **-o** | Set Fortishield path.                                                         |
+        +-----------------------------------+-------------------------------------+
|        | Default                           | /var/ossec                          |
+--------+-----------------------------------+-------------------------------------+
| **-s** | Select ruleset source path (instead of downloading it).                 |
+--------+-------------------------------------------------------------------------+
| **-j** | JSON output. Must be used in conjunction with the '-s' option.          |
+--------+-------------------------------------------------------------------------+
| **-d** | Run in debug mode.                                                      |
+--------+-------------------------------------------------------------------------+
| **-n** | Branch name (default: stable).                                          |
+--------+-------------------------------------------------------------------------+
