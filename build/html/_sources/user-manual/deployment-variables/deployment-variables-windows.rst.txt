.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn about the variables that facilitate the deployment of the Fortishield agent on Windows in this section of our documentation.

.. _deployment_variables_windows:

Deployment variables for Windows
================================

For an agent to be fully deployed and connected to the Fortishield server, it needs to be installed, registered, and configured. The installers can use variables that allow configuration provisioning to make the process simple.

Below you can find a table describing the variables used by Fortishield installers on Windows and a few examples of how to use them.


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
|   FORTISHIELD_REGISTRATION_PASSWORD    |  Sets the registration password by storing it in the ``authd.pass`` file. See :ref:`authorization_pass_path <enrollment_authorization_pass_path>`.                                                   |
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
|   \/l  installer.log             |  Generates a log of the installation process.                                                                                                                                                        |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \/l\*v installer.log             |  Generates a log of the installation process, including verbose messages.                                                                                                                            |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note:: In PowerShell, use ``"""`` or ``'""`` if the deployment variable contains spaces. For example, ``FORTISHIELD_REGISTRATION_PASSWORD="""TOP SECRET"""``                                                        

Below there are some examples to install and register a Windows agent.

Registration with password::

    fortishield-agent-|FORTISHIELD_CURRENT_WINDOWS|-|FORTISHIELD_REVISION_WINDOWS|.msi /q FORTISHIELD_MANAGER="10.0.0.2" FORTISHIELD_REGISTRATION_SERVER="10.0.0.2" FORTISHIELD_REGISTRATION_PASSWORD="TopSecret" FORTISHIELD_AGENT_NAME="W2012"

Registration with password and assigning a group::

    fortishield-agent-|FORTISHIELD_CURRENT_WINDOWS|-|FORTISHIELD_REVISION_WINDOWS|.msi /q FORTISHIELD_MANAGER="10.0.0.2" FORTISHIELD_REGISTRATION_SERVER="10.0.0.2" FORTISHIELD_REGISTRATION_PASSWORD="TopSecret" FORTISHIELD_AGENT_GROUP="my-group"

Registration with relative path to CA. It will be searched at your Fortishield installation folder::

    fortishield-agent-|FORTISHIELD_CURRENT_WINDOWS|-|FORTISHIELD_REVISION_WINDOWS|.msi /q FORTISHIELD_MANAGER="10.0.0.2" FORTISHIELD_REGISTRATION_SERVER="10.0.0.2" FORTISHIELD_AGENT_NAME="W2019" FORTISHIELD_REGISTRATION_CA="rootCA.pem"

Absolute paths to CA, certificate or key that contain spaces can be written as shown below::

    fortishield-agent-|FORTISHIELD_CURRENT_WINDOWS|-|FORTISHIELD_REVISION_WINDOWS|.msi /q FORTISHIELD_MANAGER="10.0.0.2" FORTISHIELD_REGISTRATION_SERVER="10.0.0.2" FORTISHIELD_REGISTRATION_KEY="C:\Progra~2\sslagent.key" FORTISHIELD_REGISTRATION_CERTIFICATE="C:\Progra~2\sslagent.cert"

The number "2" means that the file will be searched at the second occurrence of the "Progra" word, thus, the key and certificate would be searched at the folder "C:\\Program Files (x86)". In case this number was "1", it would be searched at "Program Files".

.. note::
    It's necessary to use both FORTISHIELD_REGISTRATION_KEY and FORTISHIELD_REGISTRATION_CERTIFICATE options to verify agents via SSL. See the :ref:`verify hosts with SSL <enrollment_additional_security>` section.

Registration with protocol::

    fortishield-agent-|FORTISHIELD_CURRENT_WINDOWS|-|FORTISHIELD_REVISION_WINDOWS|.msi /q FORTISHIELD_MANAGER="10.0.0.2" FORTISHIELD_REGISTRATION_SERVER="10.0.0.2" FORTISHIELD_AGENT_NAME="W2016" FORTISHIELD_PROTOCOL="udp"

.. warning::
    In Windows versions older than Windows Server 2008 or Windows 7, it's necessary to run the ``fortishield-authd`` program on the Fortishield manager with the ``-a`` flag or set the ``<ssl_auto_negotiate>`` option to ``yes`` on the :ref:`auth configuration <reference_ossec_auth>` to avoid compatibility errors.
