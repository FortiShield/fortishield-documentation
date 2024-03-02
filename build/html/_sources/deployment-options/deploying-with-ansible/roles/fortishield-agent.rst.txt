.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to use a preconfigured role to install and configure the Fortishield Agent on different hosts in this section of the Fortishield documentation.
  
Fortishield Agent
-----------

This role is designed to install and configure the Fortishield Agent on different hosts. There are agent installer packages for Linux, macOS, and Windows machines. This role can also enroll the agent in the Fortishield Manager. Below are some variables you can use to customize the installation:

-  ``fortishield_managers``: This specifies a list of Fortishield manager node(s) for Fortishield agents to report to.
-  ``fortishield_agent_authd``: This specifies a set of options to register the Fortishield agent on the Fortishield server. This requires the ``fortishield-authd`` service to be running on the Fortishield server.

To use the role in a playbook, a YAML file ``fortishield-agent.yml`` can be created with the contents below:

.. code-block:: yaml

   - hosts: all:!fortishield-manager
     roles:
      - ansible-fortishield-agent

You can maintain different environments using a variable definition YAML file for each one:

-  For a production environment, the variables can be saved in ``vars-production.yml``:

.. code-block:: yaml

   fortishield_managers:
     - address: 10.1.1.12
       port: 1514
       protocol: udp
   fortishield_agent_authd:
     registration_address: 10.1.1.12
     enable: true
     port: 1515
     ssl_agent_ca: null
     ssl_auto_negotiate: 'no'

-  For a development environment, the variables can be saved in ``vars-development.yml``:

.. code-block:: yaml

   fortishield_managers:
     - address: 192.168.0.10
       port: 1514
       protocol: udp
   fortishield_agent_authd:
     registration_address: 192.168.0.10
     enable: true
     port: 1515
     ssl_agent_ca: null
     ssl_auto_negotiate: 'no'

To run the playbook for a specific environment, the command below is run:

.. code-block:: console

   $ ansible-playbook fortishield-agent.yml -e@vars-production.yml

The example above for a production environment will install a Fortishield agent in all host groups except the ``fortishield-manager`` group. Then, it will register them against the ``fortishield-manager`` with IP address ``10.1.1.12``.

Please review the :ref:`variables references <fortishield_ansible_reference_agent>` section to see all variables available for this role.
