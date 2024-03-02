.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to upgrade the Fortishield indexer, server, and dashboard to the latest version available.

Fortishield central components
========================

This section guides you through the upgrade process of the Fortishield indexer, the Fortishield server, and the Fortishield dashboard. To migrate from Open Distro for Elasticsearch 1.13 to the Fortishield indexer and dashboard components, read the corresponding :doc:`/migration-guide/fortishield-indexer` and :doc:`/migration-guide/fortishield-dashboard` sections.

.. note:: You need root user privileges to run all the commands described below.

Preparing the upgrade
---------------------

In the case Fortishield is installed in a multi-node cluster configuration, repeat the following steps for every node.

#. Add the Fortishield repository. You can skip this step if the repository is already present and enabled on the node.

   .. tabs::


     .. group-tab:: Yum


       .. include:: /_templates/installations/common/yum/add-repository.rst



     .. group-tab:: APT


       .. include:: /_templates/installations/common/deb/add-repository.rst




#. Stop the Filebeat service and the Fortishield dashboard service if installed in the node.

   .. tabs::

      .. tab:: Systemd

         .. code-block:: console

            # systemctl stop filebeat
            # systemctl stop fortishield-dashboard

      .. tab:: SysV init

         .. code-block:: console

            # service filebeat stop
            # service fortishield-dashboard stop

Upgrading the Fortishield indexer
---------------------------

.. note::

   Note that this upgrade process doesn't update plugins installed manually. Outdated plugins might cause the upgrade to fail.

   To ensure compatibility with the latest Fortishield indexer and Fortishield dashboard, please update manually installed plugins accordingly. For additional information, check the `distribution matrix <https://github.com/fortishield/fortishield-packages/tree/v|FORTISHIELD_CURRENT|#distribution-version-matrix>`__.

In the case of having a Fortishield indexer cluster with multiple nodes, the cluster will remain available throughout the upgrading process. This rolling upgrade allows shutting down one Fortishield indexer node at a time for minimal disruption of service. Repeat these steps for every Fortishield indexer node.

.. note::

   -  Replace ``<FORTISHIELD_INDEXER_IP_ADDRESS>``, ``<username>``, and ``<password>`` before running the commands below.

#. Disable shard allocation.

   .. code-block:: bash
   
      curl -X PUT "https://<FORTISHIELD_INDEXER_IP_ADDRESS>:9200/_cluster/settings"  -u <username>:<password> -k -H 'Content-Type: application/json' -d'
      {
        "persistent": {
          "cluster.routing.allocation.enable": "primaries"
        }
      }
      '

#. Stop non-essential indexing and perform a synced flush.

   .. code-block:: console

      # curl -X POST "https://<FORTISHIELD_INDEXER_IP_ADDRESS>:9200/_flush/synced" -u <username>:<password> -k

#. Shut down the Fortishield indexer in the node.

   .. tabs::

      .. tab:: Systemd

         .. code-block:: console

            # systemctl stop fortishield-indexer

      .. tab:: SysV init

         .. code-block:: console

            # service fortishield-indexer stop

#. Upgrade the Fortishield indexer to the latest version.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum upgrade fortishield-indexer|FORTISHIELD_INDEXER_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get install fortishield-indexer|FORTISHIELD_INDEXER_DEB_PKG_INSTALL|

#. Restart the service.

   .. include:: /_templates/installations/indexer/common/enable_indexer.rst

#. Check that the newly-upgraded node joins the cluster.

   .. code-block:: console

      # curl -k -u <username>:<password> https://<FORTISHIELD_INDEXER_IP_ADDRESS>:9200/_cat/nodes?v

#. Re-enable shard allocation.

   .. code-block:: bash

      curl -X PUT "https://<FORTISHIELD_INDEXER_IP_ADDRESS>:9200/_cluster/settings" -u <username>:<password> -k -H 'Content-Type: application/json' -d'
      {
        "persistent": {
          "cluster.routing.allocation.enable": "all"
        }
      }
      '

#. Check again the status of the cluster to see if shard allocation has finished.

   .. code-block:: console

      # curl -k -u <username>:<password> https://<FORTISHIELD_INDEXER_IP_ADDRESS>:9200/_cat/nodes?v

#. If you're upgrading from a version earlier than 4.8.0, run the Fortishield indexer ``indexer-init.sh`` script on `any` Fortishield indexer node to re-initialize the cluster. Find more information in :doc:`/user-manual/fortishield-indexer/index-life-management`.

   -  If there is a rollover policy in use, your new policy needs a higher priority value to take precedence over it. Add ``-P <CUSTOM_PRIORITY_VALUE>`` into the command below to set a custom priority value.
      
   .. code-block:: console

      # bash /usr/share/fortishield-indexer/bin/indexer-init.sh -i <FORTISHIELD_INDEXER_IP_ADDRESS> -p <password>

   .. note::

      The policy will be applied only to new indices and not to existing ones. To rotate the current write index managed by the previous policy and start applying the new one, use the ``POST <alias>/_rollover`` endpoint. For example: ``POST fortishield-alerts/_rollover``

.. _upgrading_fortishield_server:

Upgrading the Fortishield server
--------------------------

When upgrading a multi-node Fortishield manager cluster, run the upgrade in every node to make all the Fortishield manager nodes join the cluster. Start with the master node to reduce server downtime.

   .. note:: Upgrading from Fortishield 4.2.x or lower creates the ``fortishield`` operating system user and group to replace ``ossec``. To avoid upgrade conflicts, make sure that the ``fortishield`` user and group are not present in your operating system.

#. Upgrade the Fortishield manager to the latest version.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum upgrade fortishield-manager|FORTISHIELD_MANAGER_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get install fortishield-manager|FORTISHIELD_MANAGER_DEB_PKG_INSTALL|

   .. note::

      If the ``/var/ossec/etc/ossec.conf`` configuration file was modified, it will not be replaced by the upgrade. You will therefore have to add the settings of the new capabilities manually. More information can be found in :doc:`/user-manual/index`.


#. Download the Fortishield module for Filebeat:

    .. code-block:: console

      # curl -s https://packages.fortishield.com/4.x/filebeat/fortishield-filebeat-0.4.tar.gz | sudo tar -xvz -C /usr/share/filebeat/module


#. Download the alerts template:

    .. code-block:: console

      # curl -so /etc/filebeat/fortishield-template.json https://raw.githubusercontent.com/fortishield/fortishield/v|FORTISHIELD_CURRENT|/extensions/elasticsearch/7.x/fortishield-template.json
      # chmod go+r /etc/filebeat/fortishield-template.json

#. Restart Filebeat:

    .. include:: /_templates/installations/basic/elastic/common/enable_filebeat.rst

#. Upload the new Fortishield template and pipelines for Filebeat.

   .. code-block:: console

      # filebeat setup --pipelines
      # filebeat setup --index-management -E output.logstash.enabled=false

Upgrading the Fortishield dashboard
-----------------------------

.. note::

   Note that this upgrade process doesn't update plugins installed manually. Outdated plugins might cause the upgrade to fail.

   To ensure compatibility with the latest Fortishield indexer and Fortishield dashboard, please update manually installed plugins accordingly. For additional information, check the `distribution matrix <https://github.com/fortishield/fortishield-packages/tree/v|FORTISHIELD_CURRENT|#distribution-version-matrix>`__.

#. Upgrade the Fortishield dashboard.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum upgrade fortishield-dashboard|FORTISHIELD_DASHBOARD_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get install fortishield-dashboard|FORTISHIELD_DASHBOARD_DEB_PKG_INSTALL|

#. Restart the Fortishield dashboard:

    .. include:: /_templates/installations/dashboard/enable_dashboard.rst



Next steps
----------

The Fortishield server, indexer, and dashboard are now successfully upgraded. The next step consists in upgrading the Fortishield agents. Follow the instructions in:

-  :doc:`Upgrading the Fortishield agent </upgrade-guide/fortishield-agent/index>`.
