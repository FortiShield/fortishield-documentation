.. Copyright (C) 2015, Fortishield, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl daemon-reload
      # systemctl enable fortishield-indexer
      # systemctl start fortishield-indexer



  .. group-tab:: SysV init

    Choose one option according to the operating system used.

    a) RPM-based operating system:

      .. code-block:: console

        # chkconfig --add fortishield-indexer
        # service fortishield-indexer start
    
    b) Debian-based operating system:

      .. code-block:: console

        # update-rc.d fortishield-indexer defaults 95 10
        # service fortishield-indexer start

.. End of include file
