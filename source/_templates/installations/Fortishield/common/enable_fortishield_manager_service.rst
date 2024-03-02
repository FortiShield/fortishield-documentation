.. Copyright (C) 2015, Fortishield, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl daemon-reload
      # systemctl enable fortishield-manager
      # systemctl start fortishield-manager


  .. group-tab:: SysV init

    Choose one option according to your operating system:

    a) RPM-based operating system:

      .. code-block:: console

        # chkconfig --add fortishield-manager
        # service fortishield-manager start

    b) Debian-based operating system:

      .. code-block:: console

        # update-rc.d fortishield-manager defaults 95 10
        # service fortishield-manager start

.. End of include file
