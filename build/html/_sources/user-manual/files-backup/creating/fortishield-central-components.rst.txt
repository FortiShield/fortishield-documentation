.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to keep a backup of key files of your Fortishield central components installation.
  
Fortishield central components
========================

To create a backup of the central components of your Fortishield installation, follow these steps. Repeat them on every cluster node you want to back up. 

.. note::

   You need root user privileges to execute the commands below.

Preparing the backup
--------------------

#. Create the destination folder to store the files. For version control, add the date and time of the backup to the name of the folder.

   .. code-block:: console

      # bkp_folder=~/fortishield_files_backup/$(date +%F_%H:%M)
      # mkdir -p $bkp_folder && echo $bkp_folder

#. Save the host information.

   .. code-block:: console

      # cat /etc/*release* > $bkp_folder/host-info.txt
      # echo -e "\n$(hostname): $(hostname -I)" >> $bkp_folder/host-info.txt

Backing up the Fortishield server
---------------------------

#. Back up the Fortishield server data and configuration files.

   .. code-block:: console

      # rsync -aREz \
      /etc/filebeat/ \
      /etc/postfix/ \
      /var/ossec/api/configuration/ \
      /var/ossec/etc/client.keys \
      /var/ossec/etc/sslmanager* \
      /var/ossec/etc/ossec.conf \
      /var/ossec/etc/internal_options.conf \
      /var/ossec/etc/local_internal_options.conf \
      /var/ossec/etc/rules/local_rules.xml \
      /var/ossec/etc/decoders/local_decoder.xml \
      /var/ossec/etc/shared/ \
      /var/ossec/logs/ \
      /var/ossec/queue/agentless/ \
      /var/ossec/queue/agents-timestamp \
      /var/ossec/queue/fts/ \
      /var/ossec/queue/rids/ \
      /var/ossec/stats/ \
      /var/ossec/var/multigroups/ $bkp_folder

#. If present, back up certificates and additional configuration files.

   .. code-block:: console

      # rsync -aREz \
      /var/ossec/etc/*.pem \
      /var/ossec/etc/authd.pass $bkp_folder
   
#. Back up your custom files. If you have custom active responses, CDB lists, integrations, or wodles, adapt the following command accordingly.

   .. code-block:: console

      # rsync -aREz \
      /var/ossec/active-response/bin/<custom_AR_script> \
      /var/ossec/etc/lists/<user_cdb_list>.cdb \
      /var/ossec/integrations/<custom_integration_script> \
      /var/ossec/wodles/<custom_wodle_script> $bkp_folder

#. Stop the Fortishield manager service to prevent modification attempts while copying the Fortishield databases.

   .. include:: /_templates/common/stop_manager.rst

#. Back up the Fortishield databases. They hold collected data from agents.

   .. code-block:: console

      # rsync -aREz \
      /var/ossec/queue/db/ $bkp_folder

#. Start the Fortishield manager service.

   .. include:: /_templates/common/start_manager.rst

Backing up the Fortishield indexer and dashboard
------------------------------------------

#. Back up the Fortishield indexer certificates and configuration files.

   .. code-block:: console

      # rsync -aREz \
      /etc/fortishield-indexer/certs/ \
      /etc/fortishield-indexer/jvm.options \
      /etc/fortishield-indexer/jvm.options.d \
      /etc/fortishield-indexer/log4j2.properties \
      /etc/fortishield-indexer/opensearch.yml \
      /etc/fortishield-indexer/opensearch.keystore \
      /etc/fortishield-indexer/opensearch-observability/ \
      /etc/fortishield-indexer/opensearch-reports-scheduler/ \
      /etc/fortishield-indexer/opensearch-security/ \
      /usr/lib/sysctl.d/fortishield-indexer.conf $bkp_folder

#. Back up the Fortishield dashboard certificates and configuration files.

   .. code-block:: console

      # rsync -aREz \
      /etc/fortishield-dashboard/certs/ \
      /etc/fortishield-dashboard/opensearch_dashboards.yml \
      /usr/share/fortishield-dashboard/config/opensearch_dashboards.keystore \
      /usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml $bkp_folder

#. If present, back up your downloads and custom images.

   .. code-block:: console

      # rsync -aREz \
      /usr/share/fortishield-dashboard/data/fortishield/downloads/ \
      /usr/share/fortishield-dashboard/plugins/fortishield/public/assets/custom/images/ $bkp_folder

.. note::

   While you're already backing up alert files, consider backing up the cluster indices and state as well. State includes cluster settings, node information, index metadata, and shard allocation.

Check the backup
----------------

#. Verify that the Fortishield manager is active and list all the backed up files:  

   .. tabs::

      .. group-tab:: Systemd

         .. code-block:: console

            # systemctl status fortishield-manager

      .. group-tab:: SysV init

         .. code-block:: console

            # service fortishield-manager status

   .. code-block:: console

      # find $bkp_folder -type f | sed "s|$bkp_folder/||" | less
