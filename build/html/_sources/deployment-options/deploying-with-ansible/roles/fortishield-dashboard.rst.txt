.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to use a preconfigured role to install the Fortishield dashboard and customize the installation with different variables in this section.

Fortishield dashboard
---------------

This role deploys the Fortishield dashboard. You can customize the installation with the following variables:

-  ``indexer_network_host``: This defines the Elasticsearch node IP address (default: ``127.0.0.1``).
-  ``indexer_http_port``: This defines the Elasticsearch node listening port (default: ``9200``).
-  ``dashboard_server_host``: This defines the Fortishield dashboard listening node address (default: ``0.0.0.0``).

To use the role in a playbook, a YAML file ``fortishield-dashboard.yml`` can be created with the contents below:

.. code-block:: yaml

   - hosts: dashboard
     roles:
       - fortishield-dashboard

Custom variable definitions for different environments can be set. For example:

-  For a production environment, the variables can be saved in ``vars-production.yml``:

   .. code-block:: yaml

      indexer_network_host: '10.1.1.10'

-  For a development environment, the variables can be saved in ``vars-development.yml``:

   .. code-block:: yaml

      indexer_network_host: '192.168.0.10'

To run the playbook for a specific environment, the command below is run:

.. code-block:: console

   $ ansible-playbook fortishield-dashboard.yml -e@vars-production.yml

The example above will install the Fortishield dashboard and configure ``10.1.1.10`` as the Indexer node.

Please review the :ref:`variable references <fortishield_ansible_reference_dashboard>` section to see all variables available for this role.
