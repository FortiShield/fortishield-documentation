.. Copyright (C) 2022 Fortishield, Inc.
.. meta::
  :description: Learn more about how to manually restore a Fortishield-DB backup in the Fortishield server administration section of our documentation.

.. _manual_backup_restore:

Fortishield-DB backup restoration
===========================

Fortishield by default performs automatic backups of the **global.db** database. These snapshots may be useful to recover critical information.
Fortishield-DB will restore the last backup available in case of failure during the upgrade. If this process also fails, the restoration must be done manually.

Manual restore process
----------------------

The first step is to turn off Fortishield manager:

  a. For Systemd:

  .. code-block:: console

    # systemctl stop fortishield-manager

  b. For SysV Init:

  .. code-block:: console

    # service fortishield-manager stop

Then, locate the backup to restore. It is stored in ``FORTISHIELD_HOME/backup/db`` with a name format similar to ``global.db-backup-TIMESTAMP-pre_upgrade.gz``.

.. note::
  This process is valid for all the backups in the folder. Snapshots names containing the special tag `pre_upgrade` were created right before upgrading the Fortishield server. Any other snapshot is a periodical backup created according to the :ref:`backup <fortishield-db-config>` setting.

Decompress it. Always use the **-k** flag to preserve the original file:

  .. code-block:: console

    # gzip -dk FORTISHIELD_HOME/backup/db/global.db-backup-TIMESTAMP-pre_upgrade.gz

Remove the current **global.db** database and move the backup to the right location:

  .. code-block:: console

     # rm  FORTISHIELD_HOME/queue/db/global.db
     # mv  FORTISHIELD_HOME/backup/db/global.db-backup-TIMESTAMP-pre_upgrade FORTISHIELD_HOME/queue/db/global.db

And finally, start Fortishield:

  a. For Systemd:

  .. code-block:: console

    # systemctl start fortishield-manager

  b. For SysV Init:

  .. code-block:: console

    # service fortishield-manager start
