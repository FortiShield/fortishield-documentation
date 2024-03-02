.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn about the variables that facilitate the deployment of the Fortishield agent on macOS in this section of our documentation.
  
.. _deployment_variables_macos:

Deployment variables for macOS
==============================

For an agent to be fully deployed and connected to the Fortishield server, it needs to be installed, registered, and configured. The installers can use variables that allow configuration provisioning to make the process simple.

Below you can find a table describing the variables used by Fortishield installers, and a few examples of how to use them.


+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                           | Description                                                                                                                                                                                          |
+==================================+======================================================================================================================================================================================================+
|   FORTISHIELD_MANAGER                  |  Specifies the manager IP address or hostname. If you want to specify multiple managers, you can add them separated by commas. See :ref:`address <server_address>`.                                  |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_MANAGER_PORT             |  Specifies the manager connection port. See :ref:`port <server_port>`.                                                                                                                               |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_PROTOCOL                 |  Sets the communication protocol between the manager and the agent. Accepts UDP and TCP. The default is TCP. See :ref:`protocol <server_protocol>`.                                                  |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_REGISTRATION_SERVER      |  Specifies the Fortishield registration server used for the agent registration. See :ref:`manager_address <enrollment_manager_address>`. If empty, the value set in ``FORTISHIELD_MANAGER`` will be used.        |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_REGISTRATION_PORT        |  Specifies the port used by the Fortishield registration server. See :ref:`port <enrollment_manager_port>`.                                                                                                |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_REGISTRATION_PASSWORD    |  Sets password used to authenticate during register, stored in ``etc/authd.pass``. See :ref:`authorization_pass_path <enrollment_authorization_pass_path>`                                           |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_KEEP_ALIVE_INTERVAL      |  Sets the time between agent checks for manager connection. See :ref:`notify_time <notify_time>`.                                                                                                    |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_TIME_RECONNECT           |  Sets the time interval for the agent to reconnect with the Fortishield manager when connectivity is lost. See :ref:`time-reconnect  <time_reconnect>`.                                                    |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_REGISTRATION_CA          |  Host SSL validation need of Certificate of Authority. This option specifies the CA path. See :ref:`server_ca_path <enrollment_server_ca_path>`.                                                     |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_REGISTRATION_CERTIFICATE |  The SSL agent verification needs a CA signed certificate and the respective key. This option specifies the certificate path. See :ref:`agent_certificate_path <enrollment_agent_certificate_path>`. |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_REGISTRATION_KEY         |  Specifies the key path completing the required variables with FORTISHIELD_REGISTRATION_CERTIFICATE for the SSL agent verification process. See :ref:`agent_key_path <enrollment_agent_key_path>`.         |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_AGENT_NAME               |  Designates the agent's name. By default it will be the computer name. See :ref:`agent_name <enrollment_agent_name>`.                                                                                |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   FORTISHIELD_AGENT_GROUP              |  Assigns the agent to one or more existing groups (separated by commas). See :ref:`agent_groups <enrollment_agent_groups>`.                                                                          |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   ENROLLMENT_DELAY               |  Assigns the time that agentd should wait after a successful registration. See :ref:`delay_after_enrollment <enrollment_delay_after_enrollment>`.                                                    |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Examples:

.. tabs::

   .. group-tab:: Intel
    
      -  Registration with password:

         .. code-block:: console
         
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_PASSWORD='TopSecret' && \
            FORTISHIELD_AGENT_NAME='macos-agent'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg -target /

      -  Registration with password and assigning a group:

         .. code-block:: console
         
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && FORTISHIELD_REGISTRATION_PASSWORD='TopSecret' && \
            FORTISHIELD_AGENT_GROUP='my-group'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg -target /            

      -  Registration with relative path to CA. It will be searched at your Fortishield installation folder:

         .. code-block:: console
         
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && FORTISHIELD_AGENT_NAME='macos-agent' && \
            FORTISHIELD_REGISTRATION_CA='rootCA.pem'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg -target /

      -  Registration with protocol:

         .. code-block:: console
      
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && FORTISHIELD_AGENT_NAME='macos-agent' && \
            FORTISHIELD_PROTOCOL='udp'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg -target /

      -  Registration and adding multiple address:

         .. code-block:: console
      
            # echo "FORTISHIELD_MANAGER='10.0.0.2,10.0.0.3' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && \
            FORTISHIELD_AGENT_NAME='macos-agent'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg -target /

      -  Absolute paths to CA, certificate or key that contain spaces can be written as shown below:

         .. code-block:: console
      
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && FORTISHIELD_REGISTRATION_KEY='/var/ossec/etc/sslagent.key' && \
            FORTISHIELD_REGISTRATION_CERTIFICATE='/var/ossec/etc/sslagent.cert'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.intel64.pkg -target /

   .. group-tab:: Apple silicon
    
      -  Registration with password:

         .. code-block:: console
         
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_PASSWORD='TopSecret' && \
            FORTISHIELD_AGENT_NAME='macos-agent'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg -target /

      -  Registration with password and assigning a group:

         .. code-block:: console
         
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && FORTISHIELD_REGISTRATION_PASSWORD='TopSecret' && \
            FORTISHIELD_AGENT_GROUP='my-group'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg -target /            

      -  Registration with relative path to CA. It will be searched at your Fortishield installation folder:

         .. code-block:: console
         
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && FORTISHIELD_AGENT_NAME='macos-agent' && \
            FORTISHIELD_REGISTRATION_CA='rootCA.pem'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg -target /

      -  Registration with protocol:

         .. code-block:: console
      
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && FORTISHIELD_AGENT_NAME='macos-agent' && \
            FORTISHIELD_PROTOCOL='udp'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg -target /

      -  Registration and adding multiple address:

         .. code-block:: console
      
            # echo "FORTISHIELD_MANAGER='10.0.0.2,10.0.0.3' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && \
            FORTISHIELD_AGENT_NAME='macos-agent'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg -target /

      -  Absolute paths to CA, certificate or key that contain spaces can be written as shown below:

         .. code-block:: console
      
            # echo "FORTISHIELD_MANAGER='10.0.0.2' && FORTISHIELD_REGISTRATION_SERVER='10.0.0.2' && FORTISHIELD_REGISTRATION_KEY='/var/ossec/etc/sslagent.key' && \
            FORTISHIELD_REGISTRATION_CERTIFICATE='/var/ossec/etc/sslagent.cert'" > /tmp/fortishield_envs && installer -pkg fortishield-agent-|FORTISHIELD_CURRENT_OSX|-|FORTISHIELD_REVISION_OSX|.arm64.pkg -target /

.. note:: It’s necessary to use both KEY and PEM options to verify agents' identities with the registration server. See the :ref:`Registration Service with host verification - Agent verification with host validation <enrollment_additional_security>` section.
