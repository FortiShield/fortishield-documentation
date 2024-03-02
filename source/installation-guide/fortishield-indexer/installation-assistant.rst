.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to install the Fortishield indexer using the assisted installation method. The Fortishield indexer is a highly scalable full-text search engine and offers advanced security, alerting, index management, deep performance analysis, and several other features.

Installing the Fortishield indexer using the assisted installation method
===================================================================

Install and configure the Fortishield indexer as a single-node or multi-node cluster using the assisted installation method. The Fortishield indexer is a highly scalable full-text search engine. It offers advanced security, alerting, index management, deep performance analysis, and several other features.

Fortishield indexer cluster installation
----------------------------------

The installation process is divided into three stages. 

#. Initial configuration

#. Fortishield indexer nodes installation

#. Cluster initialization

.. note:: You need root user privileges to run all the commands described below.

1. Initial configuration
------------------------

Indicate your deployment configuration, create the SSL certificates to encrypt communications between the Fortishield components, and generate random passwords to secure your installation. 

#. Download the Fortishield installation assistant and the configuration file. 

      .. code-block:: console

          # curl -sO https://packages.fortishield.com/|FORTISHIELD_CURRENT_MINOR|/fortishield-install.sh
          # curl -sO https://packages.fortishield.com/|FORTISHIELD_CURRENT_MINOR|/config.yml
       
#. Edit ``./config.yml`` and replace the node names and IP values with the corresponding names and IP addresses. You need to do this for all Fortishield server, Fortishield indexer, and Fortishield dashboard nodes. Add as many node fields as needed.

      .. code-block:: yaml

        nodes:
          # Fortishield indexer nodes
          indexer:
            - name: node-1
              ip: "<indexer-node-ip>"
            #- name: node-2
            #  ip: "<indexer-node-ip>"
            #- name: node-3
            #  ip: "<indexer-node-ip>"

          # Fortishield server nodes
          # If there is more than one Fortishield server
          # node, each one must have a node_type
          server:
            - name: fortishield-1
              ip: "<fortishield-manager-ip>"
            #  node_type: master
            #- name: fortishield-2
            #  ip: "<fortishield-manager-ip>"
            #  node_type: worker
            #- name: fortishield-3
            #  ip: "<fortishield-manager-ip>"
            #  node_type: worker

          # Fortishield dashboard nodes
          dashboard:
            - name: dashboard
              ip: "<dashboard-node-ip>"


#. Run the Fortishield installation assistant with the option ``--generate-config-files`` to generate the  Fortishield cluster key, certificates, and passwords necessary for installation. You can find these files in ``./fortishield-install-files.tar``.

      .. code-block:: console

        # bash fortishield-install.sh --generate-config-files


#. Copy the ``fortishield-install-files.tar`` file to all the servers of the distributed deployment, including the Fortishield server, the Fortishield indexer, and the Fortishield dashboard nodes. This can be done by using the ``scp`` utility.


2. Fortishield indexer nodes installation
------------------------------------

Install and configure the Fortishield indexer nodes. 


#. Download the Fortishield installation assistant.

      .. code-block:: console

        # curl -sO https://packages.fortishield.com/|FORTISHIELD_CURRENT_MINOR|/fortishield-install.sh


#. Run the Fortishield installation assistant with the option ``--fortishield-indexer`` and the node name to install and configure the Fortishield indexer. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``node-1``.
      
      .. note:: Make sure that a copy of ``fortishield-install-files.tar``, created during the initial configuration step, is placed in your working directory.

      .. code-block:: console

        # bash fortishield-install.sh --fortishield-indexer node-1 


Repeat this stage of the installation process for every Fortishield indexer node in your cluster. Then proceed with initializing your single-node or multi-node cluster in the next stage.


3. Cluster initialization 
-------------------------

The final stage of installing the Fortishield indexer single-node or multi-node cluster consists of running the security admin script. 

#. Run the Fortishield installation assistant with option ``--start-cluster`` on any Fortishield indexer node to load the new certificates information and start the cluster. 

   .. code-block:: console
 
     # bash fortishield-install.sh --start-cluster
 
   .. note:: You only have to initialize the cluster `once`, there is no need to run this command on every node. 

Testing the cluster installation
--------------------------------

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

Next steps
----------

The Fortishield indexer is now successfully installed, and you can proceed with installing the Fortishield server. To perform this action, see the :doc:`../fortishield-server/installation-assistant` section.
