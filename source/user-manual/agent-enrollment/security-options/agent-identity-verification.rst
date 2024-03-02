.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn more about how to register Fortishield agents on Linux, Windows, or macOS X in this section of our documentation.
  
.. _agent-identity-verification:


Agent identity verification
===========================

This method uses SSL certificates to verify that an agent is authorized to enroll in the Fortishield manager. The manager verification and the agent verification are independent of each other. However, it is possible to use a combination of both.

In this document, you will find the following information:

- :ref:`agent-identity-prerequisites`
- :ref:`agent-identity-verification-options`
    - :ref:`agent-identity-manager-preparations`
    - :ref:`agent-identity-linux-unix-endpoint`
    - :ref:`agent-identity-this-windows-endpoint`
    - :ref:`agent-identity-macos-endpoint`


.. _agent-identity-prerequisites:


Prerequisites
-------------

A certificate authority to sign certificates for the Fortishield manager and agents is needed. In the absence of an already configured certificate authority, the Fortishield manager can be used as the certificate authority by running the below command:

.. code-block:: console
     
    # openssl req -x509 -new -nodes -newkey rsa:4096 -keyout rootCA.key -out rootCA.pem -batch -subj "/C=US/ST=CA/O=Fortishield"


The root certificate is created and saved as the ``rootCA.pem`` file.


.. _agent-identity-verification-options:


Agent verification options
--------------------------

An SSL certificate is issued to the agent host by the CA in prerequisite 1.On attempts to enroll by the agent, the Fortishield manager verifies the certificate presented by the agent using the root certificate. Fortishield provides two Fortishield agent verification options:

- Fortishield agent verification without host validation: The certificates for the agents are issued without specifying their host name or IP address.
- Fortishield agent verification with host validation: The certificates for the agents are issued with their IP address or hostname specified as the common name.
  
The difference between these validation methods is that the certificate in the former method can be reused on multiple agents while the certificate created in the latter can only be used on the agent whose IP address or hostname was specified during certificate generation.


.. _agent-identity-manager-preparations:


Preparations on the Fortishield manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. On the manager, generate a CSR for the Fortishield agent:

   - Fortishield agent verification without host validation: This is done without specifying the agent IP address or hostname.

     .. code-block:: console

        # openssl req -new -nodes -newkey rsa:4096 -keyout sslagent.key -out sslagent.csr -batch

   - Fortishield agent verification with host validation: This is done by specifying the agent IP or hostname.

     .. code-block:: console

        # openssl req -new -nodes -newkey rsa:4096 -keyout sslagent.key -out sslagent.csr -subj '/C=US/CN=<agent_IP>'

   Where:

     - ``sslagent.csr`` is the CSR to be submitted to the certificate authority.
     - ``sslagent.key`` is the generated CSR private key.

#. Sign the generated agent CSR using the CA keys:

   .. code-block:: console

        # openssl x509 -req -days 365 -in sslagent.csr -CA rootCA.pem -CAkey rootCA.key -out sslagent.cert -CAcreateserial


   Where:

     - ``sslagent.csr`` is the CSR to be submitted to the certificate authority.
     - ``sslagent.cert`` is the signed SSL certificate from the CSR.
     - ``rootCA.pem`` is the root certificate for the CA.
     - ``rootCA.key`` is the root certificate private key for the CA.


#. Copy the signed SSL certificate and key (``sslagent.cert`` and ``sslagent.key`` in this case) to the agent. A tool like SCP can be used to copy the certificate to the endpoints. 
#. Ensure that the ``rootCA.pem`` file is in ``/var/ossec/etc/`` on the Fortishield manager.
#. Update the ``/var/ossec/etc/ossec.conf`` file with the location of the ``rootCA.pem`` file to enable the use of certificates. This is done by uncommenting the ``<auth><ssl_agent_ca>`` section and specifying the path to the ``rootCA.pem`` file on the manager.


   .. code-block:: xml
       :emphasize-lines: 3

         <auth>
            ...
            <ssl_agent_ca>/var/ossec/etc/rootCA.pem</ssl_agent_ca>
         </auth>


#. Restart the Fortishield manager service to apply the changes.

.. code-block:: console

       #systemctl restart fortishield-manager


.. _agent-identity-linux-unix-endpoint:


Linux/Unix endpoint
^^^^^^^^^^^^^^^^^^^

The following steps serve as a guide on how to enroll a Linux/Unix endpoint by using certificates for agent verification:

#. Ensure that the signed SSL certificate and key files (``sslagent.cert`` and ``sslagent.key``) for the agent have been copied to the endpoint.
#. As a root user, modify the Fortishield agent configuration file located at ``/var/ossec/etc/ossec.conf`` and include the following:

    #. The Fortishield manager IP address or DNS name in the ``<client><server><address>`` section.
    #. The local path to the agent certificate and the agent key are in the ``<client><enrollment>`` section.


    .. code-block:: xml
        :emphasize-lines: 3, 7

         <client>
            <server>
               <address>MANAGER_IP</address>
            </server>
            <enrollment>
               <agent_certificate_path>CERTIFICATE_PATH</agent_certificate_path>
               <agent_key_path>KEY_PATH</agent_key_path>
            </enrollment>
         </client>



#. Restart the agent to make the changes effective.


   .. tabs::
         
   
      .. group-tab:: Systemd
   
         .. code-block:: console
      
             # systemctl restart fortishield-agent
   
   
      .. group-tab:: SysV init
   
         .. code-block:: console
      
             # service fortishield-agent restart


      .. group-tab:: Other Unix based OS

         .. code-block:: console

             # /var/ossec/bin/fortishield-control restart


#. Select the **Endpoints Summary** module to check for the newly enrolled agent and its connection status in the Fortishield dashboard to confirm that enrollment was successful.


.. _agent-identity-this-windows-endpoint:


Windows endpoint
^^^^^^^^^^^^^^^^

The following steps serve as a guide on how to enroll a Windows endpoint by using certificates for agent verification:

The Fortishield agent installation directory depends on the architecture of the host.

- ``C:\Program Files (x86)\ossec-agent`` for 64-bit systems.
- ``C:\Program Files\ossec-agent`` for 32-bit systems.

#. Ensure that the signed SSL certificate and key files (``sslagent.cert`` and ``sslagent.key``) have been copied to the endpoint.
#. As a root user, modify the Fortishield agent configuration file located at ``“C:\Program Files (x86)\ossec-agent\ossec.conf”`` and include the following:

    #. The Fortishield manager IP address or DNS name in the ``<client><server><address>`` section.
    #. The local path to the agent certificate and the agent key are in the ``<client><enrollment>`` section.

   .. code-block:: xml
       :emphasize-lines: 3, 7     

         <client>
            <server>
               <address>MANAGER_IP</address>
            </server>
            <enrollment>
               <agent_certificate_path>CERTIFICATE_PATH</agent_certificate_path>
               <agent_key_path>KEY_PATH</agent_key_path>
            </enrollment>
         </client>



#. Restart the agent to make the changes effective.


   .. tabs::
      
      
         .. group-tab:: PowerShell (as an administrator)
      
            .. code-block:: console
         
               # Restart-Service -Name fortishield
      
      
         .. group-tab:: CMD (as an administrator)
      
            .. code-block:: console
         
               # net stop fortishield
               # net start fortishield


#. Select the **Endpoints Summary** module to check for the newly enrolled agent and its connection status in the Fortishield dashboard to confirm that enrollment was successful.


.. _agent-identity-macos-endpoint:


macOS endpoint
^^^^^^^^^^^^^^

The following steps serve as a guide on how to enroll a macOS endpoint by using certificates for agent verification:

#. Ensure that the signed SSL certificate and key files (``sslagent.cert`` and ``sslagent.key``) have been copied to the endpoint.
#. As a root user, modify the Fortishield agent configuration file located at ``/Library/Ossec/etc/ossec.conf`` and include the following:

    #. The Fortishield manager IP address or DNS name in the ``<client><server><address>`` section.
    #. The local path to the agent certificate and agent key are in the ``<client><enrollment>`` section.


   .. code-block:: xml
       :emphasize-lines: 3, 7

         <client>
            <server>
               <address>MANAGER_IP</address>
            </server>
            <enrollment>
               <agent_certificate_path>CERTIFICATE_PATH</agent_certificate_path>
               <agent_key_path>KEY_PATH</agent_key_path>
            </enrollment>
         </client>



#. Restart the agent to make the changes effective.

   .. code-block:: console

      # /Library/Ossec/bin/fortishield-control restart


#. Select the **Endpoints Summary** module to check for the newly enrolled agent and its connection status in the Fortishield dashboard to confirm that enrollment was successful.

