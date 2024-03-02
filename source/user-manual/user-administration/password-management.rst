.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn how to use the Fortishield passwords tool to manage your passwords and secure your Fortishield installation.

Password management
===================

.. note::

   If you deployed Fortishield on Docker, read :ref:`change-pwd-existing-usr` for specific instructions.

Learn how to use the Fortishield passwords tool to manage your passwords. This tool allows you to change the passwords of both the :doc:`Fortishield indexer </getting-started/components/fortishield-indexer>` users, also known as internal users, and the :doc:`Fortishield manager API </user-manual/api/index>`  users.

Among the Fortishield indexer users, it is worth mentioning the following:

- *admin*: is the default administrator user. It's used to log in to the web interface and for communications between Filebeat and the Fortishield indexer. If you change the *admin* password, you must update it in Filebeat and the Fortishield server.

- *kibanaserver*: is used for communications between the Fortishield dashboard and the Fortishield indexer. If you change the *kibanaserver* password, you must update it in the Fortishield dashboard.

On the other hand, the Fortishield manager API has two default users:

- *fortishield*: is the default Fortishield manager API administrator user.

- *fortishield-wui*: is an admin user used for communications between Fortishield dashboard and the Fortishield manager API. If you change the *fortishield-wui* password, you must update it in the Fortishield dashboard.

If you use the tool in an all-in-one deployment, it automatically updates the passwords where necessary.  If you use it in a distributed environment, depending on the user whose password you change, you may have to update the password on other components. See  :ref:`Changing the passwords in a distributed environment <passwords_distributed>` for more details.

The passwords tool is embedded in the Fortishield indexer under ``/usr/share/fortishield-indexer/plugins/opensearch-security/tools/``. You can use the embedded version or download it with the following command:

  .. code-block:: console

    # curl -so fortishield-passwords-tool.sh https://packages.fortishield.com/|FORTISHIELD_CURRENT_MINOR|/fortishield-passwords-tool.sh


All the available options to run the script are:

+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Options                                      | Purpose                                                                                                     |
+==============================================+=============================================================================================================+
| -a / --change-all                            | Changes all the Fortishield indexer and Fortishield API user passwords and prints them on screen.                       |
|                                              | To change API passwords -au|--admin-user and -ap|--admin-password are required.                             |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -A,  --api                                   | Change the Fortishield API password given the current password.                                                   |
|                                              | Requires -u|--user, and -p|--password, -au|--admin-user and -ap|--admin-password.                           |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -au,--admin-user <adminUser>                 | Admin user for the Fortishield API. Required for changing the Fortishield API passwords.                                |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -ap, --admin-password <adminPassword>        | Password for the Fortishield API admin user. Required for changing the Fortishield API passwords.                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -u / --user <user>                           | Indicates the name of the user whose password will be changed.                                              |
|                                              | If no password is specified, it will generate a random one.                                                 |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -p / --password <password>                   | Indicates the new password. Must be used with option -u.                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -c / --cert <route-admin-certificate>        | Indicates route to the admin certificate.                                                                   |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -k / --certkey <route-admin-certificate-key> | Indicates route to the admin certificate key.                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -v / --verbose                               | Shows the complete script execution output.                                                                 |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -f / --file <password_file.yml>              | Changes the passwords for the ones given in the file.                                                       |
|                                              |                                                                                                             |
|                                              | Fortishield indexer users must have this format:                                                                  |
|                                              |                                                                                                             |
|                                              |    # Description                                                                                            |
|                                              |      indexer_username: <user>                                                                               |
|                                              |      indexer_password: <password>                                                                           |
|                                              |                                                                                                             |
|                                              | Fortishield API users must have this format:                                                                      |
|                                              |                                                                                                             |
|                                              |    # Description                                                                                            |
|                                              |     api_username: <user>                                                                                    |
|                                              |      api_password: <password>                                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -gf, --generate-file <passwords.fortishield>       | Generate password file with random passwords for standard users.                                            |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -h / --help                                  | Shows help.                                                                                                 |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+

Changing the password for single user
-------------------------------------

To change the password for a single Fortishield indexer user, run the script with the ``-u`` option and indicate the new password with the option ``-p``. The password must have a length between 8 and 64 characters and contain at least one upper case letter, one lower case letter, a number and one of the following symbols: ``.*+?-``. If no password is specified, the script will generate a random one.


   .. code-block:: console

      # bash fortishield-passwords-tool.sh -u admin -p Secr3tP4ssw*rd


   .. code-block:: console
      :class: output

      INFO: Generating password hash
      WARNING: Password changed. Remember to update the password in the Fortishield dashboard and Filebeat nodes if necessary, and restart the services.

If you use the tool in an all-in-one deployment, it automatically updates the passwords where necessary.  If you use it in a distributed environment, depending on the user whose password you change, you may have to update the password on other components. See :ref:`Changing the passwords in a distributed environment <passwords_distributed>` for more details.

If you want to change the password for a Fortishield manager API user, run the script on a Fortishield server node and use option ``-A, --api``. Alternatively, you can change the Fortishield manager API passwords following the instructions in the :doc:`Securing the Fortishield API </user-manual/api/securing-api>` documentation.


Changing the passwords for all users
------------------------------------

To generate and change passwords for all the Fortishield indexer users, run the script with the ``-a`` option:

  .. code-block:: console

    # bash fortishield-passwords-tool.sh -a

  .. code-block:: console
    :class: output
    :emphasize-lines: 2,3

    INFO: Fortishield API admin credentials not provided, Fortishield API passwords not changed.
    INFO: The password for user admin is kwd139yG?YoIK?lRnqcXQ4R4gJDlAqKn
    INFO: The password for user kibanaserver is Bu1WIELh9RdRlf*oGjinN1?yhF6XzA7V
    INFO: The password for user kibanaro is 7kZvau11cPn6Y1SbOsdr8Kwr*BRiK3u+
    INFO: The password for user logstash is SUbk4KTmLl*geQbUg0c5tyfwahjDMhx5
    INFO: The password for user readall is ?w*Itj1Lgz.5w.C7vOw0Kxi7G94G8bG*
    INFO: The password for user snapshotrestore is Z6UXgM8Sr0bfV.i*6yPPEUY3H6Du2rdz
    WARNING: Fortishield indexer passwords changed. Remember to update the password in the Fortishield dashboard, Fortishield server, and Filebeat nodes if necessary, and restart the services.

If you use the tool in an all-in-one deployment, it automatically updates the passwords where necessary. If you use it in a distributed environment, you have to update the password on other components. See :ref:`Changing the passwords in a distributed environment <passwords_distributed>` for more details.

On an all-in-one deployment, use options ``-a``, ``-au`` and ``-ap`` to also change the passwords for all the Fortishield indexer and the Fortishield manager API users.

   .. code-block:: console

      # sudo bash fortishield-passwords-tool.sh -a -au fortishield -ap KTb+Md+rR74J2yHfoGGnFGHGm03Gadyu


   .. code-block:: console
      :class: output
      :emphasize-lines: 1,2,8,9

      INFO: The password for user admin is Wkw+b2rM6BEOwUmGfr*m*i1ithWw.dg2
      INFO: The password for user kibanaserver is 5Y0lIfCwmjkus9nWAAVxMInI+Eth25hr
      INFO: The password for user kibanaro is kJG7fHX18.UJIZoNip5nDo*34DN+cGBL
      INFO: The password for user logstash is wuabgegtKsQABems5RNJfV0AOmxT?81T
      INFO: The password for user readall is gKSuQFGG.Sa0L9gzJX5WZHPP3Y4Es+sU
      INFO: The password for user snapshotrestore is UdyI8ToXkgVCNOPfJ*FX*a5vybeB.rUw
      WARNING: Fortishield indexer passwords changed. Remember to update the password in the Fortishield dashboard, Fortishield server, and Filebeat nodes if necessary, and restart the services.
      INFO: The password for Fortishield API user fortishield is zG0yTsAiettOXWEB79Aca1jbQ5.UeW3M
      INFO: The password for Fortishield API user fortishield-wui is JmKiaCBQo?4Ne0yrM4+n7kGdXGfCmVjO
      INFO: Updated fortishield-wui user password in fortishield dashboard. Remember to restart the service.




Changing the passwords using a formatted file
---------------------------------------------

Use a formatted file to indicate the passwords and run the script with the ``-f`` option followed by the file path. Use the following pattern to indicate the users and passwords in the formatted file.

For Fortishield indexer users:

  .. code-block:: none

    # Description
      indexer_username: <user>
      indexer_password: <password>

For Fortishield manager API users:

  .. code-block:: none

    # Description
      api_username: <user>
      api_password: <password>

If the ``-a`` option is used in combination with the ``-f`` option, all users not included in the file are given a random password.

The options ``-au`` and ``-ap`` are necessary to change the passwords for the API users.

.. _passwords_distributed:

Changing the passwords in a distributed environment
---------------------------------------------------

Follow the instructions below to change the passwords for all the Fortishield indexer users as well as the Fortishield manager API users.

#. On `any Fortishield indexer node`, use the Fortishield passwords tool to change the passwords of the Fortishield indexer users.

   .. code-block:: console

      # /usr/share/fortishield-indexer/plugins/opensearch-security/tools/fortishield-passwords-tool.sh --change-all

   .. code-block:: console
      :class: output
      :emphasize-lines: 2,3

      INFO: Fortishield API admin credentials not provided, Fortishield API passwords not changed.
      INFO: The password for user admin is wcAny.XUwOVWHFy.+7tW9l8gUW1L8N3j
      INFO: The password for user kibanaserver is qy6fBrNOI4fD9yR9.Oj03?pihN6Ejfpp
      INFO: The password for user kibanaro is Nj*sSXSxwntrx3O7m8ehrgdHkxCc0dna
      INFO: The password for user logstash is nQg1Qw0nIQFZXUJc8r8+zHVrkelch33h
      INFO: The password for user readall is s0iWAei?RXObSDdibBfzSgXdhZCD9kH4
      INFO: The password for user snapshotrestore is Mb2EHw8SIc1d.oz.nM?dHiPBGk7s?UZB
      WARNING: Fortishield indexer passwords changed. Remember to update the password in the Fortishield dashboard, Fortishield server, and Filebeat nodes if necessary, and restart the services.

#. On your `Fortishield server master node`, download the Fortishield passwords tool and use it to change the passwords of the Fortishield API users. Replace ``<fortishield-password>`` with the *fortishield* user password.

   .. code-block:: console

      # curl -sO https://packages.fortishield.com/|FORTISHIELD_CURRENT_MINOR|/fortishield-passwords-tool.sh
      # bash fortishield-passwords-tool.sh --change-all --admin-user fortishield --admin-password <fortishield-password>

   .. code-block:: console
      :class: output

      INFO: The password for Fortishield API user fortishield is ivLOfmj7.jL6*7Ev?UJoFjrkGy9t6Je.
      INFO: The password for Fortishield API user fortishield-wui is fL+f?sFRPEv5pYRE559rqy9b6G4Z5pVi

#. On `all your Fortishield server nodes`, run the following command to update the `admin` password in the Filebeat keystore and in the ``ossec.conf`` file for the Fortishield server. Replace ``<admin-password>`` with the random password generated in the first step.

   .. code-block:: console

      # echo <admin-password> | filebeat keystore add password --stdin --force
      # sed -i 's/<password>.*<\/password>/<password><admin-password><\/password>/g' /var/ossec/etc/ossec.conf

#. Restart Filebeat and the Fortishield server to apply the change.

   .. include:: /_templates/common/restart_filebeat.rst
   .. include:: /_templates/common/restart_manager.rst

   .. note:: Repeat steps 3 and 4 on `every Fortishield server node`.

#. On your `Fortishield dashboard node`, run the following command to update the `kibanaserver` password in the Fortishield dashboard keystore. Replace ``<kibanaserver-password>`` with the random password generated in the first step.

   .. code-block:: console

      # echo <kibanaserver-password> | /usr/share/fortishield-dashboard/bin/opensearch-dashboards-keystore --allow-root add -f --stdin opensearch.password

#. Update the ``/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml`` configuration file with the new `fortishield-wui` password generated in the second step.

   .. code-block:: yaml
      :emphasize-lines: 6

      hosts:
        - default:
            url: https://localhost
            port: 55000
            username: fortishield-wui
            password: "<fortishield-wui-password>"
            run_as: false

#. Restart the Fortishield dashboard to apply the changes.

   .. include:: /_templates/common/restart_dashboard.rst