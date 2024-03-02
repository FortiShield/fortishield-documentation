.. Copyright (C) 2015, Fortishield, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl disable fortishield-agent
      # systemctl daemon-reload


  .. group-tab:: SysV init

    Choose one option according to your operating system.

    a) RPM-based operating systems:

      .. code-block:: console

        # chkconfig fortishield-agent off
        # chkconfig --del fortishield-agent

    b) Debian-based operating systems:

      .. code-block:: console

        # update-rc.d -f fortishield-agent remove



  .. group-tab:: No service manager

     No action required.

.. End of include file