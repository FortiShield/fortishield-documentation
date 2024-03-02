Install Fortishield components using the assistant
--------------------------------------------

Install and configure the different Fortishield components with the aid of the Fortishield installation assistant. 

.. note:: You need root user privileges to run all the commands described below.

Please, make sure that a copy of the ``fortishield-install-files.tar`` and ``fortishield-offline.tar.gz`` files, created during the initial configuration step, is placed in your working directory.

Installing the Fortishield indexer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install and configure the Fortishield indexer nodes. 


#. Run the assistant with the ``--offline-install`` to perform an offline installation. Use the option ``--fortishield-indexer`` and the node name to install and configure the Fortishield indexer. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``node-1``.
      
   .. code-block:: console

      # bash fortishield-install.sh --offline-install --fortishield-indexer node-1 

   Repeat this step for every Fortishield indexer node in your cluster. Then proceed with initializing your single-node or multi-node cluster in the next step.

#. Run the Fortishield installation assistant with option ``--start-cluster`` on any Fortishield indexer node to load the new certificates information and start the cluster. 

   .. code-block:: console
 
      # bash fortishield-install.sh --start-cluster
 
   .. note:: You only have to initialize the cluster `once`, there is no need to run this command on every node. 

Testing the cluster installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command to get the *admin* password:

   .. code-block:: console

      # tar -axf fortishield-install-files.tar fortishield-install-files/fortishield-passwords.txt -O | grep -P "\'admin\'" -A 1

#. Run the following command to confirm that the installation is successful. Replace ``<ADMIN_PASSWORD>`` with the password gotten from the output of the previous command. Replace ``<FORTISHIELD_INDEXER_IP>`` with the configured Fortishield indexer IP address:

   .. code-block:: console

      # curl -k -u admin:<ADMIN_PASSWORD> https://<FORTISHIELD_INDEXER_IP>:9200

   .. code-block:: none
      :class: output

      {
        "name" : "node-1",
        "cluster_name" : "fortishield-cluster",
        "cluster_uuid" : "095jEW-oRJSFKLz5wmo5PA",
        "version" : {
          "number" : "7.10.2",
          "build_type" : "rpm",
          "build_hash" : "db90a415ff2fd428b4f7b3f800a51dc229287cb4",
          "build_date" : "2023-06-03T06:24:25.112415503Z",
          "build_snapshot" : false,
          "lucene_version" : "9.6.0",
          "minimum_wire_compatibility_version" : "7.10.0",
          "minimum_index_compatibility_version" : "7.0.0"
        },
        "tagline" : "The OpenSearch Project: https://opensearch.org/"
      }

#. Replace ``<FORTISHIELD_INDEXER_IP>`` and ``<ADMIN_PASSWORD>``, and run the following command to check if the cluster is working correctly:

   .. code-block:: console

      # curl -k -u admin:<ADMIN_PASSWORD> https://<FORTISHIELD_INDEXER_IP>:9200/_cat/nodes?v

Installing the Fortishield server
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the assistant with the ``--offline-install`` to perform an offline installation. Use the option ``--fortishield-server`` followed by the node name to install the Fortishield server. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``fortishield-1``.
 
   .. code-block:: console
  
      # bash fortishield-install.sh --offline-install --fortishield-server fortishield-1

Your Fortishield server is now successfully installed. 

-  If you want a Fortishield server multi-node cluster, repeat this step on every Fortishield server node.
-  If you want a Fortishield server single-node cluster, everything is set and you can proceed directly with the next stage.

Installing the Fortishield dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the assistant with the ``--offline-install`` to perform an offline installation. Use the option ``--fortishield-dashboard`` and the node name to install and configure the Fortishield dashboard. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``dashboard``.
   
   .. code-block:: console

      # bash fortishield-install.sh --fortishield-dashboard dashboard

   The default Fortishield web user interface port is 443, used by the Fortishield dashboard. You can change this port using the optional parameter ``-p|--port <port_number>``. Some recommended ports are 8443, 8444, 8080, 8888, and 9000.

   Once the assistant finishes the installation, the output shows the access credentials and a message that confirms that the installation was successful.

   .. code-block:: none
      :emphasize-lines: 3,4          
    
      INFO: --- Summary ---
      INFO: You can access the web interface https://<fortishield-dashboard-ip>
         User: admin
         Password: <ADMIN_PASSWORD>

      INFO: Installation finished.

   You now have installed and configured Fortishield. All passwords generated by the Fortishield installation assistant can be found in the ``fortishield-passwords.txt`` file inside the ``fortishield-install-files.tar`` archive. To print them, run the following command:
   
   .. code-block:: console
   
      # tar -O -xvf fortishield-install-files.tar fortishield-install-files/fortishield-passwords.txt

#. Access the Fortishield web interface with your credentials. 

   -  URL: *https://<fortishield-dashboard-ip>*
   -  **Username**: *admin*
   -  **Password**: *<ADMIN_PASSWORD>*

   When you access the Fortishield dashboard for the first time, the browser shows a warning message stating that the certificate was not issued by a trusted authority. An exception can be added in the advanced options of the web browser. For increased security, the ``root-ca.pem`` file previously generated can be imported to the certificate manager of the browser instead. Alternatively, a certificate from a trusted authority can be configured. 
