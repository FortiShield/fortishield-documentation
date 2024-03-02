.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: How to migrate data from Fortishield 4.2 with Open Distro to Fortishield Indexer in Docker production deployments.

Migrating data from Opendistro to the Fortishield indexer
===================================================

.. note::
   
   This guide assumes that you previously deployed the version 4.2.x production cluster. 

This guide shows how to migrate data from Opendistro to Fortishield Indexer in Docker production deployments (v4.2.x to v|FORTISHIELD_CURRENT_MINOR_DOCKER|). This procedure also upgrades the other Fortishield components to the most recent versions.

#. Run the following command from the ``fortishield-docker`` directory to stop the current v4.2.x environment: 

   .. code-block:: console

      # docker-compose -f production-cluster.yml stop

#. Check that Elasticsearch volumes are present:

   .. code-block:: console

      # docker volume ls --filter name='fortishield-docker_elastic-data'

#. Inspect Elasticsearch volumes and save the ``com.docker.compose.version`` value to use it in step 7:

   .. code-block:: console

      # docker volume inspect fortishield-docker_elastic-data-1

#. Stop and remove the containers of the current v4.2.x environment:

   .. code-block:: console

      # docker-compose -f production-cluster.yml down

#. Exit the current ``fortishield-docker`` directory and rename it to ``fortishield-docker-4.2.X``. 

#. Clone the Fortishield |FORTISHIELD_CURRENT_MINOR_DOCKER| repository to your system:

   .. code-block:: console

      # git clone https://github.com/fortishield/fortishield-docker.git -b v|FORTISHIELD_CURRENT_DOCKER|

#. Navigate to the ``multi-node`` directory and run the ``volume-migrator`` script. This script creates new volumes for |FORTISHIELD_CURRENT_MINOR_DOCKER| and copies data from old volumes to the newly created volumes. Use the Docker-compose version and project name as the arguments. You can see an example below. You can also do this step manually, see steps 5 and 6 in Fortishield Docker `Github <https://github.com/fortishield/fortishield-docker/blob/v|FORTISHIELD_CURRENT_DOCKER|/multi-node/Migration-to-Fortishield-4.4.md>`__:

   .. code-block:: console

      # ./volume-migrator.sh 1.29.2 multi-node

#. Start the |FORTISHIELD_CURRENT_MINOR_DOCKER| environment:

   .. code-block:: console

      # docker-compose -f generate-indexer-certs.yml run --rm generator
      # docker-compose up -d
