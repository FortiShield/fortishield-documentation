.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Follow this guide to migrate from Open Distro for Elasticsearch to the Fortishield indexer.
  
.. _migration_guide_indexer:

Migrating to the Fortishield indexer 
==============================

Follow this guide to migrate from Open Distro for Elasticsearch 1.13 to the Fortishield indexer. These instructions are intended for a standard Fortishield installation, you may need to make some changes to adapt them to your environment.

.. note:: You need root user privileges to run all the commands described below.

#. Disable shard allocation to prevent Elasticsearch from replicating shards as you shut down nodes. Replace ``<elasticsearch_IP>`` with your Elasticsearch IP address or hostname, and ``<username>:<password>`` with your Elasticsearch username and password.  

   .. code-block:: console

     curl -X PUT "https://<elasticsearch_IP>:9200/_cluster/settings" -u <username>:<password> -k -H 'Content-Type: application/json' -d'
     {
       "persistent": {
         "cluster.routing.allocation.enable": "primaries"
       }
     }
     '

#. Stop indexing, and perform a flush: indexing/searching should be stopped and _flush can be used to permanently store information into the index which will prevent any data loss during the upgrade.

   .. code-block:: console

        curl -X POST "https://<elasticsearch_IP>:9200/_flush/synced" -u <username>:<password> -k

#. Stop Filebeat.

      .. include:: /_templates/installations/basic/elastic/common/stop_filebeat.rst

#. Shutdown Elasticsearch. For distributed deployments, you can shut down a single node at a time: first data nodes and later master nodes.

      .. include:: /_templates/installations/basic/elastic/common/stop_elasticsearch.rst

#. Add the Fortishield repository. You can skip this step if the repository is already present and enabled on your server. 

    .. tabs::


      .. group-tab:: Yum


        .. include:: /_templates/installations/common/yum/add-repository.rst



      .. group-tab:: APT


        .. include:: /_templates/installations/common/deb/add-repository.rst




#. Install the Fortishield indexer. 

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum -y install fortishield-indexer|FORTISHIELD_INDEXER_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get -y install fortishield-indexer|FORTISHIELD_INDEXER_DEB_PKG_INSTALL|

#. Create the ``/etc/fortishield-indexer/certs`` directory, copy your old certificates to the new location and change ownership and permissions. Note that the ``admin.pem`` and ``admin-key.pem`` certificates do not exist on every Elasticsearch node.

   .. code-block:: console

       # mkdir /etc/fortishield-indexer/certs
       # cp /etc/elasticsearch/certs/elasticsearch-key.pem /etc/fortishield-indexer/certs/indexer-key.pem
       # cp /etc/elasticsearch/certs/elasticsearch.pem /etc/fortishield-indexer/certs/indexer.pem
       # cp /etc/elasticsearch/certs/admin.pem /etc/fortishield-indexer/certs/admin.pem
       # cp /etc/elasticsearch/certs/admin-key.pem /etc/fortishield-indexer/certs/admin-key.pem
       # cp /etc/elasticsearch/certs/root-ca.pem /etc/fortishield-indexer/certs/root-ca.pem
       # chown -R fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/certs/
       # chmod 500 /etc/fortishield-indexer/certs/
       # chmod 400 /etc/fortishield-indexer/certs/*


#. Move or copy your data to the new directories and change ownership. 

   .. code-block:: console

      # rm -rf /var/lib/fortishield-indexer/ /var/log/fortishield-indexer/
      # mv /var/lib/elasticsearch/ /var/lib/fortishield-indexer/
      # mv /var/log/elasticsearch/ /var/log/fortishield-indexer/
      # chown fortishield-indexer:fortishield-indexer -R /var/log/fortishield-indexer/
      # chown fortishield-indexer:fortishield-indexer -R /var/lib/fortishield-indexer/

   .. note::

      If you have the Open Distro for Elasticsearch performance analyzer plugin installed, change the ownership of the ``/dev/shm/performanceanalyzer/`` directory by running the following command: ``chown fortishield-indexer:fortishield-indexer -R /dev/shm/performanceanalyzer/``.

#. Port your settings from ``/etc/elasticsearch/elasticsearch.yml`` to ``/etc/fortishield-indexer/opensearch.yml``. Most settings use the same names.

   Take into account the following considerations: 

   #. At a minimum, specify ``cluster.name``, ``node.name``, ``discovery.seed_hosts``, and ``cluster.initial_master_nodes``.

   #. Editing the ``path.data`` and the ``path.logs`` settings is not needed. The old data has been moved to the default Fortishield indexer paths in the previous step.

   #. Editing the certificates names and paths is not needed. The old certificates have been moved and renamed in a previous step.  
   
   #. If you were using the default Fortishield certificates, change the Organizational Unit (OU) from ``Fortishield`` to ``Docu``.  
      
       .. code-block:: yaml
         :emphasize-lines: 2,6
 
         plugins.security.authcz.admin_dn:
         - "CN=admin,OU=Docu,O=Fortishield,L=California,C=US"
         plugins.security.check_snapshot_restore_write_privileges: true
         plugins.security.enable_snapshot_restore_privilege: true
         plugins.security.nodes_dn:
         - "CN=node-1,OU=Docu,O=Fortishield,L=California,C=US"
         #- "CN=node-2,OU=Fortishield,O=Fortishield,L=California,C=US"
         #- "CN=node-3,OU=Fortishield,O=Fortishield,L=California,C=US"      

#. **Optional**. Port any custom configurations, for example, the  ``-Xms`` and ``-Xmx`` settings, from ``/etc/elasticsearch/jvm.options`` to ``/etc/fortishield-indexer/jvm.options``.

#. Enable and start the Fortishield indexer.

   .. include:: /_templates/installations/indexer/common/enable_indexer.rst

#. For multi-node deployments, repeat steps 4–10 until the upgrade is performed on all the nodes. 

#. Once all the nodes have been upgraded, restart Filebeat.   

   .. include:: /_templates/common/restart_filebeat.rst

#. Run the following command to verify that the communication between Filebeat and the Fortishield indexer is working as expected. 

     .. code-block:: console

        # filebeat test output
     
     .. code-block:: none
          :class: output
     
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

#. Monitor the health of the cluster as follows. Replace ``<Fortishield_indexer_IP>`` with your Fortishield indexer IP address or hostname, and ``<username>:<password>`` with your Elasticsearch username and password.  


   .. code-block:: console

     curl -X GET "https://<Fortishield_indexer_IP>:9200/_cluster/health?pretty" -u <username>:<password> -k

#. Re-enable shard allocation.

   .. code-block:: console

      curl -X PUT "https://<Fortishield_indexer_IP>:9200/_cluster/settings" -u <username>:<password> -k -H 'Content-Type: application/json' -d'
      {
        "persistent": {
          "cluster.routing.allocation.enable": null
        }
      }
      '

#. Verify that the indexed data in Open Distro is now searchable and indexable in the Fortishield indexer. You may enter the web interface, search for old data and verify that new alerts are coming in. 


#. Uninstall Open Distro for Elasticsearch on all nodes.


   .. tabs::
   
   
     .. group-tab:: Yum
   
   
       .. include:: /_templates/installations/elastic/yum/uninstall_elasticsearch.rst
   
   
   
     .. group-tab:: APT
   
   
       .. include:: /_templates/installations/elastic/deb/uninstall_elasticsearch.rst


Next steps
----------

Your cluster is now updated. To guarantee a correct operation of Fortishield, make sure to also migrate from Kibana to the Fortishield dashboard.  To learn more, see the :doc:`fortishield-dashboard` section.
