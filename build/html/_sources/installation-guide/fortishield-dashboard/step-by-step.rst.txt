.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to install Fortishield dashboard, a flexible and intuitive web interface for mining and visualizing the events and archives. 

.. _fortishield_dashboard_step_by_step:

Installing the Fortishield dashboard step by step
===========================================

Install and configure the Fortishield dashboard following step-by-step instructions. The Fortishield dashboard is a web interface for mining and visualizing the Fortishield server alerts and archived events.

.. note:: You need root user privileges to run all the commands described below.

Fortishield dashboard installation
----------------------------

Installing package dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /_templates/installations/dashboard/install-dependencies.rst

Adding the Fortishield repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    If you are installing the Fortishield dashboard on the same host as the Fortishield indexer or the Fortishield server, you may skip these steps as you may have added the Fortishield repository already.

  .. tabs::
  
    .. group-tab:: Yum
  
  
      .. include:: /_templates/installations/common/yum/add-repository.rst
  
  
  
    .. group-tab:: APT
  
  
      .. include:: /_templates/installations/common/deb/add-repository.rst
  
  
  

Installing the Fortishield dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install the Fortishield dashboard package.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum -y install fortishield-dashboard|FORTISHIELD_DASHBOARD_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console
              
            # apt-get -y install fortishield-dashboard|FORTISHIELD_DASHBOARD_DEB_PKG_INSTALL|

Configuring the Fortishield dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Edit the ``/etc/fortishield-dashboard/opensearch_dashboards.yml`` file and replace the following values:

     #. ``server.host``: This setting specifies the host of the Fortishield dashboard server. To allow remote users to connect, set the value to the IP address or DNS name of the Fortishield dashboard server. The value ``0.0.0.0`` will accept all the available IP addresses of the host.

     #. ``opensearch.hosts``: The URLs of the Fortishield indexer instances to use for all your queries. The Fortishield dashboard can be configured to connect to multiple Fortishield indexer nodes in the same cluster. The addresses of the nodes can be separated by commas. For example,  ``["https://10.0.0.2:9200", "https://10.0.0.3:9200","https://10.0.0.4:9200"]``

        .. code-block:: yaml
          :emphasize-lines: 1,3

             server.host: 0.0.0.0
             server.port: 443
             opensearch.hosts: https://localhost:9200
             opensearch.ssl.verificationMode: certificate




Deploying certificates
^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    Make sure that a copy of the ``fortishield-certificates.tar`` file, created during the initial configuration step, is placed in your working directory.

  .. include:: /_templates/installations/dashboard/deploy_certificates.rst


Starting the Fortishield dashboard service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Enable and start the Fortishield dashboard service.

      .. include:: /_templates/installations/dashboard/enable_dashboard.rst

      
      **Only for distributed deployments**  
      
          Edit the ``/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml`` file and replace the ``url`` value with the IP address or hostname of the Fortishield server master node.
          
            .. code-block:: yaml
               :emphasize-lines: 3
            
               hosts:
                 - default:
                     url: https://localhost
                     port: 55000
                     username: fortishield-wui
                     password: fortishield-wui
                     run_as: false


  #. Access the Fortishield web interface with your credentials.

      - URL: *https://<fortishield-dashboard-ip>*
      - **Username**: *admin*
      - **Password**: *admin*

    When you access the Fortishield dashboard for the first time, the browser shows a warning message stating that the certificate was not issued by a trusted authority. An exception can be added in the advanced options of the web browser. For increased security, the ``root-ca.pem``  file previously generated can be imported to the certificate manager of the browser. Alternatively, a certificate from a trusted authority can be configured. 


Securing your Fortishield installation
--------------------------------


You have now installed and configured all the Fortishield central components. We recommend changing the default credentials to protect your infrastructure from possible attacks. 

Select your deployment type and follow the instructions to change the default passwords for both the Fortishield API and the Fortishield indexer users.


.. tabs::

   .. group-tab:: All-in-one deployment

      #. Use the Fortishield passwords tool to change all the internal users' passwords.
      
         .. code-block:: console
         
            # /usr/share/fortishield-indexer/plugins/opensearch-security/tools/fortishield-passwords-tool.sh --change-all --admin-user fortishield --admin-password fortishield
         
         .. code-block:: console
            :class: output
       
            INFO: The password for user admin is yWOzmNA.?Aoc+rQfDBcF71KZp?1xd7IO
            INFO: The password for user kibanaserver is nUa+66zY.eDF*2rRl5GKdgLxvgYQA+wo
            INFO: The password for user kibanaro is 0jHq.4i*VAgclnqFiXvZ5gtQq1D5LCcL
            INFO: The password for user logstash is hWW6U45rPoCT?oR.r.Baw2qaWz2iH8Ml
            INFO: The password for user readall is PNt5K+FpKDMO2TlxJ6Opb2D0mYl*I7FQ
            INFO: The password for user snapshotrestore is +GGz2noZZr2qVUK7xbtqjUup049tvLq.
            WARNING: Fortishield indexer passwords changed. Remember to update the password in the Fortishield dashboard and Filebeat nodes if necessary, and restart the services.
            INFO: The password for Fortishield API user fortishield is JYWz5Zdb3Yq+uOzOPyUU4oat0n60VmWI
            INFO: The password for Fortishield API user fortishield-wui is +fLddaCiZePxh24*?jC0nyNmgMGCKE+2
            INFO: Updated fortishield-wui user password in fortishield dashboard. Remember to restart the service.
       
    
   .. group-tab:: Distributed deployment

      #. On `any Fortishield indexer node`, use the Fortishield passwords tool to change the passwords of the Fortishield indexer users. 

         .. code-block:: console
  
            # /usr/share/fortishield-indexer/plugins/opensearch-security/tools/fortishield-passwords-tool.sh --change-all
  
         .. code-block:: console
            :class: output

            INFO: Fortishield API admin credentials not provided, Fortishield API passwords not changed.
            INFO: The password for user admin is wcAny.XUwOVWHFy.+7tW9l8gUW1L8N3j
            INFO: The password for user kibanaserver is qy6fBrNOI4fD9yR9.Oj03?pihN6Ejfpp
            INFO: The password for user kibanaro is Nj*sSXSxwntrx3O7m8ehrgdHkxCc0dna
            INFO: The password for user logstash is nQg1Qw0nIQFZXUJc8r8+zHVrkelch33h
            INFO: The password for user readall is s0iWAei?RXObSDdibBfzSgXdhZCD9kH4
            INFO: The password for user snapshotrestore is Mb2EHw8SIc1d.oz.nM?dHiPBGk7s?UZB
            WARNING: Fortishield indexer passwords changed. Remember to update the password in the Fortishield dashboard and Filebeat nodes if necessary, and restart the services.

      #. On your `Fortishield server master node`, download the Fortishield passwords tool and use it to change the passwords of the Fortishield API users.

         .. code-block:: console
  
            # curl -sO https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MINOR|/fortishield-passwords-tool.sh
            # bash fortishield-passwords-tool.sh --change-all --admin-user fortishield --admin-password fortishield
  
         .. code-block:: console
            :class: output

            INFO: The password for Fortishield API user fortishield is ivLOfmj7.jL6*7Ev?UJoFjrkGy9t6Je.
            INFO: The password for Fortishield API user fortishield-wui is fL+f?sFRPEv5pYRE559rqy9b6G4Z5pVi

      #. On `all your Fortishield server nodes`, run the following command to update the `admin` password in the Filebeat keystore. Replace ``<admin-password>`` with the random password generated in the first step.
      
         .. code-block:: console

            # echo <admin-password> | filebeat keystore add password --stdin --force

      #. Restart Filebeat to apply the change.

         .. include:: /_templates/common/restart_filebeat.rst

         .. note:: Repeat steps 3 and 4 on `every Fortishield server node`.
       
      #. On your `Fortishield dashboard node`, run the following command to update the `kibanaserver` password in the Fortishield dashboard keystore. Replace ``<kibanaserver-password>`` with the random password generated in the first step.

         .. code-block:: console

            # echo <kibanaserver-password> | /usr/share/fortishield-dashboard/bin/opensearch-dashboards-keystore --allow-root add -f --stdin opensearch.password

      #. Update the ``/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml`` configuration file with the new `fortishield-wui` password generated in the second step.

         .. code-block:: yaml
            :emphasize-lines: 6
           
            hosts:
              - default:
                  url: https://localhost
                  port: 55000
                  username: fortishield-wui
                  password: "<fortishield-wui-password>"
                  run_as: false

      #. Restart the Fortishield dashboard to apply the changes.

         .. include:: /_templates/common/restart_dashboard.rst


Next steps
----------

All the Fortishield central components are successfully installed and secured.

.. raw:: html

  <div class="link-boxes-group layout-3" data-step="4">
    <div class="steps-line">
      <div class="steps-number past-step">1</div>
      <div class="steps-number past-step">2</div>
      <div class="steps-number past-step">3</div>
    </div>
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="../fortishield-indexer/index.html">
        <p class="link-boxes-label">Install the Fortishield indexer</p>

.. image:: ../../images/installation/Indexer-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="../fortishield-server/index.html">
        <p class="link-boxes-label">Install the Fortishield server</p>

.. image:: ../../images/installation/Server-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="index.html">
        <p class="link-boxes-label">Install the Fortishield dashboard</p>

.. image:: ../../images/installation/Dashboard-Circle.png
     :align: center
     :height: 61px
     
.. raw:: html

      </a>
    </div>
  </div>


The Fortishield environment is now ready, and you can proceed with installing the Fortishield agent on the endpoints to be monitored. To perform this action, see the :doc:`Fortishield agent </installation-guide/fortishield-agent/index>` section.

If you want to uninstall the Fortishield dashboard, see :ref:`uninstall_dashboard`.
