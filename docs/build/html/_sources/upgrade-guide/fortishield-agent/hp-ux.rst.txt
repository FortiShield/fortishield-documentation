.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Check out how to upgrade the Fortishield agent to the latest available version remotely, using the agent_upgrade tool or the Fortishield API, or locally.


Upgrading Fortishield agents on HP-UX systems
=======================================

Follow the steps to upgrade the Fortishield agent on HP-UX systems.  

#. Download the latest `HP-UX installer <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_HPUX|/hp-ux/fortishield-agent-|FORTISHIELD_CURRENT_HPUX|-|FORTISHIELD_REVISION_HPUX|-hpux-11v3-ia64.tar>`_.

#. Stop the Fortishield agent.

   .. code-block:: console

      # /var/ossec/bin/fortishield-control stop


#. Backup the ``ossec.conf`` configuration file.

   .. code-block:: console

      # cp /var/ossec/etc/ossec.conf ~/ossec.conf.bk
      # cp /var/ossec/etc/client.keys ~/client.keys.bk


#. **Only for upgrades from version 4.2.7 or lower**:  
      
   #. Delete the ossec user and group.

      .. code-block:: console

         # groupdel ossec
         # userdel ossec

   #. Create the fortishield user and group.

      .. code-block:: console

         # groupadd fortishield
         # useradd -G fortishield fortishield

#. Deploy the Fortishield agent files.

   .. code-block:: console

      # tar -xvf fortishield-agent-|FORTISHIELD_CURRENT_HPUX|-|FORTISHIELD_REVISION_HPUX|-hpux-11v3-ia64.tar


#. Restore the ``ossec.conf`` configuration file.

   .. code-block:: console

      # mv ~/ossec.conf.bk /var/ossec/etc/ossec.conf
      # chown root:fortishield /var/ossec/etc/ossec.conf
      # mv ~/client.keys.bk /var/ossec/etc/client.keys
      # chown root:fortishield /var/ossec/etc/client.keys


#. Start the fortishield-agent.

   .. code-block:: console

      # /var/ossec/bin/fortishield-control start

.. note::
   :class: not-long

   When upgrading agents from versions earlier than 4.x, make sure that the communication protocol is compatible. Up to that point, UDP was the default protocol and it was switched to TCP for later versions. Edit the agent configuration file ``ossec.conf`` to update the :ref:`protocol <server_protocol>` or make sure that your Fortishield manager accepts :ref:`both protocols<manager_protocol>`.     
