.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn more about how to successfully install the Fortishield agent on Solaris systems in this section of our Installation Guide.

.. _fortishield_agent_solaris:

Installing Fortishield agents on Solaris endpoints
============================================

The agent runs on the host you want to monitor and communicates with the Fortishield manager, sending data in near real-time through an encrypted and authenticated channel.

To start the installation process, select your architecture: i386 or SPARC.

.. note:: You need root user privileges to run all the commands described below.

.. tabs::

   .. group-tab:: i386

      Select your Solaris Intel version.

      .. tabs::

         .. group-tab:: Solaris 10

            #. Download the `Fortishield agent for Solaris 10 i386 <https://packages.fortishield.com/4.x/solaris/i386/10/fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS10_i386|-sol10-i386.pkg>`_ package.

            #. Install the Fortishield agent.

               .. code-block:: console

                  # pkgadd -d fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS10_i386|-sol10-i386.pkg fortishield-agent

         .. group-tab:: Solaris 11

            #. Download the `Fortishield agent for Solaris 11 i386 <https://packages.fortishield.com/4.x/solaris/i386/11/fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_i386|-sol11-i386.p5p>`_.

            #. Install the Fortishield agent.

               .. code-block:: console

                  # pkg install -g fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_i386|-sol11-i386.p5p fortishield-agent

            If the Solaris 11 zone where you want to install the package has child zones, create a repository to install the Fortishield agent:

            .. code-block:: console

               # pkg set-publisher -g fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_i386|-sol11-i386.p5p fortishield && pkg install --accept fortishield-agent && pkg unset-publisher fortishield

   .. group-tab:: SPARC

      Select your Solaris SPARC version.

      .. tabs::

         .. group-tab:: Solaris 10

            #. Download the `Fortishield agent for Solaris 10 SPARC <https://packages.fortishield.com/4.x/solaris/sparc/10/fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS10_SPARC|-sol10-sparc.pkg>`_ package.

            #. Install the Fortishield agent.

               .. code-block:: console

                  # pkgadd -d fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS10_SPARC|-sol10-sparc.pkg fortishield-agent

         .. group-tab:: Solaris 11

            #. Download the `Fortishield agent for Solaris 11 SPARC <https://packages.fortishield.com/4.x/solaris/sparc/11/fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_SPARC|-sol11-sparc.p5p>`_.

            #. Install the Fortishield agent.

               .. code-block:: console

                  # pkg install -g fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_SPARC|-sol11-sparc.p5p fortishield-agent

            If the Solaris 11 zone where you want to install the package has child zones, create a repository to install the Fortishield agent:

            .. code-block:: console

               # pkg set-publisher -g fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_SPARC|-sol11-sparc.p5p fortishield && pkg install --accept fortishield-agent && pkg unset-publisher fortishield

The installation process is now complete, and the Fortishield agent is successfully installed on your Solaris endpoint. The next step is to register and configure the agent to communicate with the Fortishield server. To perform this action, see the :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>` section.

Uninstall a Fortishield agent
-----------------------

To uninstall the agent, select your Solaris version.

.. tabs::


  .. group-tab:: Solaris 10

    .. include:: ../../_templates/installations/fortishield/solaris/uninstall_fortishield_agent_s10.rst



  .. group-tab:: Solaris 11

    .. include:: ../../_templates/installations/fortishield/solaris/uninstall_fortishield_agent_s11.rst


The Fortishield agent is now completely removed from your Solaris endpoint.
