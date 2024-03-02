.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The FIM module runs periodic scans on specific paths and monitors specific directories for changes in real time. Learn more about how FIM works in this section. 
  
How it works
============

The FIM module runs periodic scans on specific paths and monitors specific directories for changes in real time. You can set which paths to monitor in the configuration of the Fortishield agents and manager.

FIM stores the files checksums and other attributes in a local FIM database. Upon a scan, the Fortishield agent reports any changes the FIM module finds in the monitored paths to the Fortishield server. The FIM module looks for file modifications by comparing the checksums of a file to its stored checksums and attribute values. It generates an alert if it finds discrepancies.

The Fortishield FIM module uses two databases to collect FIM event data, such as file creation, modification, and deletion data. One is a local SQLite-based database on the monitored endpoint that stores the data in: 

- ``C:\Program Files (x86)\ossec-agent\queue\fim\db`` on Windows.
- ``/var/ossec/queue/fim/db`` on Linux.
- ``/Library/Ossec/queue/fim/db`` on macOS. 

The other is an agent database on the Fortishield server. The :doc:`fortishield-db </user-manual/reference/daemons/fortishield-db>`. daemon creates and manages a database for each agent on the Fortishield server. It uses the ID of the agent to identify the database. This service stores the databases at ``/var/ossec/queue/db``.

.. thumbnail:: ../../../images/manual/fim/fim-flow.png
  :title: File Integrity Monitoring
  :alt: File Integrity Monitoring
  :align: center
  :width: 80%

The FIM module keeps the Fortishield agent and the Fortishield server databases synchronized with each other. It always updates the file inventory in the Fortishield server with the data available to  the Fortishield agent. An up-to-date Fortishield server database allows for servicing FIM-related API queries. The synchronization mechanism only updates the Fortishield server with information from the Fortishield agents such as checksums and file attributes that have changed. 

The Fortishield agent and manager have the FIM module enabled and :ref:`pre-configured <reference_ossec_syscheck_default_configuration>` by default. However, we recommend that you review the configuration of your endpoints to ensure that you tailor the FIM settings, such as monitored paths, to your environment.

