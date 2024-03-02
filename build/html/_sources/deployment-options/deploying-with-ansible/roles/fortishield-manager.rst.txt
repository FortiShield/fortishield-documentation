.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to use a preconfigured role to install the Fortishield Manager and customize the installation with different variables in this section.

Fortishield Manager
-------------

This role will install and configure the Fortishield Manager and API. There are several variables you can use to customize the installation or configuration. They include:

-  ``fortishield_manager_config_overlay``: This enables configuring the manager by overlaying sections of configs on top of defaults (default: ``true``)
-  ``fortishield_manager_json_output``: This parameter specifies whether JSON output should be enabled or not (default: ``yes``)
-  ``fortishield_manager_email_notification``: This enables email notifications (default: ``no``)
-  ``fortishield_manager_mailto``: This parameter specifies email notifications recipients (array, defaults: ``admin@example.net``)
-  ``fortishield_manager_email_smtp_server``: This parameter specifies the SMTP server to be used by email notifications ( defaults: ``localhost``)
-  ``fortishield_manager_email_from``: This parameter specifies the email notification sender identifier ( defaults: ``fortishield@example.com``)

To use the role in a playbook, a YAML file ``fortishield-manager.yml`` can be created with the contents below:

.. code-block:: yaml

   - hosts: fortishield-manager
     roles:
       - ansible-fortishield-manager
       - ansible-filebeat-oss

Custom variable definitions for different environments can be set when configuring the installation. For example: ``vars-production.yml``:

.. code-block:: yaml

   filebeat_output_indexer_hosts: '10.1.1.11:9200'

   fortishield_manager_fqdn: "fortishield-manager"

   fortishield_manager_config_overlay: true
   fortishield_manager_json_output: 'yes'
   fortishield_manager_alerts_log: 'yes'
   fortishield_manager_logall: 'no'
   fortishield_manager_log_format: 'plain'

   fortishield_manager_connection:
     - type: 'secure'
       port: '1514'
       protocol: 'tcp'

   fortishield_manager_authd:
     enable: true
     port: 1515
     use_source_ip: 'no'
     force:
       - enabled: 'yes'
         disconnected_time:
           enabled: yes
           value: '1h'
         after_registration_time: '1h'
         key_mismatch: 'yes'
     purge: 'no'
     use_password: 'no'
     ssl_agent_ca: null
     ssl_verify_host: 'no'
     ssl_manager_cert: null
     ssl_manager_key: null
     ssl_auto_negotiate: 'no'

Agentless host credentials can be configured in the file: ``ansible-fortishield-manager/vars/agentless_creds.yml``. Set as many as you need:

.. code-block:: yaml

   # Be sure you encrypt this file with ansible-vault.
   agentless_creds:
    - type: ssh_integrity_check_linux
      frequency: 3600
      host: root@example1.net
      state: periodic
      arguments: '/bin /etc/ /sbin'
      passwd: qwerty
    - type: ssh_integrity_check_bsd
      frequency: 3600
      host: user@example2.net
      state: periodic
      arguments: '/bin /etc/ /sbin'
      passwd: qwerty

Finally, the ``authd`` service password can be set in the file ``ansible-fortishield-manager/vars/authd_pass.yml``:

.. code-block:: yaml

   # Be sure you encrypt this file with ansible-vault
   authd_pass: foobar

.. warning::

   We recommend the use of `Ansible Vault <http://docs.ansible.com/ansible/playbooks_vault.html>`_ to protect Fortishield API and agentless credentials.

To run the playbook for a specific environment, the command below is run:

.. code-block:: console

   $ ansible-playbook fortishield-manager.yml -e@vars-production.yml

The example above will install Fortishield Manager and Filebeat, Filebeat will be configured to forward data to ``10.1.1.11:9200`` as the Indexer node, also it will set various ``agentless`` hosts configurations including their credentials, the Fortishield API, and the ``authd`` will be configured as well.

Please review the :ref:`variables references <fortishield_ansible_reference_manager>` section to see all variables available for this role.
