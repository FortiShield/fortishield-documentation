.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to use a preconfigured role to install the Fortishield indexer and customize the installation with different variables in this section.

Fortishield indexer
-------------

This role is intended to deploy the Fortishield indexer to a specified node. The following variables can be used to customize the installation:

-  ``indexer_network_hosts``: This defines the listening IP address (default: ``127.0.0.1``).
-  ``indexer_http_port``: This defines the listening port (default: ``9200``).
-  ``indexer_jvm_xms``: This specifies the amount of memory to be used for java (default: ``null``).

To use the role in a playbook, a YAML file ``fortishield-indexer.yml`` can be created with the contents below:

.. code-block:: yaml

   - hosts: indexer
     roles:
     - fortishield-indexer

Custom variable definitions for different environments can be set. For example:

-  For a production environment, the variables can be saved in ``vars-production.yml``:

   .. code-block:: yaml

      indexer_network_host: '10.1.1.10'

-  For a development environment, the variables can be saved in ``vars-development.yml``:

   .. code-block:: yaml

      indexer_network_host: '192.168.0.10'
        
To run the playbook for a specific environment, the command below is run:

.. code-block:: console

   $ ansible-playbook fortishield-indexer.yml -e@vars-production.yml

The example above will install the Fortishield Indexer and set the listening address to: ``10.1.1.10`` using ``vars-production.yml``.

Please review the :ref:`variables references <fortishield_ansible_reference_indexer>` section to see all variables available for this role.
