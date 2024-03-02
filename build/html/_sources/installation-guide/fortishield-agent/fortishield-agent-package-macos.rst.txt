.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn more about how to successfully install the Fortishield agent on macOS systems in this section of our Installation Guide.

Installing Fortishield agents on macOS endpoints
==========================================

The agent runs on the endpoint you want to monitor and communicates with the Fortishield server, sending data in near real-time through an encrypted and authenticated.

.. note:: You need root user privileges to run all the commands described below.

.. |macOS_intel_64| replace:: `fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_OSX|/macos/fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg>`__
.. |macOS_arm64| replace:: `fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_OSX|/macos/fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg>`__


#. To start the installation process, download the Fortishield agent according to your architecture:

   - **Intel**: |macOS_intel_64|. Suitable for macOS Sierra and later.

   - **Apple silicon**: |macOS_arm64|. Suitable for macOS Big Sur and later.

#. Select the installation method you want to follow: Command line interface (CLI) or graphical user interface (GUI).

   .. tabs::

      .. group-tab:: CLI
      
         #. To deploy the Fortishield agent on your endpoint, choose your architecture, edit the ``FORTISHIELD_MANAGER`` variable to contain your Fortishield manager IP address or hostname, and run the following command. 

            .. tabs::
            
               .. group-tab:: Intel

                  .. code-block:: console
                  
                     # echo "FORTISHIELD_MANAGER='10.0.0.2'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg -target /
   

               .. group-tab:: Apple silicon

                  .. versionadded:: 4.5.1

                  .. code-block:: console
                  
                     # echo "FORTISHIELD_MANAGER='10.0.0.2'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg -target /


               For additional deployment options such as agent name, agent group, and registration password, see the :doc:`Deployment variables for macOS </user-manual/deployment-variables/deployment-variables-macos>` section.
               
               .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables. To learn more about the different registration methods, see the :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>` section.

         #. To complete the installation process, start the Fortishield agent.

            .. code-block:: console

               # /Library/Ossec/bin/fortishield-control start


         The installation process is now complete, and the Fortishield agent is successfully deployed and running on your macOS endpoint.

      
      .. group-tab:: GUI

         #. To install the Fortishield agent on your system, run the downloaded file and follow the steps in the installation wizard. If you are not sure how to answer some of the prompts, use the default answers.

            .. thumbnail:: ../../images/installation/macos-agent.png
               :align: center
               :title: macOS agent installer
               :alt: macOS agent installer
               
         #. To complete the installation process, start the Fortishield agent.

            .. code-block:: console

               # sudo /Library/Ossec/bin/fortishield-control start

         The installation process is now complete, and the Fortishield agent is successfully installed on your macOS endpoint. The next step is to register and configure the agent to communicate with the Fortishield server. To perform this action, see the :doc:`Fortishield agent enrollment </user-manual/agent-enrollment/index>` section.  

By default, all agent files are stored in ``/Library/Ossec/`` after the installation.

Uninstall a Fortishield agent
-----------------------

To uninstall the agent, follow these steps: 

#. Stop the Fortishield agent service.

    .. code-block:: console

      # /Library/Ossec/bin/fortishield-control stop

#. Remove the ``/Library/Ossec/`` folder.

    .. code-block:: console

      # /bin/rm -r /Library/Ossec

#. Stop and unload dispatcher.

    .. code-block:: console

      # /bin/launchctl unload /Library/LaunchDaemons/com.fortishield.agent.plist

#. Remove ``launchdaemons`` and ``StartupItems``.

    .. code-block:: console

      # /bin/rm -f /Library/LaunchDaemons/com.fortishield.agent.plist
      # /bin/rm -rf /Library/StartupItems/FORTISHIELD

#. Remove the Fortishield user and group.

    .. code-block:: console

      # /usr/bin/dscl . -delete "/Users/fortishield"
      # /usr/bin/dscl . -delete "/Groups/fortishield"

#. Remove from ``pkgutil``.

    .. code-block:: console

      # /usr/sbin/pkgutil --forget com.fortishield.pkg.fortishield-agent

The Fortishield agent is now completely removed from your macOS endpoint.
