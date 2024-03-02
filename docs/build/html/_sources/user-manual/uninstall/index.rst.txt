.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn how to uninstall each Fortishield central component.
  
Uninstalling the Fortishield central components
=========================================

You can uninstall all the Fortishield central components using the `Fortishield installation assistant <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MINOR|/fortishield-install.sh>`_.

Run the assistant with the option ``-u`` or ``--uninstall`` as follows:

    .. code-block:: console

      $ sudo bash fortishield-install.sh --uninstall

This will remove the Fortishield indexer, the Fortishield server, and the Fortishield dashboard.

If you want to uninstall one specific central component, follow the instructions below.

.. note:: You need root user privileges to run all the commands described below.

.. _uninstall_dashboard:

Uninstall the Fortishield dashboard
-----------------------------

#. Remove the Fortishield dashboard installation.

    .. tabs::

      .. group-tab:: Yum

        .. code:: console
        
          # yum remove fortishield-dashboard -y
          # rm -rf /var/lib/fortishield-dashboard/
          # rm -rf /usr/share/fortishield-dashboard/
          # rm -rf /etc/fortishield-dashboard/

      .. group-tab:: APT

        .. code:: console

          # apt-get remove --purge fortishield-dashboard -y

.. _uninstall_server:

Uninstall the Fortishield server
--------------------------

#. Remove the Fortishield manager installation.

    .. tabs::

      .. group-tab:: Yum

        .. code-block:: console
          
          # yum remove fortishield-manager -y
          # rm -rf /var/ossec/

      .. group-tab:: APT

        .. code-block:: console
        
          # apt-get remove --purge fortishield-manager -y

#. Disable the Fortishield manager service.

    .. include:: ../../_templates/installations/fortishield/common/disable_fortishield_manager_service.rst

#. Remove the Filebeat installation.

    .. tabs::

      .. group-tab:: Yum

        .. code:: console
        
          # yum remove filebeat -y
          # rm -rf /var/lib/filebeat/
          # rm -rf /usr/share/filebeat/
          # rm -rf /etc/filebeat/

      .. group-tab:: APT

        .. code:: console
      
          # apt-get remove --purge filebeat -y


.. _uninstall_indexer:

Uninstall the Fortishield indexer
---------------------------

#. Remove the Fortishield indexer installation.

    .. tabs::

      .. group-tab:: Yum

        .. code:: console
        
          # yum remove fortishield-indexer -y
          # rm -rf /var/lib/fortishield-indexer/
          # rm -rf /usr/share/fortishield-indexer/
          # rm -rf /etc/fortishield-indexer/

      .. group-tab:: APT

        .. code:: console

          # apt-get remove --purge fortishield-indexer -y
