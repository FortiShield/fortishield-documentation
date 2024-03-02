.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Check out the compatibility matrix of the upgrade process of the Fortishield server and other components.
  
Compatibility matrix
====================

When upgrading Fortishield there are specific compatibility requirements to take into consideration.

Fortishield central components and agents
-----------------------------------

The Fortishield central components must share the same version numbers down to the patch category for the correct operation. For example:

-  Fortishield manager |FORTISHIELD_CURRENT|, Fortishield indexer |FORTISHIELD_CURRENT|, and Fortishield dashboard |FORTISHIELD_CURRENT|. 

- The Fortishield indexer |FORTISHIELD_CURRENT| is compatible with Filebeat-OSS |FILEBEAT_LATEST|. 

The Fortishield manager version must always be **newer than or equal to**  the Fortishield agents versions. For example:

-  Fortishield manager |FORTISHIELD_CURRENT| and Fortishield agent 4.2.7
-  Fortishield manager |FORTISHIELD_CURRENT| and Fortishield agent |FORTISHIELD_CURRENT|

The Fortishield manager is also compatible with OSSEC agents but not all capabilities are available with them. 

.. note::

   Since Fortishield v4.6.0, we don't provide the Kibana plugin and Splunk app anymore. To integrate Fortishield with Elastic or Splunk, refer to our :doc:`/integrations-guide/index`.
