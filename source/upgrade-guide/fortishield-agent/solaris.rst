.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Check out how to upgrade the Fortishield agent to the latest available version remotely, using the agent_upgrade tool or the Fortishield API, or locally.


Upgrading Fortishield agents on Solaris systems
=========================================

Select your Solaris version and follow the steps to upgrade the Fortishield agent.

.. tabs::

   .. group-tab:: Solaris 11

      #. Download the latest Solaris 11 installer. Choose one option depending on the host architecture.

         * `Solaris 11 i386 installer <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_SOLARIS11_i386|/solaris/i386/11/fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_i386|-sol11-i386.p5p>`_

         * `Solaris 11 sparc installer <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_SOLARIS11_SPARC|/solaris/sparc/11/fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_SPARC|-sol11-sparc.p5p>`_

      #. Stop the Fortishield agent.

         .. code-block:: console

            # /var/ossec/bin/fortishield-control stop


      #. Upgrade the Fortishield agent. Choose one option depending on the host architecture.

         * Solaris 11 i386:

            .. code-block:: console

               # pkg install -g fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_i386|-sol11-i386.p5p fortishield-agent

         * Solaris 11 sparc:

            .. code-block:: console

               # pkg install -g fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS11_SPARC|-sol11-sparc.p5p fortishield-agent


      #. Start the Fortishield agent.

         .. code-block:: console

            # /var/ossec/bin/fortishield-control start


   .. group-tab:: Solaris 10

      #. Download the latest Solaris 10 installer. Choose one option depending on the host architecture.

         * `Solaris 10 i386 installer <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_SOLARIS10_i386|/solaris/i386/10/fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS10_i386|-sol10-i386.pkg>`_

         * `Solaris 10 sparc installer <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_SOLARIS10_SPARC|/solaris/sparc/10/fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS10_SPARC|-sol10-sparc.pkg>`_

      #. Stop the Fortishield agent.

         .. code-block:: console

            # /var/ossec/bin/fortishield-control stop


      #. Backup the ``ossec.conf`` and ``client.keys`` files.

           .. code-block:: console

             # cp /var/ossec/etc/ossec.conf ~/ossec.conf.bk
             # cp /var/ossec/etc/client.keys ~/client.keys.bk


      #. Remove the Fortishield agent.

         .. code-block:: console

            # pkgrm fortishield-agent

      #. Remove previous installation folder.

         .. code-block:: console

            # rm -rf /var/ossec

      #. Install the Fortishield agent. Choose one option depending on the host architecture.

         * Solaris 10 i386:

            .. code-block:: console

               # pkgadd -d fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS10_i386|-sol10-i386.pkg fortishield-agent

         * Solaris 10 sparc:

            .. code-block:: console

               # pkgadd -d fortishield-agent_v|FORTISHIELD_CURRENT_SOLARIS10_SPARC|-sol10-sparc.pkg fortishield-agent


      #. Restore the ``ossec.conf`` and ``client.keys`` files.

         .. code-block:: console

            # mv ~/ossec.conf.bk /var/ossec/etc/ossec.conf
            # chown root:fortishield /var/ossec/etc/ossec.conf
            # mv ~/client.keys.bk /var/ossec/etc/client.keys
            # chown root:fortishield /var/ossec/etc/client.keys


      #. Start the Fortishield agent.

         .. code-block:: console

            # /var/ossec/bin/fortishield-control start


.. note::
   :class: not-long

   When upgrading agents from versions earlier than 4.x, make sure that the communication protocol is compatible. Up to that point, UDP was the default protocol and it was switched to TCP for later versions. Edit the agent configuration file ``ossec.conf`` to update the :ref:`protocol <server_protocol>` or make sure that your Fortishield manager accepts :ref:`both protocols<manager_protocol>`.