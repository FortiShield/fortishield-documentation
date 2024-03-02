.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: The Fortishield server is in charge of analyzing the data received from the Fortishield agents. Install the Fortishield server in a single-node or multi-node configuration according to your environment needs.

Installing the Fortishield server step by step
========================================

Install and configure the Fortishield server as a single-node or multi-node cluster following step-by-step instructions. The Fortishield server is a central component that includes the Fortishield manager and Filebeat. The Fortishield manager collects and analyzes data from the deployed Fortishield agents. It triggers alerts when threats or anomalies are detected. Filebeat securely forwards alerts and archived events to the Fortishield indexer.

The installation process is divided into two stages.

#. Fortishield server node installation

#. Cluster configuration for multi-node deployment

.. note:: You need root user privileges to run all the commands described below.

1. Fortishield server node installation
----------------------------------
.. raw:: html

  <div class="accordion-section open">

Adding the Fortishield repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    If you are installing the Fortishield server on the same host as the Fortishield indexer, you may skip these steps as you may have added the Fortishield repository already.

  ..
    Add the Fortishield repository to download the official Fortishield packages. As an alternative, you can download the Fortishield packages directly from :doc:`../packages-list`.

  .. tabs::


    .. group-tab:: Yum


      .. include:: /_templates/installations/common/yum/add-repository.rst



    .. group-tab:: APT


      .. include:: /_templates/installations/common/deb/add-repository.rst




Installing the Fortishield manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Install the Fortishield manager package.

     .. tabs::

        .. group-tab:: Yum

           .. code-block:: console

              # yum -y install fortishield-manager|FORTISHIELD_MANAGER_RPM_PKG_INSTALL|

        .. group-tab:: APT

           .. code-block:: console

              # apt-get -y install fortishield-manager|FORTISHIELD_MANAGER_DEB_PKG_INSTALL|

  #. Enable and start the Fortishield manager service.

      .. include:: /_templates/installations/fortishield/common/enable_fortishield_manager_service.rst


  #. Run the following command to verify the Fortishield manager status.

      .. include:: /_templates/installations/fortishield/common/check_fortishield_manager.rst

  #. Save the Fortishield indexer username and password into the Fortishield manager keystore using the fortishield-keystore tool: 

    .. code-block:: console

       # /var/ossec/bin/fortishield-keystore -f indexer -k username -v <INDEXER_USERNAME>
       # /var/ossec/bin/fortishield-keystore -f indexer -k password -v <INDEXER_PASSWORD>   

    .. note:: The default step-by-step installation credentials are ``admin``:``admin``

.. _fortishield_server_multi_node_filebeat:

Installing Filebeat
^^^^^^^^^^^^^^^^^^^

  #. Install the Filebeat package.

      .. tabs::


        .. group-tab:: Yum


          .. include:: /_templates/installations/filebeat/common/yum/install_filebeat.rst



        .. group-tab:: APT


          .. include:: /_templates/installations/filebeat/common/apt/install_filebeat.rst



Configuring Filebeat
^^^^^^^^^^^^^^^^^^^^

  #. Download the preconfigured Filebeat configuration file.

      .. code-block:: console

        # curl -so /etc/filebeat/filebeat.yml https://packages.fortishield.com/|FORTISHIELD_CURRENT_MINOR|/tpl/fortishield/filebeat/filebeat.yml


  #. Edit the ``/etc/filebeat/filebeat.yml`` configuration file and replace the following value:

     .. include:: /_templates/installations/filebeat/opensearch/configure_filebeat.rst

  #. Create a Filebeat keystore to securely store authentication credentials.

      .. code-block:: console

        # filebeat keystore create

  #. Add the default username and password ``admin``:``admin`` to the secrets keystore.

      .. code-block:: console

        # echo admin | filebeat keystore add username --stdin --force
        # echo admin | filebeat keystore add password --stdin --force

  #. Download the alerts template for the Fortishield indexer.

     .. code-block:: console

        # curl -so /etc/filebeat/fortishield-template.json https://raw.githubusercontent.com/fortishield/fortishield/v|FORTISHIELD_CURRENT|/extensions/elasticsearch/7.x/fortishield-template.json
        # chmod go+r /etc/filebeat/fortishield-template.json

  #. Install the Fortishield module for Filebeat.

      .. code-block:: console

        # curl -s https://packages.fortishield.com/4.x/filebeat/fortishield-filebeat-0.4.tar.gz | tar -xvz -C /usr/share/filebeat/module

Deploying certificates
^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    Make sure that a copy of the ``fortishield-certificates.tar`` file, created during the initial configuration step, is placed in your working directory.

  #. Replace ``<server-node-name>`` with your Fortishield server node certificate name, the same one used in ``config.yml`` when creating the certificates. Then, move the certificates to their corresponding location.

      .. include:: /_templates/installations/filebeat/opensearch/copy_certificates_filebeat_fortishield_cluster.rst


Starting the Filebeat service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Enable and start the Filebeat service.

      .. include:: /_templates/installations/filebeat/common/enable_filebeat.rst

  #. Run the following command to verify that Filebeat is successfully installed.

     .. code-block:: console

        # filebeat test output

     Expand the output to see an example response.

     .. code-block:: none
          :class: output accordion-output

          elasticsearch: https://127.0.0.1:9200...
            parse url... OK
            connection...
              parse host... OK
              dns lookup... OK
              addresses: 127.0.0.1
              dial up... OK
            TLS...
              security: server's certificate chain verification is enabled
              handshake... OK
              TLS version: TLSv1.3
              dial up... OK
            talk to server... OK
            version: 7.10.2


Your Fortishield server node is now successfully installed. Repeat this stage of the installation process for every Fortishield server node in your Fortishield cluster, then proceed with configuring the Fortishield cluster. If you want a Fortishield server single-node cluster, everything is set and you can proceed directly with :doc:`../fortishield-dashboard/step-by-step`.

2. Cluster configuration for multi-node deployment
--------------------------------------------------
.. raw:: html

  <div class="accordion-section">

After completing the installation of the Fortishield server on every node, you need to configure one server node only as the master and the rest as workers.

.. _fortishield_server_master_node:

Configuring the Fortishield server master node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Edit the following settings in the ``/var/ossec/etc/ossec.conf`` configuration file.

      .. include:: /_templates/installations/manager/configure_fortishield_master_node.rst

  #. Restart the Fortishield manager.

      .. include:: /_templates/installations/manager/restart_fortishield_manager.rst

.. _fortishield_server_worker_nodes:

Configuring the Fortishield server worker nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. .. include:: /_templates/installations/manager/configure_fortishield_worker_node.rst

  #. Restart the Fortishield manager.

      .. include:: /_templates/installations/manager/restart_fortishield_manager.rst

  Repeat these configuration steps for every Fortishield server worker node in your cluster.

Testing Fortishield server cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To verify that the Fortishield cluster is enabled and all the nodes are connected, execute the following command:

  .. code-block:: console

    # /var/ossec/bin/cluster_control -l

An example output of the command looks as follows:

  .. code-block:: none
    :class: output

      NAME         TYPE    VERSION  ADDRESS
      master-node  master  |FORTISHIELD_CURRENT|   10.0.0.3
      worker-node1 worker  |FORTISHIELD_CURRENT|   10.0.0.4
      worker-node2 worker  |FORTISHIELD_CURRENT|   10.0.0.5

Note that ``10.0.0.3``, ``10.0.0.4``, ``10.0.0.5`` are example IPs.

Next steps
----------

The Fortishield server installation is now complete, and you can proceed with :doc:`../fortishield-dashboard/step-by-step`.

If you want to uninstall the Fortishield server, see :ref:`uninstall_server`.
