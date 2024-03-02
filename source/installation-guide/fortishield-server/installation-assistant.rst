.. Copyright (C) 2015, Fortishield, Inc.

.. meta:: 
   :description: Learn how to install the Fortishield server using the assisted installation method. The Fortishield server analyzes the data received from the agents triggering alerts when it detects threats and anomalies. This central component includes the Fortishield manager and Filebeat. 

Installing the Fortishield server using the assisted installation method
==================================================================

Install the Fortishield server as a single-node or multi-node cluster using the assisted installation method. The Fortishield server analyzes the data received from the agents triggering alerts when it detects threats and anomalies. This central component includes the Fortishield manager and Filebeat.

Fortishield server cluster installation
---------------------------------

#. Download the Fortishield installation assistant.

   .. code-block:: console
   
       # curl -sO https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MINOR|/fortishield-install.sh

#. Run the Fortishield installation assistant with the option ``--fortishield-server`` followed by the node name to install the Fortishield server. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``fortishield-1``.
 
   .. note:: Make sure that a copy of the ``fortishield-install-files.tar``, created during the initial configuration step, is placed in your working directory.

   .. code-block:: console
  
       # bash fortishield-install.sh --fortishield-server fortishield-1


Your Fortishield server is now successfully installed. 

- If you want a Fortishield server single-node cluster, everything is set and you can proceed directly with :doc:`../fortishield-dashboard/installation-assistant`.
      
- If you want a Fortishield server multi-node cluster, repeat this process on every Fortishield server node.

Next steps
----------
  
The Fortishield server installation is now complete, and you can proceed with installing the Fortishield dashboard. To perform this action, see the :doc:`../fortishield-dashboard/installation-assistant` section.  
