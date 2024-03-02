
.. Copyright (C) 2015, Fortishield, Inc.
.. meta::
  :description: Check out how to upgrade the Fortishield agent to the latest available version remotely, using the agent_upgrade tool or the Fortishield API, or locally.


Upgrading Fortishield agents on macOS systems
=======================================

Follow these steps to upgrade Fortishield agents locally on macOS systems. If you want to perform a remote upgrade, check the :doc:`Remote agent upgrade </user-manual/agents/remote-upgrading/upgrading-agent>` section to learn more. 

.. note:: To perform the agent upgrade, administrator privileges are required.

.. |macOS_intel_64| replace:: `fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg <https://packages.fortishield.com/|FORTISHIELD_CURRENT_MAJOR_OSX|/macos/fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg>`__
.. |macOS_arm64| replace:: `fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg <https://packages.fortishield.com/|FORTISHIELD_CURRENT_MAJOR_OSX|/macos/fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg>`__


#. Download the latest macOS installer:

   - **Intel**: |macOS_intel_64|.

   - **Apple silicon**: |macOS_arm64|.

#. Run the macOS installer by using the command line interface (CLI) or the graphical user interface (GUI).

   .. tabs::
    
      .. group-tab:: CLI

         To upgrade the Fortishield agent by using the command line, select your architecture, and run the installer:
         
         .. tabs::

            .. group-tab:: Intel
         
               .. code-block:: console

                  # installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg -target /


            .. group-tab:: Apple silicon
         
               .. code-block:: console

                  # installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg -target /

               .. note::
                  
                  Packages earlier than 4.5.1 are not available for ARM64 architectures.

      .. group-tab:: GUI

         Using the GUI will perform a simple upgrade. Double click on the downloaded file and follow the wizard. If you are not sure how to answer some of the prompts, simply use the default answers.

         .. thumbnail:: ../../images/installation/macos-agent.png
            :align: center
            :title: macOS agent installer
            :alt: macOS agent installer            


.. note::
   :class: not-long

   When upgrading agents from versions earlier than 4.x, make sure that the communication protocol is compatible. Up to that point, UDP was the default protocol and it was switched to TCP for later versions. Edit the agent configuration file ``ossec.conf`` to update the :ref:`protocol <server_protocol>` or make sure that your Fortishield manager accepts :ref:`both protocols<manager_protocol>`. 

  