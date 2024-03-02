.. Copyright (C) 2015, Fortishield, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl daemon-reload
      # systemctl enable fortishield-dashboard
      # systemctl start fortishield-dashboard



  .. group-tab:: SysV init

    Choose one option according to your operating system:

    a) RPM-based operating system:

      .. code-block:: console

        # chkconfig --add fortishield-dashboard
        # service fortishield-dashboard start
    
    b) Debian-based operating system:

      .. code-block:: console

        # update-rc.d fortishield-dashboard defaults 95 10
        # service fortishield-dashboard start

.. End of include file
