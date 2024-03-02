.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Deploying the Fortishield indexer and the Fortishield dashboard with Ansible.

Install Fortishield indexer and dashboard
===================================

In the Fortishield Ansible repository, we can find the playbooks and roles necessary to install the Fortishield indexer and dashboard components. The Ansible server must have access to the indexer and dashboard server.

.. contents::
   :local:
   :depth: 1
   :backlinks: none

.. warning::

	In previous versions of this guide, playbooks were used pointing to roles to install Opendistro. Starting with Fortishield v.4.3.0 those roles have been replaced by the Fortishield indexer and dashboard.

1 - Accessing the fortishield-ansible directory
-----------------------------------------

We access the contents of the directory on the Ansible server where we have cloned the repository to. We can see the roles we have by running the command below in the cloned directory:

.. code-block:: console

   # cd /etc/ansible/roles/fortishield-ansible/
   # tree roles -d

.. code-block:: none
   :class: output

   roles
   ├── ansible-galaxy
   │   └── meta
   └── fortishield
     ├── ansible-filebeat-oss
     │   ├── defaults
     │   ├── handlers
     │   ├── meta
     │   ├── tasks
     │   └── templates
     ├── ansible-fortishield-agent
     │   ├── defaults
     │   ├── handlers
     │   ├── meta
     │   ├── tasks
     │   └── templates
     ├── ansible-fortishield-manager
     │   ├── defaults
     │   ├── files
     │   │   └── custom_ruleset
     │   │       ├── decoders
     │   │       └── rules
     │   ├── handlers
     │   ├── meta
     │   ├── tasks
     │   ├── templates
     │   └── vars
     ├── fortishield-dashboard
     │   ├── defaults
     │   ├── handlers
     │   ├── tasks
     │   ├── templates
     │   └── vars
     └── fortishield-indexer
         ├── defaults
         ├── handlers
         ├── meta
         ├── tasks
         └── templates

And we can see the preconfigured playbooks we have by running the command below.:

.. code-block:: console

   root@ansible:/etc/ansible/roles/fortishield-ansible# tree playbooks/

.. code-block:: none
   :class: output

   playbooks
   ├── ansible.cfg
   ├── fortishield-agent.yml
   ├── fortishield-dashboard.yml
   ├── fortishield-indexer.yml
   ├── fortishield-manager-oss.yml
   ├── fortishield-production-ready.yml
   └── fortishield-single.yml

Using the dashboard and indexer  roles, we will install and configure the Fortishield dashboard and indexer components. Let’s see below, the content of the playbook ``/etc/ansible/roles/fortishield-ansible/playbooks/fortishield-indexer.yml``.

.. code-block:: yaml

   ---
   - hosts: wi_cluster
   roles:
     - role: ../roles/fortishield/fortishield-indexer

   vars:
     instances:           # A certificate will be generated for every node using the name as CN.
       node1:
         name: node-1
         ip: <node-1 IP>
         role: indexer
       node2:
         name: node-2
         ip: <node-2 IP>
         role: indexer
       node3:
         name: node-3
         ip: <node-3 IP>
         role: indexer

Let’s see below, the content of the playbook ``/etc/ansible/roles/fortishield-ansible/playbooks/fortishield-dashboard.yml``

.. code-block:: yaml

   ---
   - hosts: wi1
     roles:
       - role: ../roles/fortishield/fortishield-dashboard
     vars:
       ansible_shell_allow_world_readable_temp: true

These files are designed to run the installations of each service individually.

Let's take a closer look at the content.

-  The line ``hosts``: indicates the endpoints where the commands of the playbook will be executed.

-  The ``roles``: section indicates the roles that will be executed on the hosts.

There are several variables we can use to customize the installation or configuration. If we want to change the default configuration:

-  We can change the following files:

   -  ``/etc/ansible/roles/fortishield-ansible/roles/fortishield/fortishield-dashboard/defaults/main.yml``
   -  ``/etc/ansible/roles/fortishield-ansible/roles/fortishield/fortishield-indexer/defaults/main.yml``
    
-  Alternatively, we also can create another YAML file with the content we want to change for each role. We can find more information about the roles below:

   -  :doc:`Fortishield indexer <../roles/fortishield-indexer>` role.
   -  :doc:`Fortishield dashboard <../roles/fortishield-dashboard>` role.

More details on default configuration variables can be found in the :doc:`variables references section <../reference>`.

2 - Preparing to run the playbook
---------------------------------

We can configure the indexer and dashboard files and execute them individually, or create a single file that executes the installation of the services in our all in one Fortishield server. In this case, we choose to use a single file to execute the installation.

Create the file fortishield-indexer-and-dashboard.yml in the playbooks directory.

.. code-block:: console

   # touch playbooks/fortishield-indexer-and-dashboard.yml

Fill it with the content below:

.. code-block:: yaml
   :class: output

   - hosts: all_in_one
     roles:
       - role: ../roles/fortishield/fortishield-indexer
         perform_installation: false
     become: no
     vars:
       indexer_node_master: true
       instances:
         node1:
           name: node-1       # Important: must be equal to indexer_node_name.
           ip: 127.0.0.1
           role: indexer
     tags:
       - generate-certs

   - hosts: all_in_one
     become: yes
     become_user: root
     roles:
       - role: ../roles/fortishield/fortishield-indexer
       - role: ../roles/fortishield/fortishield-dashboard

     vars:
       single_node: true
       indexer_network_host: 127.0.0.1
       ansible_shell_allow_world_readable_temp: true
       instances:           # A certificate will be generated for every node using the name as CN.
         node1:
           name: node-1
           ip: 127.0.0.1
           role: indexer
 
As we can see, we have added the IP address of our dashboard and indexer server to the ``indexer_network_host`` entry.

3 - Running the playbook
------------------------

Now, It seems that we are ready to run the playbook and start the installation. However, some of the operations to be performed on the remote systems will need sudo permissions. We can solve this in several ways, such as entering the password when Ansible requests it or using the `become <https://docs.ansible.com/ansible/latest/user_guide/become.html#id1>`_ option (to avoid entering passwords one by one).

#. Let's run the playbook.

   Switch to the playbooks folder on the Ansible server and proceed to run the command below:

   .. code-block:: console

      # ansible-playbook fortishield-indexer-and-dashboard.yml -b -K

#. We can check the status of our new services on our Fortishield indexer and dashboard server.

   -  **Fortishield indexer**

      .. code-block:: console

         # systemctl status fortishield-indexer

   -  **Fortishield dashboard**
    
      .. code-block:: console

         # systemctl status fortishield-dashboard

.. note::
	
	- 	The Fortishield dashboard can be accessed by visiting ``https://<fortishield_server_IP>``

	- 	The default credentials for Fortishield deployed using ansible is:
		
		|	Username: admin
		| Password: changeme
		| These credentials should be changed using the password changing tool.
..
    Once the Fortishield API is registered we can access it through the Fortishield dashboard.

    .. thumbnail:: ../../../images/ansible/fortishield-dashboard-main.png
       :title: Fortishield dashboard portal
       :align: center
       :width: 80%
