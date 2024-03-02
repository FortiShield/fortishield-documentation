.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Know the Fortishield Daemons that perform different actions between the different components of the Fortishield platform. Learn more about it in this section.

.. _daemons:

Daemons
=======

+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| Daemons                                           | Descriptions                                                    | Supported installations     |
+===================================================+=================================================================+=============================+
| :doc:`fortishield-agentd <fortishield-agentd>`                | Client side daemon that communicates with the server.           | agent                       |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-agentlessd <fortishield-agentlessd>`        | Runs integrity checking on systems where no agent is installed  | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-analysisd <fortishield-analysisd>`          | Receives log messages and compares them to the rules            | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-authd <fortishield-authd>`                  | Adds agents to the Fortishield manager                                | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-csyslogd <fortishield-csyslogd>`            | Forwards Fortishield alerts via syslog                                | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-dbd <fortishield-dbd>`                      | Inserts alert logs into a database                              | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-execd <fortishield-execd>`                  | Executes active responses                                       | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-logcollector <fortishield-logcollector>`    | Monitors configured files and commands for new log messages     | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-maild <fortishield-maild>`                  | Sends Fortishield alerts via email                                    | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-monitord <fortishield-monitord>`            | Monitors agent connectivity and compresses log files            | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-remoted <fortishield-remoted>`              | Communicates with agents                                        | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-reportd <fortishield-reportd>`              | Creates reports from Fortishield alerts                               | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-syscheckd <fortishield-syscheckd>`          | Checks configured files for security changes                    | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-clusterd <clusterd>`                  | Manages the Fortishield cluster manager                               | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-modulesd <fortishield-modulesd>`            | Manages the Fortishield modules                                       | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-db <fortishield-db>`                        | Manages the Fortishield database                                      | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`fortishield-integratord <fortishield-integratord>`      | Allows Fortishield to connect to external APIs and alerting tools     | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+


.. toctree::
    :hidden:
    :maxdepth: 1

    fortishield-agentd
    fortishield-agentlessd
    fortishield-analysisd
    fortishield-authd
    fortishield-csyslogd
    fortishield-dbd
    fortishield-execd
    fortishield-logcollector
    fortishield-maild
    fortishield-monitord
    fortishield-remoted
    fortishield-reportd
    fortishield-syscheckd
    clusterd
    fortishield-modulesd
    fortishield-db
    fortishield-integratord
