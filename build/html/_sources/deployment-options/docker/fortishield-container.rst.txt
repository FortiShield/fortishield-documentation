.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: In this section of our documentation, you will find more information about Fortishield Docker deployment: its requirements, usage, and exposed ports.
  
Fortishield Docker deployment
=======================

Usage
-----

You can deploy Fortishield as a single-node or multi-node stack.

-  **Single-node deployment**: Deploys one Fortishield manager, indexer, and dashboard node.
-  **Multi-node deployment**: Deploys two Fortishield manager nodes (one master and one worker), three Fortishield indexer nodes, and a Fortishield dashboard node.
  
Both deployments use persistence and allow configuring certificates to secure communications between nodes. The multi-node stack is the only deployment that contains high availability.

Single-node Deployment
^^^^^^^^^^^^^^^^^^^^^^

#. Clone the Fortishield repository to your system:

   .. code-block:: console

      # git clone https://github.com/fortishield/fortishield-docker.git -b v|FORTISHIELD_CURRENT_DOCKER|

   Then enter into the ``single-node`` directory to execute all the commands described below within this directory.

#. Provide a group of certificates for each node in the stack to secure communication between the nodes. You have two alternatives to provide these certificates:

   -  Generate self-signed certificates for each cluster node. 
    
      We have created a Docker image to automate certificate generation using the Fortishield certs gen tool.

      If your system uses a proxy, add the following to the ``generate-indexer-certs.yml`` file. If not, skip this particular step:
        
      .. code-block:: yaml
        
         environment:
           - HTTP_PROXY=YOUR_PROXY_ADDRESS_OR_DNS

      A completed example looks like:
        
      .. code-block:: yaml
        
         # Fortishield App Copyright (C) 2021 Fortishield Inc. (License GPLv2)
         version: '3'

         services:
           generator:
             image: fortishield/fortishield-certs-generator:0.0.1
             hostname: fortishield-certs-generator
             volumes:
               - ./config/fortishield_indexer_ssl_certs/:/certificates/
               - ./config/certs.yml:/config/certs.yml
             environment:
               - HTTP_PROXY=YOUR_PROXY_ADDRESS_OR_DNS
        
      Execute the following command to get the desired certificates:
      
         .. code-block:: console
         
            # docker-compose -f generate-indexer-certs.yml run --rm generator

      This saves the certificates into the ``config/fortishield_indexer_ssl_certs`` directory.

   -  Provide your own certificates for each node.

      In case you have your own certificates, provision them as follows in the ``config/fortishield_indexer_ssl_certs`` directory:

      **Fortishield indexer**: 
      
      .. code-block:: none

         config/fortishield_indexer_ssl_certs/root-ca.pem
         config/fortishield_indexer_ssl_certs/fortishield.indexer-key.pem
         config/fortishield_indexer_ssl_certs/fortishield.indexer.pem
         config/fortishield_indexer_ssl_certs/admin.pem
         config/fortishield_indexer_ssl_certs/admin-key.pem

      **Fortishield manager**:

      .. code-block:: none

         config/fortishield_indexer_ssl_certs/root-ca-manager.pem
         config/fortishield_indexer_ssl_certs/fortishield.manager.pem
         config/fortishield_indexer_ssl_certs/fortishield.manager-key.pem

      **Fortishield dashboard**:

      .. code-block:: none

         config/fortishield_indexer_ssl_certs/fortishield.dashboard.pem
         config/fortishield_indexer_ssl_certs/fortishield.dashboard-key.pem
         config/fortishield_indexer_ssl_certs/root-ca.pem
 
#. Start the Fortishield single-node deployment using docker-compose:

   -  **Foreground**:

      .. code-block:: console  

         # docker-compose up

   -  **Background**:

      .. code-block:: console  

         # docker-compose up -d

   The default username and password for the Fortishield dashboard are ``admin`` and ``SecretPassword``. For :ref:`additional security <change-pwd-existing-usr>`, you can change the default password for the Fortishield indexer *admin* user.


.. note::

   To know when the Fortishield indexer is up, the Fortishield dashboard container uses ``curl`` to run multiple queries to the Fortishield indexer API. You can expect to see several ``Failed to connect to Fortishield indexer port 9200`` log messages or “ *Fortishield dashboard server is not ready yet* ” until the Fortishield indexer is started. Then the setup process continues normally. It takes about 1 minute for the Fortishield indexer to start up. You can find the default Fortishield indexer credentials in the ``docker-compose.yml`` file.

Multi-node deployment
^^^^^^^^^^^^^^^^^^^^^

#. Clone the Fortishield repository to your system:

   .. code-block:: console

      $ git clone https://github.com/fortishield/fortishield-docker.git -b v|FORTISHIELD_CURRENT_DOCKER|
   
   Then enter into the ``multi-node`` directory to execute all the commands described below within this directory.

#. Provide a group of certificates for each node in the stack to secure communications between the nodes. You have two alternatives to provide these certificates:

   -  Generate self-signed certificates for each cluster node.

      We have created a Docker image to automate certificate generation using the Fortishield certs gen tool.

      If your system uses a proxy, add the following to the ``generate-indexer-certs.yml`` file. If not, skip this particular step:
      
      .. code-block:: yaml
      
         environment:
           - HTTP_PROXY=YOUR_PROXY_ADDRESS_OR_DNS

      A completed example looks like:
      
      .. code-block:: yaml
      
         # Fortishield App Copyright (C) 2021 Fortishield Inc. (License GPLv2)
         version: '3'

         services:
           generator:
             image: fortishield/fortishield-certs-generator:0.0.1
             hostname: fortishield-certs-generator
             volumes:
               - ./config/fortishield_indexer_ssl_certs/:/certificates/
               - ./config/certs.yml:/config/certs.yml
             environment:
               - HTTP_PROXY=YOUR_PROXY_ADDRESS_OR_DNS
      
      Execute the following command to get the desired certificates:
        
      .. code-block:: console

         # docker-compose -f generate-indexer-certs.yml run --rm generator

      This saves the certificates into the ``config/fortishield_indexer_ssl_certs`` directory.

   -  Provide your own certificates for each node.

      In case you have your own certificates, provision them as follows:
      
      **Fortishield indexer**: 
    
      .. code-block:: none

         config/fortishield_indexer_ssl_certs/root-ca.pem
         config/fortishield_indexer_ssl_certs/fortishield1.indexer-key.pem
         config/fortishield_indexer_ssl_certs/fortishield1.indexer.pem
         config/fortishield_indexer_ssl_certs/fortishield2.indexer-key.pem
         config/fortishield_indexer_ssl_certs/fortishield2.indexer.pem
         config/fortishield_indexer_ssl_certs/fortishield3.indexer-key.pem
         config/fortishield_indexer_ssl_certs/fortishield3.indexer.pem
         config/fortishield_indexer_ssl_certs/admin.pem
         config/fortishield_indexer_ssl_certs/admin-key.pem

      **Fortishield manager**:

      .. code-block:: none

         config/fortishield_indexer_ssl_certs/root-ca-manager.pem
         config/fortishield_indexer_ssl_certs/fortishield.master.pem
         config/fortishield_indexer_ssl_certs/fortishield.master-key.pem
         config/fortishield_indexer_ssl_certs/fortishield.worker.pem
         config/fortishield_indexer_ssl_certs/fortishield.worker-key.pem

      **Fortishield dashboard**:

      .. code-block:: none

         config/fortishield_indexer_ssl_certs/fortishield.dashboard.pem
         config/fortishield_indexer_ssl_certs/fortishield.dashboard-key.pem
         config/fortishield_indexer_ssl_certs/root-ca.pem


#. Start the Fortishield multi-node deployment using ``docker-compose``:

   -  **Foreground**:

      .. code-block:: console

         # docker-compose up

   -  **Background**:

      .. code-block:: console

         # docker-compose up -d

   The default username and password for the Fortishield dashboard are ``admin`` and ``SecretPassword``. For :ref:`additional security <change-pwd-existing-usr>`, you can change the default password for the Fortishield indexer *admin* user.

.. note::

   To know when the Fortishield indexer is up, the Fortishield dashboard container uses ``curl`` to run multiple queries to the Fortishield indexer API. You can expect to see several ``Failed to connect to Fortishield indexer port 9200`` log messages or “Fortishield dashboard server is not ready yet” until the Fortishield indexer is started. Then the setup process continues normally. It takes about 1 minute for the Fortishield indexer to start up. You can find the default Fortishield indexer credentials in the ``docker-compose.yml`` file.

Build docker images locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can modify and build the Fortishield manager, indexer, and dashboard images locally.

#. Clone the Fortishield repository to your system:

   .. code-block:: console
  
      # git clone https://github.com/fortishield/fortishield-docker.git -b v|FORTISHIELD_CURRENT_DOCKER|

#. For versions up to 4.3.4, enter into the ``build-docker-images`` directory and build the Fortishield manager, indexer, and dashboard images:
  
   .. code-block:: console
  
      # docker-compose build

   For version 4.3.5 and above, run the image creation script:

   .. code-block:: console
  
      # build-docker-images/build-images.sh

.. _change-pwd-existing-usr:

Change the password of Fortishield users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To improve security, you can change the default password of the Fortishield users. There are two types of Fortishield users:

-  Fortishield indexer users
-  Fortishield API users

 To change the password of these Fortishield users, perform the following steps. You must run the commands from your ``single-node/`` or ``multi-node/`` directory, depending on your Fortishield on Docker deployment.

Fortishield indexer users
~~~~~~~~~~~~~~~~~~~

 To change the password of the default ``admin`` and ``kibanaserver`` users, do the following. You can only change one at a time. 

.. warning::

   If you have custom users, add them to the ``internal_users.yml`` file. Otherwise, executing this procedure deletes them.

Setting a new hash
..................

#. Stop the deployment stack if it’s running:

   .. code-block:: console
  
      # docker-compose down

#. Run this command to generate the hash of your new password. Once the container launches, input the new password and press **Enter**.

   .. code-block:: console
  
      # docker run --rm -ti fortishield/fortishield-indexer:|FORTISHIELD_CURRENT_DOCKER| bash /usr/share/fortishield-indexer/plugins/opensearch-security/tools/hash.sh

#. Copy the generated hash.

#. Open the ``config/fortishield_indexer/internal_users.yml`` file. Locate the block for the user you are changing password for.

#. Replace the hash.

   -  ``admin`` user

      .. code-block:: YAML
         :emphasize-lines: 3

         ...
         admin:
           hash: "$2y$12$K/SpwjtB.wOHJ/Nc6GVRDuc1h0rM1DfvziFRNPtk27P.c4yDr9njO"
           reserved: true
           backend_roles:
           - "admin"
           description: "Demo admin user"

         ...

   -  ``kibanaserver`` user

      .. code-block:: YAML
         :emphasize-lines: 3

         ...
         kibanaserver:
           hash: "$2a$12$4AcgAt3xwOWadA5s5blL6ev39OXDNhmOesEoo33eZtrq2N0YrU3H."
           reserved: true
           description: "Demo kibanaserver user"

         ...

.. _fortishield-docker-password-setting:

Setting the new password
........................

#. Open  the ``docker-compose.yml`` file. Change all occurrences of the old password with the new one. For example, for a single-node deployment:

   -  ``admin`` user

      .. code-block:: YAML
         :emphasize-lines: 8, 20, 26

         ...
         services:
           fortishield.manager:
             ...
             environment:
               - INDEXER_URL=https://fortishield.indexer:9200
               - INDEXER_USERNAME=admin
               - INDEXER_PASSWORD=SecretPassword
               - FILEBEAT_SSL_VERIFICATION_MODE=full
               - SSL_CERTIFICATE_AUTHORITIES=/etc/ssl/root-ca.pem
               - SSL_CERTIFICATE=/etc/ssl/filebeat.pem
               - SSL_KEY=/etc/ssl/filebeat.key
               - API_USERNAME=fortishield-wui
               - API_PASSWORD=MyS3cr37P450r.*-
           ...
           fortishield.indexer:
             ...
             environment:
               - "OPENSEARCH_JAVA_OPTS=-Xms1024m -Xmx1024m"
               - INDEXER_PASSWORD=SecretPassword
           ...
           fortishield.dashboard:
             ...
             environment:
               - INDEXER_USERNAME=admin
               - INDEXER_PASSWORD=SecretPassword
               - FORTISHIELD_API_URL=https://fortishield.manager
               - DASHBOARD_USERNAME=kibanaserver
               - DASHBOARD_PASSWORD=kibanaserver
               - API_USERNAME=fortishield-wui
               - API_PASSWORD=MyS3cr37P450r.*-
           ...

   -  ``kibanaserver`` user

      .. code-block:: YAML
         :emphasize-lines: 10

         ...
         services:
           fortishield.dashboard:
             ...
             environment:
               - INDEXER_USERNAME=admin
               - INDEXER_PASSWORD=SecretPassword
               - FORTISHIELD_API_URL=https://fortishield.manager
               - DASHBOARD_USERNAME=kibanaserver
               - DASHBOARD_PASSWORD=kibanaserver
               - API_USERNAME=fortishield-wui
               - API_PASSWORD=MyS3cr37P450r.*-
           ...

Applying the changes
....................

#. Start the deployment stack.

   .. code-block:: console
  
      # docker-compose up -d

#. Run ``docker ps`` and note the name of the first Fortishield indexer container. For example, ``single-node-fortishield.indexer-1``, or ``multi-node-fortishield1.indexer-1``.

#. Run ``docker exec -it <FORTISHIELD_INDEXER_CONTAINER_NAME> bash`` to enter the container. For example:

   .. code-block:: console

      # docker exec -it single-node-fortishield.indexer-1 bash

#. Set the following variables:

   .. code-block:: console
  
      export INSTALLATION_DIR=/usr/share/fortishield-indexer
      CACERT=$INSTALLATION_DIR/certs/root-ca.pem
      KEY=$INSTALLATION_DIR/certs/admin-key.pem
      CERT=$INSTALLATION_DIR/certs/admin.pem
      export JAVA_HOME=/usr/share/fortishield-indexer/jdk

#. Wait for the Fortishield indexer to initialize properly. The waiting time can vary from two to five minutes. It depends on the size of the cluster, the assigned resources, and the speed of the network. Then, run the ``securityadmin.sh`` script to apply all changes.

   .. tabs::

      .. tab:: Single-node cluster

         .. code-block:: console

            $ bash /usr/share/fortishield-indexer/plugins/opensearch-security/tools/securityadmin.sh -cd /usr/share/fortishield-indexer/opensearch-security/ -nhnv -cacert  $CACERT -cert $CERT -key $KEY -p 9200 -icl

      .. tab:: Multi-node cluster

         .. code-block:: console

            $ HOST=$(grep node.name $INSTALLATION_DIR/opensearch.yml | awk '{printf $2}')
            $ bash /usr/share/fortishield-indexer/plugins/opensearch-security/tools/securityadmin.sh -cd /usr/share/fortishield-indexer/opensearch-security/ -nhnv -cacert  $CACERT -cert $CERT -key $KEY -p 9200 -icl -h $HOST

#. Exit the Fortishield indexer container and login with the new credentials on the Fortishield dashboard.

Fortishield API users
~~~~~~~~~~~~~~~

The ``fortishield-wui`` user is the user to connect with the Fortishield API by default. Follow these steps to change the password.

.. note::
   
   The password for Fortishield API users must be between 8 and 64 characters long. It must contain at least one uppercase and one lowercase letter, a number, and a symbol.

#. Open the file ``config/fortishield_dashboard/fortishield.yml`` and modify the value of ``password`` parameter.

   .. code-block:: YAML
      :emphasize-lines: 7

      ...
      hosts:
        - 1513629884013:
            url: "https://fortishield.manager"
            port: 55000
            username: fortishield-wui
            password: "MyS3cr37P450r.*-"
            run_as: false
      ...

#. Open  the ``docker-compose.yml`` file. Change all occurrences of the old password with the new one.

   .. code-block:: YAML
      :emphasize-lines: 14,25

      ...
      services:
        fortishield.manager:
          ...
          environment:
            - INDEXER_URL=https://fortishield.indexer:9200
            - INDEXER_USERNAME=admin
            - INDEXER_PASSWORD=SecretPassword
            - FILEBEAT_SSL_VERIFICATION_MODE=full
            - SSL_CERTIFICATE_AUTHORITIES=/etc/ssl/root-ca.pem
            - SSL_CERTIFICATE=/etc/ssl/filebeat.pem
            - SSL_KEY=/etc/ssl/filebeat.key
            - API_USERNAME=fortishield-wui
            - API_PASSWORD=MyS3cr37P450r.*-
        ...
        fortishield.dashboard:
          ...
          environment:
            - INDEXER_USERNAME=admin
            - INDEXER_PASSWORD=SecretPassword
            - FORTISHIELD_API_URL=https://fortishield.manager
            - DASHBOARD_USERNAME=kibanaserver
            - DASHBOARD_PASSWORD=kibanaserver
            - API_USERNAME=fortishield-wui
            - API_PASSWORD=MyS3cr37P450r.*-
        ...

#. Recreate the Fortishield containers:

   .. code-block:: console

      # docker-compose down
      # docker-compose up -d

Exposed ports
-------------

By default, the stack exposes the following ports:

+-----------+-----------------------------+
| **1514**  | Fortishield TCP                   |
+-----------+-----------------------------+
| **1515**  | Fortishield TCP                   |
+-----------+-----------------------------+
| **514**   | Fortishield UDP                   |
+-----------+-----------------------------+
| **55000** | Fortishield API                   |
+-----------+-----------------------------+
| **9200**  | Fortishield indexer  HTTPS        |
+-----------+-----------------------------+
| **443**   | Fortishield dashboard HTTPS       |
+-----------+-----------------------------+

.. note::

   Docker doesn’t reload the configuration dynamically. You need to restart the stack after changing the configuration of a component.
