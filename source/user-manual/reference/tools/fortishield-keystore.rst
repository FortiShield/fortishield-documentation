.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Tool where sensitive configuration data can be securely stored, including any information that the Fortishield manager daemons/tools need for their work. 

.. _fortishield-keystore:

fortishield-keystore
==============

The fortishield-keystore increases the security of sensitive information, storing in it any information that the Fortishield manager requires for its correct operation.

fortishield-keystore options
----------------------

+------------------------+---------------------------------------------------------+
| **-h**                 | Display the help message.                               |
+------------------------+---------------------------------------------------------+
| **-f <FAMILY>**        | Specifies the target column family for the insertion.   |
+------------------------+---------------------------------------------------------+
| **-k <KEY>**           | Specifies the key for the key-value pair.               |
+------------------------+---------------------------------------------------------+
| **-v <VALUE>**         | Specifies the value associated with the key.            |
+------------------------+---------------------------------------------------------+

Example
-------
* Set indexer's username and password:

.. code-block:: console

    # /var/ossec/bin/fortishield-keystore -f indexer -k username -v admin
    # /var/ossec/bin/fortishield-keystore -f indexer -k password -v admin
