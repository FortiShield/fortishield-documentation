.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Check out this installation guide to create an environment consisting of a Fortishield server, an Elastic Stack server, and a Fortishield agent. 
  
.. _fortishield_ansible_guide:

Installation Guide
==================

The objective of this section is to guide users in the installation of an environment consisting of a Fortishield indexer, dashboard, manager, and Fortishield agents, in a simple and intuitive way using the Ansible deploy tool.

`Ansible <https://www.ansible.com/resources/get-started>`_ is an open source software that automates software provisioning, configuration management, and application deployment.


Requirements
------------
  
Before we get started with Ansible, confirm the following requirements are met:

-  **Private network DNS**: If you intend to use hostname instead of IP Address for remote endpoints definitions, be sure you have correctly set up your DNS server and that it corresponds to the FQDN of your endpoints. Otherwise, use your hosts file.

-  **Firewall settings**: Ansible can work with any TCP port. By default, it uses TCP/22 port to work with Linux endpoints. Ensure this port is open in endpoints and/or firewalls. In addition, you need to use and configure ``iptables``, ``firewalld``, ``ufw``, *Security Groups*, or any other firewall settings.

-  **Required open ports**: You can access the :ref:`Required ports <default_ports>` list to find out which ports you need to communicate the Fortishield components with external services such as Ansible. 

.. toctree::
   :maxdepth: 1

   guide/install-ansible
   guide/install-indexer-dashboard
   guide/install-fortishield-manager
   guide/install-fortishield-cluster
   guide/install-fortishield-agent
