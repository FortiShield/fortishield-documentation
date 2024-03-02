.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn more about upgrading the Fortishield deployment on Docker in this section of our documentation. 

Upgrading Fortishield Docker
======================

This section describes how to upgrade your Fortishield Docker deployment, starting from version 4.3. To upgrade Fortishield deployments of versions earlier than 4.3, refer to the :doc:`/deployment-options/docker/data-migration` documentation.

To upgrade to version |FORTISHIELD_CURRENT_MINOR|, you can follow one of two strategies.

- `Using default docker-compose files`_ : This strategy uses the default docker-compose files for Fortishield |FORTISHIELD_CURRENT_MINOR|. It replaces the docker-compose files of your outdated Fortishield version. 
- `Keeping custom docker-compose files`_ : This strategy preserves the docker-compose files of your outdated Fortishield deployment. It ignores the docker-compose files of the latest Fortishield version. 

Using default docker-compose files
----------------------------------

#. Run the following command from your fortishield-docker directory, such as ``fortishield-docker/single-node/`` or ``fortishield-docker/multi-node/``, to stop the outdated environment:

   .. code-block::

      # docker-compose down

#. Checkout the tag for the current version of fortishield-docker:

      .. code-block::

         # git checkout v|FORTISHIELD_CURRENT_DOCKER|

#. Start the new version of Fortishield using ``docker-compose``:

   .. code-block::

      # docker-compose up -d

Keeping custom docker-compose files
-----------------------------------

In Fortishield 4.4, some paths are different to those in earlier versions. You have to update the old paths with the new ones.

``old-path`` -> ``new-path``

-  ``/usr/share/fortishield-dashboard/config/certs/`` -> ``/usr/share/fortishield-dashboard/certs/``
-  ``/usr/share/fortishield-indexer/config/certs/`` -> ``/usr/share/fortishield-indexer/certs/``
-  ``/usr/share/fortishield-indexer/plugins/opensearch-security/securityconfig/`` -> ``/usr/share/fortishield-indexer/opensearch-security/``

To upgrade your deployment keeping your custom docker-compose files, do the following.

#. Run the following command from your fortishield-docker directory, such as ``fortishield-docker/single-node/`` or ``fortishield-docker/multi-node/``, to stop the outdated environment:

   .. code-block::

      # docker-compose down

#. If you are updating from 4.3, edit ``docker-compose.yml`` and update it with the new paths in 4.4. You can see the new paths for single node docker compose files, such as  ``single-node/docker-compose.yml`` below. For multi node docker compose files, such as  ``multi-node/docker-compose.yml``, you need to do similar changes in the corresponding files.

   .. code-block:: yaml
      :emphasize-lines: 8-12, 14, 19-21

      fortishield.manager:
         image: fortishield/fortishield-manager:|FORTISHIELD_CURRENT_KUBERNETES|
      ...
      fortishield.indexer:
         image: fortishield/fortishield-indexer:|FORTISHIELD_CURRENT_KUBERNETES|
         volumes:
            - fortishield-indexer-data:/var/lib/fortishield-indexer
            - ./config/fortishield_indexer_ssl_certs/root-ca.pem:/usr/share/fortishield-indexer/certs/root-ca.pem
            - ./config/fortishield_indexer_ssl_certs/fortishield.indexer-key.pem:/usr/share/fortishield-indexer/certs/fortishield.indexer.key
            - ./config/fortishield_indexer_ssl_certs/fortishield.indexer.pem:/usr/share/fortishield-indexer/certs/fortishield.indexer.pem
            - ./config/fortishield_indexer_ssl_certs/admin.pem:/usr/share/fortishield-indexer/certs/admin.pem
            - ./config/fortishield_indexer_ssl_certs/admin-key.pem:/usr/share/fortishield-indexer/certs/admin-key.pem
            - ./config/fortishield_indexer/fortishield.indexer.yml:/usr/share/fortishield-indexer/opensearch.yml
            - ./config/fortishield_indexer/internal_users.yml:/usr/share/fortishield-indexer/opensearch-security/internal_users.yml
      ...
      fortishield.dashboard:
         image: fortishield/fortishield-dashboard:|FORTISHIELD_CURRENT_KUBERNETES|
         volumes:
            - ./config/fortishield_indexer_ssl_certs/fortishield.dashboard.pem:/usr/share/fortishield-dashboard/certs/fortishield-dashboard.pem
            - ./config/fortishield_indexer_ssl_certs/fortishield.dashboard-key.pem:/usr/share/fortishield-dashboard/certs/fortishield-dashboard-key.pem
            - ./config/fortishield_indexer_ssl_certs/root-ca.pem:/usr/share/fortishield-dashboard/certs/root-ca.pem
            - ./config/fortishield_dashboard/opensearch_dashboards.yml:/usr/share/fortishield-dashboard/config/opensearch_dashboards.yml
            - ./config/fortishield_dashboard/fortishield.yml:/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml

#. Start the new version of Fortishield using ``docker-compose``:

   .. code-block::

      # docker-compose up -d            

