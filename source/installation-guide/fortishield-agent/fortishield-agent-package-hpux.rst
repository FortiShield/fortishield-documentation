.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn more about how to successfully install the Fortishield agent on HP-UX systems in this section of our Installation Guide.

.. _fortishield_agent_package_hpux:

Installing Fortishield agents on HP-UX endpoints
==========================================

The installed agent runs on the endpoint you want to monitor and communicates with the Fortishield server, sending data in near real-time through an encrypted and authenticated channel.

.. note:: You need root user privileges to run all the commands described below.

#. To start the installation process, download the `HP-UX installer <https://packages.fortishield.com/|FORTISHIELD_CURRENT_MAJOR_HPUX|/hp-ux/fortishield-agent-|FORTISHIELD_CURRENT_HPUX|-|FORTISHIELD_REVISION_HPUX|-hpux-11v3-ia64.tar>`_. 

#. Create the ``fortishield`` user and group.
   
   .. code-block:: console
   
       # groupadd fortishield
       # useradd -G fortishield fortishield
   
#. Uncompress the package in ``/``.

   .. code-block:: console
   
       # tar -xvf fortishield-agent-|FORTISHIELD_CURRENT_HPUX|-|FORTISHIELD_REVISION_HPUX|-hpux-11v3-ia64.tar


The installation process is now complete, and the Fortishield agent is successfully installed on your HP-UX endpoint. The next step is to register and configure the agent to communicate with the Fortishield server. To perform this action, see the :doc:`Linux/Unix agent enrollment via agent configuration </user-manual/agent-enrollment/via-agent-configuration/linux-endpoint>` section. To learn more about agent enrollment, visit :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>`.

Uninstall a Fortishield agent
-----------------------

To uninstall the agent, follow these steps: 

1. Stop the Fortishield agent service.

    .. code-block:: console

      # /var/ossec/bin/fortishield-control stop

2. Delete ``fortishield`` user and group:

    .. code-block:: console

        # groupdel fortishield
        # userdel fortishield

3. Remove Fortishield files.

    .. code-block:: console

      # rm -rf /var/ossec

The Fortishield agent is now completely removed from your HP-UX endpoint.