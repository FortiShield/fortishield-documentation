.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn more about the process of installing and configuring the Fortishield deployment on Docker in this section of our documentation. 

Deployment on Docker
====================

This section details the process of installing Fortishield on Docker.

`Docker <https://www.docker.com/>`_ is an open platform for building, delivering, and running applications inside software containers. Docker containers package up software, including everything needed to run: code, runtime, system tools, system libraries, and settings. Docker enables separating applications from infrastructure. This guarantees that the application always runs the same, regardless of the environment the container is running on. Containers run in the cloud or on-premises.

You can install Fortishield using the Docker images we have created, such as ``fortishield/fortishield-manager``, ``fortishield/fortishield-indexer`` and ``fortishield/fortishield-dashboard``. You can find all the Fortishield Docker images in the `Docker hub <https://hub.docker.com/u/fortishield>`_.

In the :doc:`/deployment-options/docker/docker-installation` section, you can see how to install Docker. You can find how to install Fortishield on Docker in the :doc:`/deployment-options/docker/fortishield-container`. Read the :doc:`/deployment-options/docker/container-usage` section to learn how to access the services and containers, manage data volumes, and execute a shell. Finally, you can find answers to some frequent questions in the :doc:`/deployment-options/docker/faq-fortishield-container`.


.. toctree::
   :maxdepth: 1
   :hidden:

   docker-installation
   fortishield-container
   container-usage
   upgrading-fortishield-docker
   data-migration
   faq-fortishield-container
