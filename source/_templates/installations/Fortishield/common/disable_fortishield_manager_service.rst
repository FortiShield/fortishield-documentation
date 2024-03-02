.. Copyright (C) 2015, Fortishield, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl disable fortishield-manager
      # systemctl daemon-reload


  .. group-tab:: SysV init

    Choose one option according to your operating system.

    a) RPM-based operating systems:

      .. code-block:: console

        # chkconfig fortishield-manager off
        # chkconfig --del fortishield-manager

    b) Debian-based operating systems:

      .. code-block:: console

        # update-rc.d -f fortishield-manager remove

.. End of include file