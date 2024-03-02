.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Jumpcloud is a Unified Device and Identity Access Management platform. Learn more about it and the administrator role in this section of the Fortishield documentation.

Jumpcloud
=========

`Jumpcloud <https://jumpcloud.com/>`__, is a Unified Device and Identity Access Management platform that provides services such as Multi-Factor Authentication (MFA), Single Sign-On, password management, and cloud directory. In this guide, we integrate the Jumpcloud SSO to authenticate users into the Fortishield platform.

There are three stages in the single sign-on integration.

#. `Jumpcloud Configuration`_
#. `Fortishield indexer configuration`_
#. `Fortishield dashboard configuration`_

Jumpcloud Configuration
-----------------------

#. Create an account in Jumpcloud. Request a free trial if you don't have a paid license.
#. Create a new user. This step can be skipped if you are just testing, you can use your Jumpcloud ``admin`` user for example.

   #. Go to **User Management**, click on **Users** > **(+)** >  **Manual user entry**. Fill in the user information, activate the user and click on **save user**. 

      .. thumbnail:: /images/single-sign-on/jumpcloud/01-go-to-user-management-and-click-on-users.png
          :title: Go to User Management and click on Users
          :align: center
          :width: 80%

#. Create a new group and assign the user.

   #. Go to **User Management** > **User Groups** > **(+)** and give a name to the group. In our case, this is ``Fortishield admins``.

      .. thumbnail:: /images/single-sign-on/jumpcloud/02-go-to-user-management-user-groups.png
          :title: Go to User Management - User Groups
          :align: center
          :width: 80%

      The name you give to your group will be used in the configuration. It will be our ``backend_roles`` in ``roles_mapping.yml``.

   #. In the selected **User Groups**,  go to the **Users** tab, select the newly created user and Save the changes.

      .. thumbnail:: /images/single-sign-on/jumpcloud/03-go-to-users-tab.png
          :title: Go to the Users tab and select the newly created user 
          :align: center
          :width: 80%

#. Create a new app. Configure the SAML settings while you create the app.

   #. Under the User Authentication section, go to **SSO Applications**, select **+ Add New Application**, and select **Custom Application**.

      .. thumbnail:: /images/single-sign-on/jumpcloud/04-go-to-SSO.png
          :title: Add new SSO application
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/05-select-custom-app.png
          :title: Select custom application
          :align: center
          :width: 80%    

   #. Complete the **Create New Application Integration** page with the appropriate information.

      -  Click **Next** on the **Select Application** page.
      -  Check the **Manage Single Sign-On (SSO)** and **Configure SSO with SAML** options on the **Select Options** page. Click **Next** to proceed to the next step.
      -  Assign a **Display Label** to the application, and click the **Show this application in User Portal** checkbox on the **Enter General Info** page. Click **Save Application** to apply the settings. 
      -  Click **Configure Application** on the Review page.

      .. thumbnail:: /images/single-sign-on/jumpcloud/06-select-application.png
          :title: Custom application selected
          :alt: Custom application selected
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/07-select-manage-sso.png
          :title: Configure SSO options
          :alt: Configure SSO options
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/08-enter-general-info.png
          :title: Enter general info
          :alt: Enter general info
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/09-go-to-review.png
          :title: Confirm new application integration
          :alt: Confirm new application integration
          :align: center
          :width: 80%    

   #. Complete the SSO tab with the appropriate information.

      - **IdP Entity ID**: ``fortishield`` (this will be the ``idp.entity_id`` in our Fortishield indexer configuration).
      - **SP Entity ID**: ``fortishield-saml`` (this will be the ``sp.entity_id`` in our Fortishield indexer configuration).
      - **ACS URL**: ``https://<FORTISHIELD_DASHBOARD_URL>/_opendistro/_security/saml/acs``
      - Check **Sign Assertion**.
      - Check **Declare Redirect Endpoint**.
      - Check **include group attribute** and add **Roles** as the attribute. This will be used later in the ``config.yml`` configuration file.

      The rest of the options can be left as their default values.

      .. thumbnail:: /images/single-sign-on/jumpcloud/10-complete-the-sso-tab.png
          :title: Complete the SSO tab
          :align: center
          :width: 80%   

      .. thumbnail:: /images/single-sign-on/jumpcloud/11-complete-the-sso-tab.png      
          :title: Complete the SSO tab
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/12-complete-the-sso-tab.png
          :title: Complete the SSO tab
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/13-complete-the-sso-tab.png
          :title: Complete the SSO tab
          :align: center
          :width: 80%    

   #. On the **User Groups** tab, select the **Group** created previously and click **save**.

      .. thumbnail:: /images/single-sign-on/jumpcloud/14-on-the-user-groups-tab.png
          :title: On the User Groups tab, select the Group created previously
          :align: center
          :width: 80% 

#. Note the necessary parameters from the SAML settings of the new app.

   #. Open the recently created application, go to the **SSO** tab and select **Export Metadata**. This will be our ``metadata_file``. Place the metadata file in the configuration directory of the Fortishield indexer. The path to the directory is ``/etc/fortishield-indexer/opensearch-security/``.

   #. Extract the ``exchange_key`` from the ``metadata_file`` under the ``ds:X509Certificate`` tag.

      .. thumbnail:: /images/single-sign-on/jumpcloud/15-go-to-the-sso-tab.png
          :title: Go to the SSO tab and select Export Metadata
          :align: center
          :width: 80% 


Fortishield indexer configuration
---------------------------

Edit the Fortishield indexer security configuration files. We recommend that you back up these files before you carry out the configuration. 

#. Place the ``metadata_jumpcloud.xml`` file within the ``/etc/fortishield-indexer/opensearch-security/`` directory. Set the file ownership to ``fortishield-indexer`` using the following command:

   .. code-block:: console

      # chown fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/opensearch-security/metadata_jumpcloud.xml

#. Edit the ``/etc/fortishield-indexer/opensearch-security/config.yml`` file and change the following values:

   - Set the ``order`` in ``basic_internal_auth_domain`` to ``0`` and the ``challenge`` flag to ``false``. 

   - Include a ``saml_auth_domain`` configuration under the ``authc`` section similar to the following:

   .. code-block:: yaml
      :emphasize-lines: 7,10,22,23,25,26,27,28,29

          authc:
      ...
            basic_internal_auth_domain:
              description: "Authenticate via HTTP Basic against internal users database"
              http_enabled: true
              transport_enabled: true
              order: 0
              http_authenticator:
                type: "basic"
                challenge: false
              authentication_backend:
                type: "intern"
            saml_auth_domain:
              http_enabled: true
              transport_enabled: true
              order: 1
              http_authenticator:
                type: saml
                challenge: true
                config:
                  idp:
                    metadata_file: '/etc/fortishield-indexer/opensearch-security/metadata_jumpcloud.xml'
                    entity_id: fortishield
                  sp:
                    entity_id: fortishield-saml
                    forceAuthn: true
                  kibana_url: https://<FORTISHIELD_DASHBOARD_URL>
                  roles_key: Roles
                  exchange_key: 'MIIBkTCB+wIBADBSMQs......'
              authentication_backend:
                type: noop



   Ensure to change the following parameters to their corresponding value:

      - ``idp.metadata_file``
      - ``idp.entity_id``
      - ``sp.entity_id``
      - ``kibana_url``
      - ``roles_key``
      - ``exchange_key``

#. Run the ``securityadmin`` script to load the configuration changes made in the ``config.yml`` file. 

   .. code-block:: console

      # export JAVA_HOME=/usr/share/fortishield-indexer/jdk/ && bash /usr/share/fortishield-indexer/plugins/opensearch-security/tools/securityadmin.sh -f /etc/fortishield-indexer/opensearch-security/config.yml -icl -key /etc/fortishield-indexer/certs/admin-key.pem -cert /etc/fortishield-indexer/certs/admin.pem -cacert /etc/fortishield-indexer/certs/root-ca.pem -h localhost -nhnv
      
   The ``-h`` flag specifies the hostname or the IP address of the Fortishield indexer node. Note that this command uses localhost, set your Fortishield indexer address if necessary.

   The command output must be similar to the following:

   .. code-block:: console
      :class: output

      Security Admin v7
      Will connect to localhost:9200 ... done
      Connected as "CN=admin,OU=Fortishield,O=Fortishield,L=California,C=US"
      OpenSearch Version: 2.10.0
      Contacting opensearch cluster 'opensearch' and wait for YELLOW clusterstate ...
      Clustername: fortishield-cluster
      Clusterstate: GREEN
      Number of nodes: 1
      Number of data nodes: 1
      .opendistro_security index already exists, so we do not need to create one.
      Populate config from /etc/fortishield-indexer/opensearch-security
      Will update '/config' with /etc/fortishield-indexer/opensearch-security/config.yml 
         SUCC: Configuration for 'config' created or updated
      SUCC: Expected 1 config types for node {"updated_config_types":["config"],"updated_config_size":1,"message":null} is 1 (["config"]) due to: null
      Done with success
   
#. Edit the ``/etc/fortishield-indexer/opensearch-security/roles_mapping.yml`` file and change the following values:

   Configure the ``roles_mapping.yml`` file to map the Jumpcloud user group to the appropriate Fortishield indexer role. In our case, we map the ``Fortishield admins`` group to the ``all_access`` role:

   .. code-block:: console
      :emphasize-lines: 6

      all_access:
        reserved: false
        hidden: false
        backend_roles:
        - "admin"
        - "Fortishield admins"
        description: "Maps admin to all_access"

#. Run the ``securityadmin`` script to load the configuration changes made in the ``roles_mapping.yml`` file. 

   .. code-block:: console

      # export JAVA_HOME=/usr/share/fortishield-indexer/jdk/ && bash /usr/share/fortishield-indexer/plugins/opensearch-security/tools/securityadmin.sh -f /etc/fortishield-indexer/opensearch-security/roles_mapping.yml -icl -key /etc/fortishield-indexer/certs/admin-key.pem -cert /etc/fortishield-indexer/certs/admin.pem -cacert /etc/fortishield-indexer/certs/root-ca.pem -h localhost -nhnv      

   The ``-h`` flag specifies the hostname or the IP address of the Fortishield indexer node. Note that this command uses localhost, set your Fortishield indexer address if necessary.
      
   The command output must be similar to the following:
       
   .. code-block:: console
      :class: output

      Security Admin v7
      Will connect to localhost:9200 ... done
      Connected as "CN=admin,OU=Fortishield,O=Fortishield,L=California,C=US"
      OpenSearch Version: 2.10.0
      Contacting opensearch cluster 'opensearch' and wait for YELLOW clusterstate ...
      Clustername: fortishield-cluster
      Clusterstate: GREEN
      Number of nodes: 1
      Number of data nodes: 1
      .opendistro_security index already exists, so we do not need to create one.
      Populate config from /etc/fortishield-indexer/opensearch-security
      Will update '/rolesmapping' with /etc/fortishield-indexer/opensearch-security/roles_mapping.yml 
         SUCC: Configuration for 'rolesmapping' created or updated
      SUCC: Expected 1 config types for node {"updated_config_types":["rolesmapping"],"updated_config_size":1,"message":null} is 1 (["rolesmapping"]) due to: null
      Done with success

Fortishield dashboard configuration
-----------------------------

#. Check the value of ``run_as`` in the ``/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml`` configuration file. If ``run_as`` is set to ``false``, proceed to the next step.

   .. code-block:: yaml
      :emphasize-lines: 7

      hosts:
        - default:
            url: https://localhost
            port: 55000
            username: fortishield-wui
            password: "<fortishield-wui-password>"
            run_as: false

   If ``run_as`` is set to ``true``, you need to add a role mapping on the Fortishield dashboard. To map the backend role to Fortishield, follow these steps:

   #. Click **☰** to open the menu on the Fortishield dashboard, go to **Server management** > **Security**, and then **Roles mapping** to open the page.

      .. thumbnail:: /images/single-sign-on/Fortishield-role-mapping.gif
         :title: Fortishield role mapping
         :alt: Fortishield role mapping 
         :align: center
         :width: 80%

   #. Click **Create Role mapping** and complete the empty fields with the following parameters:

      - **Role mapping name**: Assign a name to the role mapping.
      - **Roles**: Select ``administrator``.
      - **Custom rules**: Click **Add new rule** to expand this field.
      - **User field**: ``backend_roles``
      - **Search operation**: ``FIND``
      - **Value**: Assign the name of the Jumpcloud user group. In our case, this is  ``Fortishield admins``.

      .. thumbnail:: /images/single-sign-on/jumpcloud/Fortishield-role-mapping.png
         :title: Create Fortishield role mapping
         :alt: Create Fortishield role mapping 
         :align: center
         :width: 80%      

   #. Click **Save role mapping** to save and map the backend role with Fortishield as administrator.

#. Edit the Fortishield dashboard configuration file. Add these configurations to ``/etc/fortishield-dashboard/opensearch_dashboards.yml``. We recommend that you back up these files before you carry out the configuration.

   .. code-block:: console  

      opensearch_security.auth.type: "saml"
      server.xsrf.allowlist: ["/_opendistro/_security/saml/acs", "/_opendistro/_security/saml/logout", "/_opendistro/_security/saml/acs/idpinitiated"]
      opensearch_security.session.keepalive: false

#. Restart the Fortishield dashboard service.

   .. include:: /_templates/common/restart_dashboard.rst

#. Test the configuration. Go to your Fortishield dashboard URL and log in with your Jumpcloud account. 



