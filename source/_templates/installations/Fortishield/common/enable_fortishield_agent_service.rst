.. Copyright (C) 2015, Fortishield, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl daemon-reload
      # systemctl enable fortishield-agent
      # systemctl start fortishield-agent


  .. group-tab:: SysV init

    Choose one option according to your operating system.

    a) RPM-based operating systems:

      .. code-block:: console

        # chkconfig --add fortishield-agent
        # service fortishield-agent start

    b) Debian-based operating systems:

      .. code-block:: console

        # update-rc.d fortishield-agent defaults 95 10
        # service fortishield-agent start



  .. group-tab:: No service manager

     On some systems, like Alpine Linux, you need to start the agent manually: 

     .. code-block:: console

       # /var/ossec/bin/fortishield-control start

.. End of include file