.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to use our preconfigured roles to deploy Fortishield indexer and dashboard components, Fortishield Manager and Fortishield Agents.

Roles
=====

You can use our preconfigured roles to deploy the Fortishield indexer and dashboard components, Fortishield Manager, and Fortishield Agents. First, clone our `GitHub repository <https://github.com/fortishield/fortishield-ansible>`_ directly to your Ansible roles folder:

.. code-block:: console

   # cd /etc/ansible/roles
   # git clone --branch v|FORTISHIELD_CURRENT_ANSIBLE| https://github.com/fortishield/fortishield-ansible.git

Below we briefly explain how to use these roles. Please check out the `Ansible Playbook Documentation <http://docs.ansible.com/ansible/playbooks.html>`_ for more information on Ansible roles.

.. topic:: Contents

   .. toctree::
      :maxdepth: 2

      fortishield-indexer
      fortishield-dashboard
      fortishield-filebeat
      fortishield-manager
      fortishield-agent
