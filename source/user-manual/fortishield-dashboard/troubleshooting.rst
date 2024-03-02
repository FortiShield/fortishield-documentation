.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: This section of the Fortishield documentation lists the common installation or usage issues with the Fortishield dashboard and how to resolve them. 
  
.. _fortishield_dashboard_troubleshooting:

Troubleshooting
===============

This section collects common installation or usage issues on the Fortishield dashboard, and some basic steps to solve them.

Fortishield API seems to be down
--------------------------

This issue means that your Fortishield API might be unavailable. Check the status of the Fortishield manager to check if the service is active: 

.. include:: /_templates/installations/fortishield/common/check_fortishield_manager.rst

If the Fortishield API is running, try to fetch data using the CLI from the Fortishield dashboard server:

.. code-block:: console

  # curl -k -X GET "https://<api_url>:55000/" -H "Authorization: Bearer $(curl -u <api_user>:<api_password> -k -X POST 'https://<api_url>:55000/security/user/authenticate?raw=true')"

.. code-block:: console
  :class: output

    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
    100   271  100   271    0     0    879      0 --:--:-- --:--:-- --:--:--   882
    {"data": {"title": "Fortishield API REST", "api_version": "4.1.1", "revision": 40110, "license_name": "GPL 2.0", "license_url": "https://github.com/fortishield/fortishield/blob/4.1/LICENSE", "hostname": "localhost.localdomain", "timestamp": "2021-03-03T10:01:18+0000"}, "error": 0}



I do not see alerts in the Fortishield dashboard
------------------------------------------

The first step is to check if there are alerts in Fortishield indexer.

.. code-block:: console

  # curl https://<FORTISHIELD_INDEXER_IP>:9200/_cat/indices/fortishield-alerts-* -u <fortishield_indexer_user>:<fortishield_indexer_password> -k

.. code-block:: none
    :class: output

     green open fortishield-alerts-4.x-2021.03.03 xwFPX7nFQxGy-O5aBA3LFQ 3 0 340 0 672.6kb 672.6kb

If you do not see any Fortishield related index, it means you have no alerts stored in Fortishield indexer.

To ensure that Filebeat is correctly configured, run the following command:

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



Could not connect to API with id: default: 3003 - Missing param: API USERNAME
-----------------------------------------------------------------------------

Starting Fortishield 4.0 the Fortishield API username variable changed from ``user`` to ``username``. It's necessary to change the credentials (foo:bar are no longer accepted) as well as the name of the variable in the ``/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml`` configuration file. For example, the configuration can be: 

.. code-block:: console
   
   hosts:
    - production:
        url: https://localhost
        port: 55000
        username: fortishield-wui
        password: fortishield-wui
        run_as: false


"Fortishield API and Fortishield dashboard version mismatch" error is displayed
-------------------------------------------------------------------

This error shows a mismatch between the Fortishield server and the Fortishield dashboard versions.

The Fortishield server and the Fortishield dashboard must run the same major and minor versions. For example:

-  `Fortishield server |FORTISHIELD_CURRENT_MINOR|.x`
-  `Fortishield dashboard |FORTISHIELD_CURRENT_MINOR|.y`

Moreover, we recommend both server and dashboard run the same full version, for example |FORTISHIELD_CURRENT|. Running the same full version ensures the correct operation and communication between these components.

Check out how to upgrade Fortishield in our :doc:`upgrade guide</upgrade-guide/index>`.

Saved object for index pattern not found
----------------------------------------

Saved objects store data for later use, including dashboards, visualizations, maps, index patterns, and more.

This message indicates that there is a problem loading the information of an index pattern which should be stored in a saved object, but the dashboard is unable to find it.

This situation can happen if the indexer is reinstalled and the previously saved objects are lost, while the dashboard is running and is not restarted in the process.

Remediation
^^^^^^^^^^^

The dashboard initializes the saved objects with the index definitions when it starts, so the suggested solution is to restart the service to initialize the saved objects again. 

#. Restart the Fortishield dashboard service.

   .. include:: /_templates/common/restart_dashboard.rst

   This will initialize the index with the required mappings.

   .. note:: If the index contains data but has missing objects, the dashboard will migrate the data to a new index with the missing objects added.

If the restart does not solve the problem, we can execute this process manually:

#. Stop the Fortishield dashboard service.

   .. tabs::
   
      .. group-tab:: Systemd
   
         .. code-block:: console
   
            # systemctl stop fortishield-dashboard
   
      .. group-tab:: SysV
   
         .. code-block:: console
   
            # service fortishield-dashboard stop

#. Identify the index or indices that have the wrong field mappings, this depends on the logged user that experiences the problem or the selected tenant. By default, the index name should start with ``.kibana``.

#. Get the field mapping for the ``type`` field for the indices that store the saved objects.

   .. code-block:: console

      # curl https://<FORTISHIELD_INDEXER_IP>:9200/.kibana*/_mapping/field/type?pretty -u <fortishield_indexer_user>:<fortishield_indexer_password> -k

   .. code-block:: none
     :class: output
     :emphasize-lines: 8,10,11,26,28,29

     {
       ".kibana" : {
         "mappings" : {
           "type" : {
             "full_name" : "type",
             "mapping" : {
               "type" : {
                 "type" : "text",
                 "fields" : {
                   "keyword" : {
                     "type" : "keyword",
                     "ignore_above" : 256
                   }
                 }
               }
             }
           }
         }
       },
       ".kibana_92668751_admin_1" : {
         "mappings" : {
           "type" : {
             "full_name" : "type",
             "mapping" : {
               "type" : {
                 "type" : "text",
                 "fields" : {
                   "keyword" : {
                     "type" : "keyword",
                     "ignore_above" : 256
                   }
                 }
               }
             }
           }
         }
       }
     }
   
   
   In the output, we can see `type` field mapping for the ``.kibana`` and ``.kibana_92668751_admin_1`` indices.  Note that the field mapping type for the `type` field is ``text`` and that it contains a subfield called `keyword`. This is not the expected result, the `type` field should be ``keyword``, not ``text``, and it should not include the `keyword` subfield. 
   
   These errors happened because there was no template that specified the appropriate field mappings at the time the saved object data was indexed. To solve the errors, we need to remove the index and rebuild it. 

#. Delete the index or indices that store the saved objects with the wrong field mapping.

   .. code-block:: console

      # curl https://<FORTISHIELD_INDEXER_IP>:9200/<INDEX/INDICES_SEPARATED_BY_COMMAS> -u <fortishield_indexer_user>:<fortishield_indexer_password> -k -XDELETE

   .. code-block:: none
      :class: output

      {“acknowledged”:true}


#. Restart the Fortishield dashboard service.

   .. include:: /_templates/common/restart_dashboard.rst

.. note:: These actions take into account that the index that stores the saved objects must have valid field mappings. The field mappings are defined through a template, so they should exist before the index is created. This template is added when Fortishield dashboard starts if it doesn’t exist.

None of the above solutions are fixing my problem
-------------------------------------------------

We have a welcoming community which can help you with most of the problems you might have regarding Fortishield deployment and usage `<https://fortishield.com/community>`_.

Also, you can contact us opening issues in our GitHub repositories under the `organization <https://github.com/fortishield>`_.

We will  be interested in the log files of your deployment. You can check them out on each component:

Check the following log files:

      - Fortishield indexer:

      .. code-block:: console

          # cat /var/log/fortishield-indexer/fortishield-cluster.log | grep -i -E "error|warn"

      - Fortishield manager:

      .. code-block:: console

          # cat /var/log/filebeat/filebeat | grep -i -E "error|warn"

          # cat /var/ossec/logs/ossec.log | grep -i -E "error|warn"

      - Fortishield dashboard:

      .. code-block:: console

          # journalctl -u fortishield-dashboard

          # cat /usr/share/fortishield-dashboard/data/fortishield/logs/fortishieldapp.log | grep -i -E "error|warn"

    .. note::
      The Fortishield indexer uses the ``/var/log`` folder to store logs by default.

    .. warning::
      By default, the Fortishield dashboard doesn't store logs on a file. You can change this by configuring ``logging.dest`` setting in the ``opensearch_dashboard.yml`` configuration file.



    
