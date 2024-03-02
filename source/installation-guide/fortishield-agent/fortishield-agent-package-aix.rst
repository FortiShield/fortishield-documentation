.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn how to deploy the Fortishield agent on AIX using deployment variables that facilitate the task of installing, registering, and configuring the agent. 

.. _fortishield_agent_package_aix:

Deploying Fortishield agents on AIX endpoints
=======================================

The agent runs on the endpoint you want to monitor and communicates with the Fortishield server, sending data in near real-time through an encrypted and authenticated channel. 

The deployment of a Fortishield agent on an AIX system uses deployment variables that facilitate the task of installing, registering, and configuring the agent. 

.. note:: You need root user privileges to run all the commands described below.

#. To start the deployment process, download the `AIX installer <https://packages.fortishield.com/|FORTISHIELD_CURRENT_MAJOR_AIX|/aix/fortishield-agent-|FORTISHIELD_CURRENT_AIX|-|FORTISHIELD_REVISION_AIX|.aix.ppc.rpm>`_. 

#. To deploy the Fortishield agent to your endpoint, edit the ``FORTISHIELD_MANAGER`` variable so that it contains the Fortishield manager IP address or hostname.

   .. code-block:: console
   
      # FORTISHIELD_MANAGER="10.0.0.2" rpm -ivh fortishield-agent-|FORTISHIELD_CURRENT_AIX|-|FORTISHIELD_REVISION_AIX|.aix.ppc.rpm

   For additional deployment options such as agent name, agent group, and registration password, see :doc:`Deployment variables for AIX </user-manual/deployment-variables/deployment-variables-aix>` section.   
   
   .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables.  To learn more about the different registration methods, see the :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>` section.

#. To complete the installation process, start the Fortishield agent.

    .. code-block:: console

      # /var/ossec/bin/fortishield-control start

      
The deployment process is now complete, and the Fortishield agent is successfully running on your AIX endpoint.
      

Uninstall a Fortishield agent
-----------------------

To uninstall the agent, run the following command:

    .. code-block:: console

      # rpm -e fortishield-agent

   Some files are not removed from the filesystem by the package manager. If you want to completely remove all files, delete the ``/var/ossec`` folder. 

The Fortishield agent is now completely removed from your AIX system
