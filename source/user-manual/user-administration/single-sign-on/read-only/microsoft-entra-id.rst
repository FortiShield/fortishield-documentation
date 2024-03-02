.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Microsoft Entra ID is a cloud-based identity and access management service by Microsoft. Learn more about it and the read-only role in this section of the Fortishield documentation.

Microsoft Entra ID
==================

`Microsoft Entra ID <https://portal.azure.com/>`_ (ME-ID) is a cloud-based identity and access management service by Microsoft. It provides single sign-on, multifactor authentication, and access to internal and cloud developed applications. In this guide, we integrate the Microsoft Entra ID IdP to authenticate users into the Fortishield platform.

There are three stages in the single sign-on integration.

#. `Microsoft Entra ID Configuration`_
#. `Fortishield indexer configuration`_
#. `Fortishield dashboard configuration`_
   
.. note::

   You may have to request a free trial at least to complete the configuration. 

Microsoft Entra ID Configuration
--------------------------------

#. Create a Microsoft account or use your own if you already have one.
#. Go to `Microsoft Azure Portal <https://portal.azure.com/>`_ and sign in with your Microsoft account.
#. Create an app in **Microsoft Entra ID**.

   #. Go to **Microsoft Entra ID** > **Enterprise applications** > **New application** and **Create your own application**. 

   #. Select **Integrate any other application you don't find in the gallery**. Give a name to your application and click **Add**. In our case, we name this application ``fortishield-sso``.

   .. thumbnail:: /images/single-sign-on/azure-active-directory/01-go-to-azure-active-directory.png
      :title: Create an app in Microsoft Entra ID
      :align: center
      :width: 80%

#. Create a role for your application.

   #. Go back to **Microsoft Entra ID** and click on **App registrations**.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/02-click-on-app-registrations-RO.png
         :title: Click on App registrations
         :align: center
         :width: 80%

   #. Select your new app under **All applications** and click **App roles**.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/03-select-app-roles-RO.png
         :title: Select your new app
         :align: center
         :width: 80%

   #. Add the following details to your app role:

      -  **Display name**: This can be any value that you want. In our case, this is ``Fortishield Read Only Role``.
      -  **Allowed member types**: Select ``Users/Groups``.
      -  **Value**: defines the name of the role. In this case ``fortishield-readonly``, which will be the backend role value to be mapped on the Fortishield dashboard.
      -  **Description**: This can be any value that you want. In our case, this is ``Fortishield Read Only Role``.
      -  **Do you want to enable this app role**: Click on the checkmark to enable the role.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/04-create-app-roles-RO.png

   #. Click **Apply** to save the changes and proceed to the next step.

#. Assign a user to the app.

   #. In **Microsoft Entra ID**, go to **Enterprise applications**, select your application and then click on **Assign users and groups** (or **Users and Groups** in the panel to the left).

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/05-assign-a-user-to-the-app-RO.png
         :title: Assign a user to the app
         :align: center
         :width: 80%

   #. Click on **Add user/group**, assign a **user** and select the role we created in **App roles**. Click on **Assign** to save the configuration.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/06-click-on-add-user-group-RO.png
         :title: Click on Add user/group
         :align: center
         :width: 80%

#. Configure Single sign-on.

   #. Go to **Enterprise applications**, select your application and then click on **Set up single sign-on > SAML**.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/07-configure-single-sign-on-RO.png
         :title: Configure Single sign-on
         :align: center
         :width: 80%

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/08-set-up-single-sign-on-SAML-RO.png
         :title: Set up single sign-on > SAML
         :align: center
         :width: 80%
    
      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/09-set-up-single-sign-on-SAML-RO.png
         :title: Set up single sign-on > SAML 
         :align: center
         :width: 80%
    
      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/10-set-up-single-sign-on-SAML-RO.png
         :title: Set up single sign-on > SAML
         :align: center
         :width: 80%

   #. In option 1, under  **Basic SAML Configuration**, click **edit** and set ``fortishield-saml`` as **Identifier (Entity ID)**, ``https://<FORTISHIELD_DASHBOARD_URL>/_opendistro/_security/saml/acs`` as **Reply URL (Assertion Consumer Service URL)**, and ``https://<FORTISHIELD_DASHBOARD_URL>`` as **Sign on URL (Optional)**. Replace ``<FORTISHIELD_DASHBOARD_URL>`` with the corresponding value. Save and proceed to the next step.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/11-click-edit-and-set-fortishield-saml-RO.png
         :title: Click edit and set fortishield-saml
         :align: center
         :width: 80%

   #. In option 2 under **Attributes & Claims**, click **edit** and select **Add new claim**. Select **Roles** as the name and **user.assignedroles** as **Source attribute**. This claim will be mapped with ``roles_key`` on the Fortishield indexer configuration.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/12-click-edit-and-select-add-new-claim.png
         :title: Click edit and select Add new claim
         :align: center
         :width: 80%

#. Note the necessary parameters. In the **Enterprise applications** menu, select your application and then click on **Single sign-on**. Note some parameters that will be used in the Fortishield indexer configuration.

   - In option 3 **SAML Certificate**, the **App Federation Metadata Url** will be the ``idp.metadata_url`` in the Fortishield indexer configuration file.

   - Go to the metadata URL using your web browser. Copy the value of the ``<X509Certificate>`` field. It’s your ``exchange_key`` parameter:

   .. thumbnail:: /images/single-sign-on/azure-active-directory/13-go-to-the-metadata-url.png
      :title: Go to the metadata URL
      :align: center
      :width: 80%

   - In option 4 **Set up <YOUR APPLICATION>**, the **Microsoft Entra ID Identifier** will be our ``idp.entity_id``.

Fortishield indexer configuration
---------------------------

Edit the Fortishield indexer security configuration files. We recommend that you back up these files before you carry out the configuration.

#. Edit the ``/etc/fortishield-indexer/opensearch-security/config.yml`` file and change the following values:

   - Set the ``order`` in ``basic_internal_auth_domain`` to ``0`` and the ``challenge`` flag to ``false``. 

   - Include a ``saml_auth_domain`` configuration under the ``authc`` section similar to the following:

   .. code-block:: yaml
      :emphasize-lines: 7,10,22,23,25,26,27,28

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
              transport_enabled: false
              order: 1
              http_authenticator:
                type: saml
                challenge: true
                config:
                  idp:
                    metadata_url: https://login.microsoftonline.com/...
                    entity_id: https://sts.windows.net/...
                  sp:
                    entity_id: fortishield-saml
                  kibana_url: https://<FORTISHIELD_DASHBOARD_URL>
                  roles_key: Roles
                  exchange_key: 'MIIC8DCCAdigAwIBAgIQXzg.........'
              authentication_backend:
                type: noop


   Ensure to change the following parameters to their corresponding value: 

   - ``idp.metadata_url`` 
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

Fortishield dashboard configuration
-----------------------------

#. Create a new role mapping for the backend role. Follow these steps to create a new role mapping, and grant read-only permissions to the backend role.

   #. Log into the Fortishield dashboard as administrator.
   #. Click the upper-left menu icon **☰** to open the options, go to **Indexer/dashboard management** > **Security**, and then **Roles** to open the roles page.
   #. Click **Create role**, complete the empty fields with the following parameters, and then click **Create** to complete the task.

      -  **Name**: Assign a name to the role.
      -  **Cluster permissions**: ``cluster_composite_ops_ro``
      -  **Index**: ``*``
      -  **Index permissions**: ``read``
      -  **Tenant permissions**: Select ``global_tenant`` and the ``Read only`` option.
   #. Select the newly created role.
   #. Select the **Mapped users** tab and click **Manage mapping**.
   #. Under **Backend roles**, add the value attribute of the app role you created in Microsoft Entra ID and click **Map** to confirm the action. In our case, the backend role is ``fortishield-readonly``.

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
      - **Roles**: Select ``readonly``.
      - **Custom rules**: Click **Add new rule** to expand this field.
      - **User field**: ``backend_roles``
      - **Search operation**: ``FIND``
      - **Value**: Assign the value attribute of the app role you created  in Microsoft Entra ID, in our case, this is ``fortishield-readonly``.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/read-only/Fortishield-role-mapping-RO.png
         :title: Create Fortishield role mapping
         :alt: Create Fortishield role mapping 
         :align: center
         :width: 80%      

   #. Click **Save role mapping** to save and map the backend role with Fortishield as *read-only*.

#. Edit the Fortishield dashboard configuration file. Add these configurations to ``/etc/fortishield-dashboard/opensearch_dashboards.yml``. We recommend that you back up these files before you carry out the configuration.

   .. code-block:: console  

      opensearch_security.auth.type: "saml"
      server.xsrf.allowlist: ["/_opendistro/_security/saml/acs", "/_opendistro/_security/saml/logout", "/_opendistro/_security/saml/acs/idpinitiated"]
      opensearch_security.session.keepalive: false

#. Restart the Fortishield dashboard service.

   .. include:: /_templates/common/restart_dashboard.rst

#. Test the configuration. Go to your Fortishield dashboard URL and log in with your Microsoft account. 
