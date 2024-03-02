.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Get answers to the most frequently asked questions about the Fortishield deployment on Docker in this FAQ. 
    
FAQ
===

How can I tune the Fortishield dashboard configuration?
-------------------------------------------------

The Fortishield dashboard reads its configuration from ``config/fortishield_dashboard/opensearch_dashboards.yml``:

.. code-block:: yaml

    fortishield-dashboard:
    ...
    volumes:
      - ./custom_opensearch_dashboards.yml:/usr/share/fortishield-dashboard/opensearch_dashboards.yml

Read the `YAML files Opensearch documentation <https://opensearch.org/docs/latest/security-plugin/configuration/yaml/#opensearchyml>`__ to know more about the variables you can use on this image.

How can I tune the Fortishield indexer configuration?
-----------------------------------------------

The Fortishield indexer container uses the default configuration, and it’s not exposed by default.

If you want to override the default configuration, create a file ``config/fortishield_indexer/<new_fortishield_indexer>.yml`` and add your custom version of the configuration to it. Then map your configuration file inside the container in the ``docker-compose.yml``. Update the Fortishield indexer container declaration to:

.. code-block:: yaml

    <new_fortishield_indexer>:
      image: fortishield/fortishield-indexer:latest
      ports:
        - "9200:9200"
        - "9300:9300"
      environment:
        ES_JAVA_OPTS: "-Xms6g -Xmx6g"
      networks:
        - docker_fortishield

How can I store the Fortishield indexer data?
---------------------------------------

The data stored in the Fortishield indexer persists after container reboots but not after container removal.

By default, the single-node and multi-node deployments already have volumes configured. For example, see  ``fortishield1.indexer`` volume in the multi-node ``docker-compose.yml`` file:

.. code-block:: yaml

   fortishield1.indexer:
    ...
    volumes:
      - fortishield-indexer-data-1:/var/lib/fortishield-indexer

This stores Fortishield indexer data inside ``fortishield-indexer-data-1`` volume in the Docker host local file system.
