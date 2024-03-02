
.. Copyright (C) 2015, Fortishield, Inc.
.. meta::
  :description: Check out how to upgrade the Fortishield agent to the latest available version remotely, using the agent_upgrade tool or the Fortishield API, or locally.


Upgrading Fortishield agents on Windows systems
=========================================

Follow these steps to upgrade Fortishield agents locally on Windows systems. If you want to perform a remote upgrade, check the :doc:`Remote agent upgrade </user-manual/agents/remote-upgrading/upgrading-agent>` section to learn more. 

.. note:: To perform the agent upgrade, administrator privileges are required.

#. Download the latest `Windows installer <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_WINDOWS|/windows/fortishield-agent-|FORTISHIELD_CURRENT_WINDOWS|-|FORTISHIELD_REVISION_WINDOWS|.msi>`_. 

#. Run the Windows installer by using the command line interface (CLI) or the graphical user interface (GUI).


   .. tabs::
    
      .. group-tab:: CLI

         To upgrade the Fortishield agent from the command line, run the installer using Windows PowerShell or the command prompt. The ``/q`` argument is used for unattended installations.

            .. code-block:: none

               # .\fortishield-agent-|FORTISHIELD_CURRENT_WINDOWS|-|FORTISHIELD_REVISION_WINDOWS|.msi /q


      .. group-tab:: GUI

         Open the installer and follow the instructions to upgrade the Fortishield agent.

            .. thumbnail:: /images/installation/windows.png
              :title: Windows agent setup window
              :alt: Windows agent setup Window
              :align: center
              :width: 100%
   

.. note::
   :class: not-long

   When upgrading agents from versions earlier than 4.x, make sure that the communication protocol is compatible. Up to that point, UDP was the default protocol and it was switched to TCP for later versions. Edit the agent configuration file ``ossec.conf`` to update the :ref:`protocol <server_protocol>` or make sure that your Fortishield manager accepts :ref:`both protocols<manager_protocol>`. 
               