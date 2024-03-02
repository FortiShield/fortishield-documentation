.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Check the tasks that help you benefit the most from the installation of Fortishield after the installation of the Fortishield-Docker. 
  
Fortishield Docker utilities
======================

After installing the Fortishield-Docker containers, there are several tasks you can do to benefit the most from your Fortishield installation.

..
   .. contents::
      :local:
      :depth: 1
      :backlinks: none

Access to services and containers
---------------------------------

#. Access the Fortishield dashboard using the Docker host IP address. For example, ``https://localhost``, if you are on the Docker host.

   .. note::

      In case you use a self-signed certificate, your browser will warn that it cannot verify its authenticity.

#. Enroll the agents by following the standard enrollment process and using the Docker host address as the manager address. For more information, see the :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>` documentation.

#. List the containers in the directory where the Fortishield ``docker-compose.yml`` file is located:

   .. code-block:: console

      # docker-compose ps

   .. code-block:: none
      :class: output

      NAME                            COMMAND                  SERVICE             STATUS              PORTS
      single-node-fortishield.dashboard-1   "/entrypoint.sh"         fortishield.dashboard     running             443/tcp, 0.0.0.0:443->5601/tcp
      single-node-fortishield.indexer-1     "/entrypoint.sh open…"   fortishield.indexer       running             0.0.0.0:9200->9200/tcp
      single-node-fortishield.manager-1     "/init"                  fortishield.manager       running             0.0.0.0:1514-1515->1514-1515/tcp, 0.0.0.0:514->514/udp, 0.0.0.0:55000->55000/tcp, 1516/tcp

#. Run the command below from the directory where the ``docker-compose.yml`` file is located to access the command line of each container:

   .. code-block:: console

      # docker-compose exec <SERVICE> bash

Fortishield service data volumes
--------------------------

You can set Fortishield configuration and log files to exist outside their containers. This allows the files to persist after removing containers, and you can provision custom configuration files to your containers.

You need multiple volumes to ensure persistence on a Fortishield container. The following is an example of a ``docker-compose.yml`` with persistent volumes:

.. code-block:: yaml

   services:
     fortishield:
       . . .
       volumes:
         - fortishield_api_configuration:/var/ossec/api/configuration

   volumes:
     fortishield_api_configuration:

You can list persistent volumes with ``docker volume ls``:

.. code-block:: none
   :class: output

   DRIVER              VOLUME NAME
   local               single-node_fortishield_api_configuration

Storage volume for Fortishield indexer and dashboard
----------------------------------------------

Attaching a volume for the storage of Fortishield indexer data is also possible. By default, the single-node and multi-node deployments already have volumes configured. An example of a single-node fortishield indexer volume is shown in the ``docker-compose.yml`` below:

.. code-block:: yaml

   fortishield.indexer:
       . . .
        volumes:
          - fortishield-indexer-data:/var/lib/fortishield-indexer

       . . .

   volumes:
     fortishield-indexer-data


Custom commands and scripts
---------------------------

To execute commands in the Fortishield manager container, you can execute a shell:

.. code-block:: console

   # docker exec -it single-node-fortishield.manager-1 bash

Every change made on this shell persists as long as you have the data volumes configured correctly.
