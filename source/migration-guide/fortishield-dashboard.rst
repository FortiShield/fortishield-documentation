.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Follow this guide to migrate from Open Distro for Elasticsearch Kibana to the Fortishield dashboard.
  
.. _migration_guide_dashboard:

Migrating to the Fortishield dashboard
================================

Follow this guide to migrate from Open Distro for Elasticsearch Kibana 1.13 to the Fortishield dashboard. These instructions are intended for a standard Fortishield installation, you may need to make some changes to adapt them to your environment.

To guarantee a correct operation of Fortishield, make sure to also migrate from Open Distro for Elasticsearch to the Fortishield indexer. To learn more, see the :doc:`Migrating to the Fortishield indexer </migration-guide/fortishield-indexer>` documentation. 

.. note:: You need root user privileges to run all the commands described below.

#. Stop the Kibana service. 

   .. tabs::
   
    .. group-tab:: Systemd
   
     .. code-block:: console
   
      # systemctl stop kibana
   
    .. group-tab:: SysV init
   
     .. code-block:: console
   
      # service kibana stop  

#. Add the Fortishield repository. You can skip this step if the repository is already present and enabled on your server.

    .. tabs::


      .. group-tab:: Yum


        .. include:: /_templates/installations/common/yum/add-repository.rst



      .. group-tab:: APT


        .. include:: /_templates/installations/common/deb/add-repository.rst



#. Install the Fortishield dashboard package.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum -y install fortishield-dashboard|FORTISHIELD_DASHBOARD_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console
              
            # apt-get -y install fortishield-dashboard|FORTISHIELD_DASHBOARD_DEB_PKG_INSTALL|

   .. note::

      Make sure that your Fortishield manager is updated to the latest version. To learn more, see :ref:`upgrading_fortishield_server`. 

#. Create the ``/etc/fortishield-dashboard/certs`` directory, copy your old certificates to the new location and change ownership and permissions.    

   .. code-block:: console

     # mkdir /etc/fortishield-dashboard/certs
     # cp /etc/kibana/certs/kibana.pem /etc/fortishield-dashboard/certs/dashboard.pem
     # cp /etc/kibana/certs/kibana-key.pem /etc/fortishield-dashboard/certs/dashboard-key.pem
     # cp /etc/kibana/certs/root-ca.pem /etc/fortishield-dashboard/certs/root-ca.pem
     # chmod 500 /etc/fortishield-dashboard/certs
     # chmod 400 /etc/fortishield-dashboard/certs/*
     # chown -R fortishield-dashboard:fortishield-dashboard /etc/fortishield-dashboard/certs

#. Port your settings from ``/etc/kibana/kibana.yml`` to the ``/etc/fortishield-dashboard/opensearch_dashboards.yml`` file. You can omit the ``opensearch.username`` and the ``opensearch.password`` settings as they are now stored in the Fortishield dashboard keystore. 

    .. code-block:: yaml
      :emphasize-lines: 1,3

      server.host: 0.0.0.0
      server.port: 443
      opensearch.hosts: https://localhost:9200
      opensearch.ssl.verificationMode: certificate
      #opensearch.username:
      #opensearch.password:
      opensearch.requestHeadersAllowlist: ["securitytenant","Authorization"]
      opensearch_security.multitenancy.enabled: false
      opensearch_security.readonly_mode.roles: ["kibana_read_only"]
      server.ssl.enabled: true
      server.ssl.key: "/etc/fortishield-dashboard/certs/dashboard-key.pem"
      server.ssl.certificate: "/etc/fortishield-dashboard/certs/dashboard.pem"
      opensearch.ssl.certificateAuthorities: ["/etc/fortishield-dashboard/certs/root-ca.pem"]
      uiSettings.overrides.defaultRoute: /app/wz-home

#. Add the password of the ``kibanaserver`` user to the Fortishield dashboard keystore.  Execute the command below and follow the instructions. You may find your old password in the ``/etc/kibana/kibana.yml`` configuration file. 

    .. code-block:: console

      /usr/share/fortishield-dashboard/bin/opensearch-dashboards-keystore --allow-root add opensearch.password    
   
    **Optional action** -  To change the default user, run the following command. You will need to change the password accordingly. 

    .. code-block:: console

      /usr/share/fortishield-dashboard/bin/opensearch-dashboards-keystore --allow-root add opensearch.username 


#. Enable and start the Fortishield dashboard service.

      .. include:: /_templates/installations/dashboard/enable_dashboard.rst            


#.  Port your settings from ``/usr/share/kibana/data/fortishield/config/fortishield.yml`` to ``/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml``. It is recommended to copy the content from ``/usr/share/kibana/data/fortishield/downloads/`` as well.

#. Access the Fortishield web interface at ``https://<dashboard_ip>`` with your credentials and make sure that everything is working as expected. 

#. Uninstall Kibana.

    .. tabs::
    
    
      .. group-tab:: Yum
    
    
        .. include:: /_templates/installations/elastic/yum/uninstall_kibana.rst
    
    
    
      .. group-tab:: APT
    
    
        .. include:: /_templates/installations/elastic/deb/uninstall_kibana.rst
