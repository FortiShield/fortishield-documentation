.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Find out how to verify sections of the Fortishield configuration in this section of the Fortishield documentation.

.. _verifying_configuration:

Verifying configuration
========================

+--------------------------------------+----------------------------------------+
| Configuration section                | command                                |
+======================================+========================================+
| Syscheck/Rootcheck                   | /var/ossec/bin/fortishield-syscheckd -t      |
+--------------------------------------+----------------------------------------+
| local files                          | /var/ossec/bin/fortishield-logcollector -t   |
+--------------------------------------+----------------------------------------+
| Wodles                               | /var/ossec/bin/fortishield-modulesd -t       |
+--------------------------------------+----------------------------------------+
| global/rules/decoders (manager only) | /var/ossec/bin/fortishield-analysisd -t      |
+--------------------------------------+----------------------------------------+
| Client (agent only)                  | /var/ossec/bin/fortishield-agentd -t         |
+--------------------------------------+----------------------------------------+
