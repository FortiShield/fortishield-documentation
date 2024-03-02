.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn how to deploy the Fortishield agent on Linux with deployment variables that facilitate the task of installing, registering, and configuring the agent. 

.. _fortishield_agent_package_linux:

Deploying Fortishield agents on Linux endpoints
=========================================

The agent runs on the host you want to monitor and communicates with the Fortishield server, sending data in near real-time through an encrypted and authenticated channel. 

The deployment of a Fortishield agent on a Linux system uses deployment variables that facilitate the task of installing, registering, and configuring the agent. Alternatively, if you want to download the Fortishield agent package directly, see the :doc:`packages list </installation-guide/packages-list>` section. 

.. note:: You need root user privileges to run all the commands described below.

Add the Fortishield repository
-------------------------

Add the Fortishield repository to download the official packages. 

.. tabs::


  .. group-tab:: Yum


    .. include:: ../../_templates/installations/fortishield/yum/add_repository.rst



  .. group-tab:: APT


    .. include:: ../../_templates/installations/fortishield/deb/add_repository.rst



  .. group-tab:: ZYpp


    .. include:: ../../_templates/installations/fortishield/zypp/add_repository.rst



  .. group-tab:: APK


    .. include:: ../../_templates/installations/fortishield/apk/add_repository.rst



Deploy a Fortishield agent
--------------------

#. To deploy the Fortishield agent on your endpoint, select your package manager and edit the ``FORTISHIELD_MANAGER`` variable to contain your Fortishield manager IP address or hostname.   

   .. tabs::
   
      .. group-tab:: Yum
   
         .. code-block:: console
          
            # FORTISHIELD_MANAGER="10.0.0.2" yum install fortishield-agent|FORTISHIELD_AGENT_RPM_PKG_INSTALL|

         For additional deployment options such as agent name, agent group, and registration password, see the :doc:`Deployment variables for Linux </user-manual/deployment-variables/deployment-variables-linux>` section.

          .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables. To learn more about the different registration methods, see the :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>` section. 
   
      .. group-tab:: APT
   
         .. code-block:: console
          
            # FORTISHIELD_MANAGER="10.0.0.2" apt-get install fortishield-agent|FORTISHIELD_AGENT_DEB_PKG_INSTALL|

         For additional deployment options such as agent name, agent group, and registration password, see the :doc:`Deployment variables for Linux </user-manual/deployment-variables/deployment-variables-linux>` section.

         .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables. To learn more about the different registration methods, see the :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>` section. 
   
      .. group-tab:: ZYpp
   
         .. code-block:: console
          
            # FORTISHIELD_MANAGER="10.0.0.2" zypper install fortishield-agent|FORTISHIELD_AGENT_ZYPP_PKG_INSTALL|

         For additional deployment options such as agent name, agent group, and registration password, see the :doc:`Deployment variables for Linux </user-manual/deployment-variables/deployment-variables-linux>` section.

         .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables. To learn more about the different registration methods, see the :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>` section. 

      .. group-tab:: APK
   
         #. Install the Fortishield agent:

            .. code-block:: console
            
               # apk add fortishield-agent|FORTISHIELD_AGENT_APK_PKG_INSTALL|

         #. Edit the agent configuration to add the address of your Fortishield manager:

            .. code-block:: console
            
               # export FORTISHIELD_MANAGER="10.0.0.2" && sed -i "s|MANAGER_IP|$FORTISHIELD_MANAGER|g" /var/ossec/etc/ossec.conf

            For more customization options, like agent name or group, see the :doc:`Linux/Unix endpoint configuration </user-manual/agent-enrollment/via-agent-configuration/linux-endpoint>` page. For more security options, check the :doc:`Additional security options </user-manual/agent-enrollment/security-options/index>` section. 

#. Enable and start the Fortishield agent service.

   .. include:: ../../_templates/installations/fortishield/common/enable_fortishield_agent_service.rst

The deployment process is now complete, and the Fortishield agent is successfully running on your Linux system. 

- **Recommended action** -  Disable Fortishield updates

  Compatibility between the Fortishield agent and the Fortishield manager is guaranteed when the Fortishield manager version is later than or equal to that of the Fortishield agent. Therefore, we recommend disabling the Fortishield repository to prevent accidental upgrades. To do so, use the following command:

    .. tabs::


      .. group-tab:: Yum


        .. include:: ../../_templates/installations/fortishield/yum/disabling_repository.rst



      .. group-tab:: APT


        .. include:: ../../_templates/installations/fortishield/deb/disabling_repository.rst



      .. group-tab:: ZYpp

        .. include:: ../../_templates/installations/fortishield/zypp/disabling_repository.rst



      .. group-tab:: APK

        .. include:: ../../_templates/installations/fortishield/apk/disabling_repository.rst


Uninstall a Fortishield agent
-----------------------

To uninstall the agent, run the following commands:


#. Remove the Fortishield agent installation. 


   .. tabs::
 
 
     .. group-tab:: Yum
 
 
       .. include:: ../../_templates/installations/fortishield/yum/uninstall_fortishield_agent.rst
 
 
 
     .. group-tab:: APT
 
 
       .. include:: ../../_templates/installations/fortishield/deb/uninstall_fortishield_agent.rst
 
 
 
     .. group-tab:: ZYpp
 
 
       .. include:: ../../_templates/installations/fortishield/zypp/uninstall_fortishield_agent.rst



     .. group-tab:: APK
 
 
       .. include:: ../../_templates/installations/fortishield/apk/uninstall_fortishield_agent.rst



#. Disable the Fortishield agent service. 

   .. include:: ../../_templates/installations/fortishield/common/disable_fortishield_agent_service.rst


The Fortishield agent is now completely removed from your Linux endpoint.
