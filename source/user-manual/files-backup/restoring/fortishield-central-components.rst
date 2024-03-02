.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to restore a backup of key files of your Fortishield central components installation.
  
Fortishield central components
========================

Perform the following actions to restore the Fortishield central components data, depending on your deployment type.

.. note::
   
   For a multi-node setup, there should be a backup file for each node within the cluster. You need root user privileges to execute the commands below.

Single-node data restoration
----------------------------

You need to have a new installation of Fortishield. Follow the :doc:`/quickstart` guide to perform a fresh installation of the Fortishield central components on a new server.

The actions below will guide you through the data restoration process for a single-node deployment.

Preparing the data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Compress the files generated after performing Fortishield files backup and transfer them to the new server:

   .. code-block:: console

      # tar -cvzf fortishield_central_components.tar.gz ~/fortishield_files_backup/

#. Move the compressed file to the root ``/`` directory of your node:

   .. code-block:: console

      # mv fortishield_central_components.tar.gz /
      # cd /

#. Decompress the backup files and change the current working directory to the directory based on the date and time of the backup files:

   .. code-block:: console

      # tar -xzvf fortishield_central_components.tar.gz
      # cd ~/fortishield_files_backup/<DATE_TIME>

Restoring Fortishield indexer files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following steps to restore the Fortishield indexer files on the new server.

#. Stop the Fortishield indexer to prevent any modifications to the Fortishield indexer files during the restoration process:

   .. code-block:: console

      # systemctl stop fortishield-indexer

#. Restore the Fortishield indexer configuration files and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp etc/fortishield-indexer/jvm.options /etc/fortishield-indexer/jvm.options
      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/jvm.options
      # sudo cp -r etc/fortishield-indexer/jvm.options.d/* /etc/fortishield-indexer/jvm.options.d/
      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/jvm.options.d
      # sudo cp etc/fortishield-indexer/log4j2.properties /etc/fortishield-indexer/log4j2.properties
      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/log4j2.properties
      # sudo cp etc/fortishield-indexer/opensearch.keystore /etc/fortishield-indexer/opensearch.keystore
      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/opensearch.keystore
      # sudo cp -r etc/fortishield-indexer/opensearch-observability/* /etc/fortishield-indexer/opensearch-observability/
      # chown -R fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/opensearch-observability/
      # sudo cp -r etc/fortishield-indexer/opensearch-reports-scheduler/* /etc/fortishield-indexer/opensearch-reports-scheduler/
      # chown -R fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/opensearch-reports-scheduler/
      # sudo cp usr/lib/sysctl.d/fortishield-indexer.conf /usr/lib/sysctl.d/fortishield-indexer.conf

#. Start the Fortishield indexer service:

   .. code-block:: console

      # systemctl start fortishield-indexer

.. _restoring-server-single-node:

Restoring Fortishield server files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following steps to restore the Fortishield server files on the new server.

#. Stop the Fortishield manager and Filebeat to prevent any modification to the Fortishield server files during the restore process:

   .. code-block:: console

      # systemctl stop filebeat
      # systemctl stop fortishield-manager

#. Copy the Fortishield server data and configuration files, and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp etc/filebeat/filebeat.reference.yml /etc/filebeat/
      # sudo cp etc/filebeat/fields.yml /etc/filebeat/
      # sudo cp -r etc/filebeat/modules.d/* /etc/filebeat/modules.d/
      # sudo cp -r etc/postfix/* /etc/postfix/
      # sudo cp var/ossec/etc/client.keys /var/ossec/etc/
      # chown root:fortishield /var/ossec/etc/client.keys
      # sudo cp -r var/ossec/etc/sslmanager* /var/ossec/etc/
      # sudo cp var/ossec/etc/ossec.conf /var/ossec/etc/
      # chown root:fortishield /var/ossec/etc/ossec.conf
      # sudo cp var/ossec/etc/internal_options.conf /var/ossec/etc/
      # chown root:fortishield /var/ossec/etc/internal_options.conf
      # sudo cp var/ossec/etc/local_internal_options.conf /var/ossec/etc/
      # chown root:fortishield /var/ossec/etc/local_internal_options.conf
      # sudo cp -r var/ossec/etc/rules/* /var/ossec/etc/rules/
      # chown -R fortishield:fortishield /var/ossec/etc/rules/
      # sudo cp -r var/ossec/etc/decoders/* /var/ossec/etc/decoders
      # chown -R fortishield:fortishield /var/ossec/etc/decoders/
      # sudo cp -r var/ossec/etc/shared/* /var/ossec/etc/shared/
      # chown -R fortishield:fortishield /var/ossec/etc/shared/
      # chown root:fortishield /var/ossec/etc/shared/ar.conf
      # sudo cp -r var/ossec/logs/* /var/ossec/logs/
      # chown -R fortishield:fortishield /var/ossec/logs/
      # sudo cp -r var/ossec/queue/agentless/*  /var/ossec/queue/agentless/
      # chown -R fortishield:fortishield /var/ossec/queue/agentless/
      # sudo cp var/ossec/queue/agents-timestamp /var/ossec/queue/
      # chown root:fortishield /var/ossec/queue/agents-timestamp
      # sudo cp -r var/ossec/queue/fts/* /var/ossec/queue/fts/
      # chown -R fortishield:fortishield /var/ossec/queue/fts/
      # sudo cp -r var/ossec/queue/rids/* /var/ossec/queue/rids/
      # chown -R fortishield:fortishield /var/ossec/queue/rids/
      # sudo cp -r var/ossec/stats/* /var/ossec/stats/ 
      # chown -R fortishield:fortishield /var/ossec/stats/ 
      # sudo cp -r var/ossec/var/multigroups/* /var/ossec/var/multigroups/
      # chown -R fortishield:fortishield /var/ossec/var/multigroups/

#. Restore certificates for Fortishield agent and Fortishield server communication, and additional configuration files if present:

   .. code-block:: console

      # sudo cp -r var/ossec/etc/*.pem /var/ossec/etc/
      # chown -R root:fortishield /var/ossec/etc/*.pem
      # sudo cp var/ossec/etc/authd.pass /var/ossec/etc/
      # chown -R root:fortishield /var/ossec/etc/authd.pass

#. Restore your custom files. If you have custom active response scripts, CDB lists, integrations, or wodles, adapt the following commands accordingly:

   .. code-block:: console

      # sudo cp var/ossec/active-response/bin/<CUSTOM_ACTIVE_RESPONSE_SCRIPT> /var/ossec/active-response/bin/
      # chown root:fortishield /var/ossec/active-response/bin/<CUSTOM_ACTIVE_RESPONSE_SCRIPT> 
      # sudo cp var/ossec/etc/lists/<USER_CDB_LIST>.cdb /var/ossec/etc/lists/
      # chown root:fortishield /var/ossec/etc/lists/<USER_CDB_LIST>.cdb 
      # sudo cp var/ossec/integrations/<CUSTOM_INTEGRATION_SCRIPT> /var/ossec/integrations/
      # chown root:fortishield /var/ossec/integrations/<CUSTOM_INTEGRATION_SCRIPT>
      # sudo cp var/ossec/wodles/<CUSTOM_WODLE_SCRIPT> /var/ossec/wodles/
      # chown root:fortishield /var/ossec/wodles/<CUSTOM_WODLE_SCRIPT>

#. Restore the Fortishield databases that contain collected data from the Fortishield agents:

   .. code-block:: console

      # sudo cp var/ossec/queue/db/* /var/ossec/queue/db/ 
      # chown -R fortishield:fortishield /var/ossec/queue/db/

#. Start the Filebeat service:

   .. code-block:: console

      # systemctl start filebeat

#. Start the Fortishield manager service:

   .. code-block:: console

      # systemctl start fortishield-manager

Restoring Fortishield dashboard files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following steps to restore Fortishield reports and custom images on the new server if you have any from your backup.

#. Restore your Fortishield reports using the following command:

   .. code-block:: console

      # mkdir -p /usr/share/fortishield-dashboard/data/fortishield/downloads/reports/
      # sudo cp -r usr/share/fortishield-dashboard/data/fortishield/downloads/reports/* /usr/share/fortishield-dashboard/data/fortishield/downloads/reports/ 
      # chown -R fortishield-dashboard:fortishield-dashboard /usr/share/fortishield-dashboard/data/fortishield/downloads/

#. Navigate to **Indexer/dashboard management** > **App Settings** > **Custom branding** from the Fortishield dashboard and upload your custom images.

Restoring old logs
^^^^^^^^^^^^^^^^^^

Fortishield, by default, compresses logs that are older than a day. While performing old log restoration in the :ref:`restoring-server-single-node` section, the old logs remain compressed.

Perform the following actions on your Fortishield server to decompress these logs and index them in the new Fortishield indexer:

.. note::
   
   Restoring old logs will have a creation date of the day when the restoration is performed.

#. Create a Python script called ``recovery.py`` on your Fortishield server. This script decompresses all the old logs and stores them in the ``recovery.json`` file in the ``/tmp`` directory:

   .. code-block:: console

      # touch recovery.py

#. Add the following content to the ``recovery.py`` script:


   .. code-block:: python

      #!/usr/bin/env python

      import gzip
      import time
      import json
      import argparse
      import re
      import os
      from datetime import datetime
      from datetime import timedelta

      def log(msg):
          now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          final_msg = "{0} fortishield-reinjection: {1}".format(now_date, msg)
          print(final_msg)
          if log_file:
              f_log.write(final_msg + "\n")

      EPS_MAX = 400
      fortishield_path = '/var/ossec/'
      max_size=1
      log_file = None

      parser = argparse.ArgumentParser(description='Reinjection script')
      parser.add_argument('-eps','--eps', metavar='eps', type=int, required = False, help='Events per second.')
      parser.add_argument('-min', '--min_timestamp', metavar='min_timestamp', type=str, required = True, help='Min timestamp. Example: 2017-12-13T23:59:06')
      parser.add_argument('-max', '--max_timestamp', metavar='max_timestamp', type=str, required = True, help='Max timestamp. Example: 2017-12-13T23:59:06')
      parser.add_argument('-o', '--output_file', metavar='output_file', type=str, required = True, help='Output filename.')
      parser.add_argument('-log', '--log_file', metavar='log_file', type=str, required = False, help='Logs output')
      parser.add_argument('-w', '--fortishield_path', metavar='fortishield_path', type=str, required = False, help='Path to Fortishield. By default:/var/ossec/')
      parser.add_argument('-sz', '--max_size', metavar='max_size', type=float, required = False, help='Max output file size in Gb. Default: 1Gb. Example: 2.5')

      args = parser.parse_args()

      if args.log_file:
          log_file = args.log_file
          f_log = open(log_file, 'a+')


      if args.max_size:
          max_size = args.max_size

      if args.fortishield_path:
          fortishield_path = args.fortishield_path

      output_file = args.output_file

      #Gb to bytes
      max_bytes = int(max_size * 1024 * 1024 * 1024)

      if (max_bytes <= 0):
          log("Error: Incorrect max_size")
          exit(1)

      month_dict = ['Null','Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

      if args.eps:
          EPS_MAX = args.eps

      if EPS_MAX < 0:
          log("Error: incorrect EPS")
          exit(1)

      min_date = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T\\d\\d:\\d\\d:\\d\\d', args.min_timestamp)
      if min_date:
          min_year = int(min_date.group(1))
          min_month = int(min_date.group(2))
          min_day = int(min_date.group(3))
      else:
          log("Error: Incorrect min timestamp")
          exit(1)

      max_date = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T\\d\\d:\\d\\d:\\d\\d', args.max_timestamp)
      if max_date:
          max_year = int(max_date.group(1))
          max_month = int(max_date.group(2))
          max_day = int(max_date.group(3))
      else:
          log("Error: Incorrect max timestamp")
          exit(1)

      # Converting timestamp args to datetime
      min_timestamp = datetime.strptime(args.min_timestamp, '%Y-%m-%dT%H:%M:%S')
      max_timestamp = datetime.strptime(args.max_timestamp, '%Y-%m-%dT%H:%M:%S')

      chunk = 0
      written_alerts = 0
      trimmed_alerts = open(output_file, 'w')

      max_time=datetime(max_year, max_month, max_day)
      current_time=datetime(min_year, min_month, min_day)

      while current_time <= max_time: 
          alert_file = "{0}logs/alerts/{1}/{2}/ossec-alerts-{3:02}.json.gz".format(fortishield_path,current_time.year,month_dict[current_time.month],current_time.day)

          if os.path.exists(alert_file):
              daily_alerts = 0
              compressed_alerts = gzip.open(alert_file, 'r')
              log("Reading file: "+ alert_file)
              for line in compressed_alerts:
                  # Transform line to json object
                  try:
                      line_json = json.loads(line.decode("utf-8", "replace"))

                      # Remove unnecessary part of the timestamp
                      string_timestamp = line_json['timestamp'][:19]

                      # Ensure timestamp integrity
                      while len(line_json['timestamp'].split("+")[0]) < 23:
                          line_json['timestamp'] = line_json['timestamp'][:20] + "0" + line_json['timestamp'][20:]

                      # Get the timestamp readable
                      event_date = datetime.strptime(string_timestamp, '%Y-%m-%dT%H:%M:%S')

                      # Check the timestamp belongs to the selected range
                      if (event_date <= max_timestamp and event_date >= min_timestamp):
                          chunk+=1
                          trimmed_alerts.write(json.dumps(line_json))
                          trimmed_alerts.write("\n")
                          trimmed_alerts.flush()
                          daily_alerts += 1
                          if chunk >= EPS_MAX:
                              chunk = 0
                              time.sleep(2)
                          if os.path.getsize(output_file) >= max_bytes:
                              trimmed_alerts.close()
                              log("Output file reached max size, setting it to zero and restarting")
                              time.sleep(EPS_MAX/100)
                              trimmed_alerts = open(output_file, 'w')

                  except ValueError as e:
                      print("Oops! Something went wrong reading: {}".format(line))
                      print("This is the error: {}".format(str(e)))

              compressed_alerts.close()
              log("Extracted {0} alerts from day {1}-{2}-{3}".format(daily_alerts,current_time.day,month_dict[current_time.month],current_time.year))
          else:
              log("Couldn't find file {}".format(alert_file))

          #Move to next file
          current_time += timedelta(days=1)

      trimmed_alerts.close()

   While you run the ``recovery.py`` script, you need to consider the following parameters:

   .. code-block:: none

      usage: recovery.py [-h] [-eps eps] -min min_timestamp -max max_timestamp -o
                            output_file [-log log_file] [-w fortishield_path]
                            [-sz max_size]

        -eps eps, --eps eps   Events per second. Default: 400
        -min min_timestamp, --min_timestamp min_timestamp
                              Min timestamp. Example: 2019-11-13T08:42:17
        -max max_timestamp, --max_timestamp max_timestamp
                              Max timestamp. Example: 2019-11-13T23:59:06
        -o output_file, --output_file output_file
                              Alerts output file.
        -log log_file, --log_file log_file
                              Logs output.
        -w fortishield_path, --fortishield_path fortishield_path
                              Path to Fortishield. By default:/var/ossec/
        -sz max_size, --max_size max_size
                              Max output file size in Gb. Default: 1Gb. Example: 2.5

#. Run the command below to make the ``recovery.py`` script executable:

   .. code-block:: console

      # chmod +x recovery.py

#. Execute the script using ``nohup`` command in the background to keep it running after the session is closed. It may take time depending on the size of the old logs.

   Usage example:

   .. code-block:: console

      # nohup ./recovery.py -eps 500 -min 2023-06-10T00:00:00 -max 2023-06-18T23:59:59 -o /tmp/recovery.json -log ./recovery.log -sz 2.5 &

#. Add the ``/tmp/recovery.json`` path to the Fortishield Filebeat module ``/usr/share/filebeat/module/fortishield/alerts/manifest.yml`` so that Filebeat sends the old alerts to the Fortishield indexer for indexing: 


   .. code-block:: yaml
      :emphasize-lines: 7

      module_version: 0.1

      var:
        - name: paths
          default:
            - /var/ossec/logs/alerts/alerts.json
            - /tmp/recovery.json
        - name: index_prefix
          default: fortishield-alerts-4.x-

      input: config/alerts.yml

      ingest_pipeline: ingest/pipeline.json

#. Restart Filebeat for the changes to take effect:

   .. code-block:: console

      # systemctl restart filebeat

Verifying data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the Fortishield dashboard, navigate to the **Threat Hunting**, **File Integrity Monitoring**, **Vulnerability Detection**, and any other modules to see if the data is restored successfully.

Multi-node data restoration
---------------------------

Perform the actions below to restore the Fortishield central components on their respective Fortishield nodes.

Preparing the data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Compress the files generated after performing :doc:`Fortishield files backup <../creating/fortishield-central-components>` and transfer them to the respective new servers:

   .. code-block:: console

      # tar -cvzf <SERVER_HOSTNAME>.tar.gz ~/fortishield_files_backup/ 

   Where:

   -  ``<SERVER_HOSTNAME>`` represents the current server name. Consider adding the naming convention, ``_indexer``, ``_server``, ``_dashboard`` if the current hostnames don’t specify them.

   .. note::
      
      Make sure that Fortishield indexer compressed files are transferred to the new Fortishield indexer nodes, Fortishield server compressed files are transferred to the new Fortishield server nodes, and Fortishield dashboard compressed files are transferred to the new Fortishield dashboard nodes.

#. Move the compressed file to the root ``/`` directory of each node:

   .. code-block:: console

      # mv <SERVER_HOSTNAME>.tar.gz /
      # cd /

#. Decompress the backup files and change the current working directory to the directory based on the date and time of the backup files:

   .. code-block:: console

      # tar -xzvf <SERVER_HOSTNAME>.tar.gz
      # cd ~/fortishield_files_backup/<DATE_TIME>

Restoring Fortishield indexer files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to have a new installation of Fortishield indexer. Follow the :doc:`Fortishield indexer - Installation guide </installation-guide/fortishield-indexer/index>` to perform a fresh Fortishield indexer installation.

Perform the following steps on each Fortishield indexer node.

#. Stop the Fortishield indexer to prevent any modification to the Fortishield indexer files during the restore process:

   .. code-block:: console

      # systemctl stop fortishield-indexer

#. Restore the Fortishield indexer configuration files, and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp etc/fortishield-indexer/jvm.options /etc/fortishield-indexer/jvm.options
      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/jvm.options
      # sudo cp etc/fortishield-indexer/jvm.options.d /etc/fortishield-indexer/jvm.options.d
      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/jvm.options.d
      # sudo cp etc/fortishield-indexer/log4j2.properties /etc/fortishield-indexer/log4j2.properties
      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/log4j2.properties
      # sudo cp etc/fortishield-indexer/opensearch.keystore /etc/fortishield-indexer/opensearch.keystore
      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/opensearch.keystore
      # sudo cp -r etc/fortishield-indexer/opensearch-observability/* /etc/fortishield-indexer/opensearch-observability/
      # chown -R fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/opensearch-observability/
      # sudo cp -r etc/fortishield-indexer/opensearch-reports-scheduler/* /etc/fortishield-indexer/opensearch-reports-scheduler/
      # chown -R fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/opensearch-reports-scheduler/
      # sudo cp usr/lib/sysctl.d/fortishield-indexer.conf /usr/lib/sysctl.d/fortishield-indexer.conf

#. Start the Fortishield indexer service:

   .. code-block:: console

      # systemctl start fortishield-indexer

.. _restoring-server-multi-node:

Restoring Fortishield server files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to have a new installation of a Fortishield server. Follow the :doc:`Fortishield server - Installation guide </installation-guide/fortishield-server/index>` to perform a multi-node Fortishield server installation. There will be at least one master node and one worker node as node types. Perform the steps below, considering your node type.

#. Stop the Fortishield manager and Filebeat to prevent any modification to the Fortishield server files during the restore process:

   .. code-block:: console

      # systemctl stop filebeat
      # systemctl stop fortishield-manager

#. Copy Fortishield server data and configuration files, and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp etc/filebeat/filebeat.reference.yml /etc/filebeat/
      # sudo cp etc/filebeat/fields.yml /etc/filebeat/
      # sudo cp -r etc/filebeat/modules.d/* /etc/filebeat/modules.d/
      # sudo cp -r etc/postfix/* /etc/postfix/
      # sudo cp var/ossec/etc/client.keys /var/ossec/etc/
      # chown root:fortishield /var/ossec/etc/client.keys
      # sudo cp -r var/ossec/etc/sslmanager* /var/ossec/etc/
      # sudo cp var/ossec/etc/ossec.conf /var/ossec/etc/
      # chown root:fortishield /var/ossec/etc/ossec.conf
      # sudo cp var/ossec/etc/internal_options.conf /var/ossec/etc/
      # chown root:fortishield /var/ossec/etc/internal_options.conf
      # sudo cp var/ossec/etc/local_internal_options.conf /var/ossec/etc/
      # chown root:fortishield /var/ossec/etc/local_internal_options.conf
      # sudo cp -r var/ossec/etc/rules/* /var/ossec/etc/rules/
      # chown -R fortishield:fortishield /var/ossec/etc/rules/
      # sudo cp -r var/ossec/etc/decoders/* /var/ossec/etc/decoders
      # chown -R fortishield:fortishield /var/ossec/etc/decoders/
      # sudo cp -r var/ossec/etc/shared/*  /var/ossec/etc/shared/
      # chown -R fortishield:fortishield /var/ossec/etc/shared/
      # chown root:fortishield /var/ossec/etc/shared/ar.conf
      # sudo cp -r var/ossec/logs/* /var/ossec/logs/
      # chown -R fortishield:fortishield /var/ossec/logs/
      # sudo cp -r var/ossec/queue/agentless/*  /var/ossec/queue/agentless/
      # chown -R fortishield:fortishield /var/ossec/queue/agentless/
      # sudo cp var/ossec/queue/agents-timestamp /var/ossec/queue/
      # chown root:fortishield /var/ossec/queue/agents-timestamp
      # sudo cp -r var/ossec/queue/fts/* /var/ossec/queue/fts/
      # chown -R fortishield:fortishield /var/ossec/queue/fts/
      # sudo cp -r var/ossec/queue/rids/* /var/ossec/queue/rids/
      # chown -R fortishield:fortishield /var/ossec/queue/rids/
      # sudo cp -r var/ossec/stats/* /var/ossec/stats/ 
      # chown -R fortishield:fortishield /var/ossec/stats/ 
      # sudo cp -r var/ossec/var/multigroups/* /var/ossec/var/multigroups/
      # chown -R fortishield:fortishield /var/ossec/var/multigroups/

#. Restore certificates for Fortishield agent and Fortishield server communication, and additional configuration files if present:

   .. code-block:: console

      # sudo cp -r var/ossec/etc/*.pem /var/ossec/etc/
      # chown -R root:fortishield /var/ossec/etc/*.pem
      # sudo cp var/ossec/etc/authd.pass /var/ossec/etc/
      # chown -R root:fortishield /var/ossec/etc/authd.pass

#. Restore your custom files. If you have custom active response scripts, CDB lists, integrations, or wodle commands, adapt the following commands accordingly:

   .. code-block:: console

      # sudo cp var/ossec/active-response/bin/<CUSTOM_AR_SCRIPT> /var/ossec/active-response/bin/
      # chown root:fortishield /var/ossec/active-response/bin/<CUSTOM_AR_SCRIPT> 
      # sudo cp var/ossec/etc/lists/<USER_CDB_LIST>.cdb /var/ossec/etc/lists/
      # chown root:fortishield /var/ossec/etc/lists/<USER_CDB_LIST>.cdb 
      # sudo cp var/ossec/integrations/<CUSTOM_INTEGRATION_SCRIPT> /var/ossec/integrations/
      # chown root:fortishield /var/ossec/integrations/<CUSTOM_INTEGRATION_SCRIPT>
      # sudo cp var/ossec/wodles/<CUSTOM_WODLE_SCRIPT> /var/ossec/wodles/
      # chown root:fortishield /var/ossec/wodles/<CUSTOM_WODLE_SCRIPT>

#. Restore the Fortishield databases that contain collected data from Fortishield agents:

   .. code-block:: console

      # sudo cp var/ossec/queue/db/* /var/ossec/queue/db/ 
      # chown -R root:fortishield /var/ossec/queue/db/

#. Start the Filebeat service:

   .. code-block:: console

      # systemctl start filebeat

#. Start the Fortishield manager service:

   .. code-block:: console

      # systemctl start fortishield-manager

Restoring Fortishield dashboard files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to have a new installation of the Fortishield dashboard. Follow :doc:`Fortishield dashboard - Installation guide </installation-guide/fortishield-dashboard/index>` to perform Fortishield dashboard installation.

Perform the following steps to restore Fortishield reports and custom images on the new server if you have any from your backup.

#. Restore your Fortishield reports using the following command:

   .. code-block:: console

      # mkdir -p /usr/share/fortishield-dashboard/data/fortishield/downloads/reports/
      # sudo cp -r usr/share/fortishield-dashboard/data/fortishield/downloads/reports/* /usr/share/fortishield-dashboard/data/fortishield/downloads/reports/ 
      # chown -R fortishield-dashboard:fortishield-dashboard /usr/share/fortishield-dashboard/data/fortishield/downloads/

#. Navigate to **Indexer/dashboard management** > **App Settings** > **Custom branding** from the Fortishield dashboard and upload your custom images.

Restoring old logs
^^^^^^^^^^^^^^^^^^

Fortishield, by default, compresses logs that are older than a day. While performing log restoration in the :ref:`restoring-server-multi-node` section, the old logs remain compressed.

Perform the following actions on both master and worker nodes of your Fortishield server to decompress the old logs and re-inject them for indexing to the Fortishield indexer.

.. note::
   
   Restoring old logs will have a creation date of the day when the restoration is performed.

#. Create a Python script called ``recovery.py`` on your Fortishield server. This script decompresses all the old logs and stores them in the ``recovery.json`` file in ``/tmp`` directory.

   .. code-block:: console

      # touch recovery.py

#. Add the following content to the ``recovery.py`` script:

   .. code-block:: python

      #!/usr/bin/env python

      import gzip
      import time
      import json
      import argparse
      import re
      import os
      from datetime import datetime
      from datetime import timedelta

      def log(msg):
          now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          final_msg = "{0} fortishield-reinjection: {1}".format(now_date, msg)
          print(final_msg)
          if log_file:
              f_log.write(final_msg + "\n")

      EPS_MAX = 400
      fortishield_path = '/var/ossec/'
      max_size=1
      log_file = None

      parser = argparse.ArgumentParser(description='Reinjection script')
      parser.add_argument('-eps','--eps', metavar='eps', type=int, required = False, help='Events per second.')
      parser.add_argument('-min', '--min_timestamp', metavar='min_timestamp', type=str, required = True, help='Min timestamp. Example: 2017-12-13T23:59:06')
      parser.add_argument('-max', '--max_timestamp', metavar='max_timestamp', type=str, required = True, help='Max timestamp. Example: 2017-12-13T23:59:06')
      parser.add_argument('-o', '--output_file', metavar='output_file', type=str, required = True, help='Output filename.')
      parser.add_argument('-log', '--log_file', metavar='log_file', type=str, required = False, help='Logs output')
      parser.add_argument('-w', '--fortishield_path', metavar='fortishield_path', type=str, required = False, help='Path to Fortishield. By default:/var/ossec/')
      parser.add_argument('-sz', '--max_size', metavar='max_size', type=float, required = False, help='Max output file size in Gb. Default: 1Gb. Example: 2.5')

      args = parser.parse_args()

      if args.log_file:
          log_file = args.log_file
          f_log = open(log_file, 'a+')


      if args.max_size:
          max_size = args.max_size

      if args.fortishield_path:
          fortishield_path = args.fortishield_path

      output_file = args.output_file

      #Gb to bytes
      max_bytes = int(max_size * 1024 * 1024 * 1024)

      if (max_bytes <= 0):
          log("Error: Incorrect max_size")
          exit(1)

      month_dict = ['Null','Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

      if args.eps:
          EPS_MAX = args.eps

      if EPS_MAX < 0:
          log("Error: incorrect EPS")
          exit(1)

      min_date = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T\\d\\d:\\d\\d:\\d\\d', args.min_timestamp)
      if min_date:
          min_year = int(min_date.group(1))
          min_month = int(min_date.group(2))
          min_day = int(min_date.group(3))
      else:
          log("Error: Incorrect min timestamp")
          exit(1)

      max_date = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T\\d\\d:\\d\\d:\\d\\d', args.max_timestamp)
      if max_date:
          max_year = int(max_date.group(1))
          max_month = int(max_date.group(2))
          max_day = int(max_date.group(3))
      else:
          log("Error: Incorrect max timestamp")
          exit(1)

      # Converting timestamp args to datetime
      min_timestamp = datetime.strptime(args.min_timestamp, '%Y-%m-%dT%H:%M:%S')
      max_timestamp = datetime.strptime(args.max_timestamp, '%Y-%m-%dT%H:%M:%S')

      chunk = 0
      written_alerts = 0
      trimmed_alerts = open(output_file, 'w')

      max_time=datetime(max_year, max_month, max_day)
      current_time=datetime(min_year, min_month, min_day)

      while current_time <= max_time: 
          alert_file = "{0}logs/alerts/{1}/{2}/ossec-alerts-{3:02}.json.gz".format(fortishield_path,current_time.year,month_dict[current_time.month],current_time.day)

          if os.path.exists(alert_file):
              daily_alerts = 0
              compressed_alerts = gzip.open(alert_file, 'r')
              log("Reading file: "+ alert_file)
              for line in compressed_alerts:
                  # Transform line to json object
                  try:
                      line_json = json.loads(line.decode("utf-8", "replace"))

                      # Remove unnecessary part of the timestamp
                      string_timestamp = line_json['timestamp'][:19]

                      # Ensure timestamp integrity
                      while len(line_json['timestamp'].split("+")[0]) < 23:
                          line_json['timestamp'] = line_json['timestamp'][:20] + "0" + line_json['timestamp'][20:]

                      # Get the timestamp readable
                      event_date = datetime.strptime(string_timestamp, '%Y-%m-%dT%H:%M:%S')

                      # Check the timestamp belongs to the selected range
                      if (event_date <= max_timestamp and event_date >= min_timestamp):
                          chunk+=1
                          trimmed_alerts.write(json.dumps(line_json))
                          trimmed_alerts.write("\n")
                          trimmed_alerts.flush()
                          daily_alerts += 1
                          if chunk >= EPS_MAX:
                              chunk = 0
                              time.sleep(2)
                          if os.path.getsize(output_file) >= max_bytes:
                              trimmed_alerts.close()
                              log("Output file reached max size, setting it to zero and restarting")
                              time.sleep(EPS_MAX/100)
                              trimmed_alerts = open(output_file, 'w')

                  except ValueError as e:
                      print("Oops! Something went wrong reading: {}".format(line))
                      print("This is the error: {}".format(str(e)))

              compressed_alerts.close()
              log("Extracted {0} alerts from day {1}-{2}-{3}".format(daily_alerts,current_time.day,month_dict[current_time.month],current_time.year))
          else:
              log("Couldn't find file {}".format(alert_file))

          #Move to next file
          current_time += timedelta(days=1)

      trimmed_alerts.close()

   While you run the ``recovery.py`` script, you need to consider the following parameters:

   .. code-block:: none

      usage: recovery.py [-h] [-eps eps] -min min_timestamp -max max_timestamp -o
                            output_file [-log log_file] [-w fortishield_path]
                            [-sz max_size]

        -eps eps, --eps eps   Events per second. Default: 400
        -min min_timestamp, --min_timestamp min_timestamp
                              Min timestamp. Example: 2019-11-13T08:42:17
        -max max_timestamp, --max_timestamp max_timestamp
                              Max timestamp. Example: 2019-11-13T23:59:06
        -o output_file, --output_file output_file
                              Alerts output file.
        -log log_file, --log_file log_file
                              Logs output.
        -w fortishield_path, --fortishield_path fortishield_path
                              Path to Fortishield. By default:/var/ossec/
        -sz max_size, --max_size max_size
                              Max output file size in Gb. Default: 1Gb. Example: 2.5

#. Run the command below to make the ``recovery.py`` script executable:

   .. code-block:: console

      # chmod +x recovery.py

#. Execute the script using ``nohup`` command in the background to keep it running after the session is closed. It may take time depending on the size of the old logs.

   Usage example:

   .. code-block:: console

      # nohup ./recovery.py -eps 500 -min 2023-06-10T00:00:00 -max 2023-06-18T23:59:59 -o /tmp/recovery.json -log ./recovery.log -sz 2.5 &

#. Add the ``/tmp/recovery.json`` path to the Fortishield Filebeat module ``/usr/share/filebeat/module/fortishield/alerts/manifest.yml`` so that Filebeat sends the old alerts to the Fortishield indexer for indexing:

   .. code-block:: yaml
      :emphasize-lines: 7

      module_version: 0.1

      var:
        - name: paths
          default:
            - /var/ossec/logs/alerts/alerts.json
            - /tmp/recovery.json
        - name: index_prefix
          default: fortishield-alerts-4.x-

      input: config/alerts.yml

      ingest_pipeline: ingest/pipeline.json

#. Restart Filebeat for the changes to take effect.

   .. code-block:: console

      # systemctl restart filebeat

Verifying data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the Fortishield dashboard, navigate to the **Threat Hunting**, **File Integrity Monitoring**, **Vulnerability Detection**, and any other modules to see if the data is restored successfully.
