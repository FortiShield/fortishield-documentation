.. Copyright (C) 2015, Fortishield, Inc.

#. Import the GPG key:

    .. code-block:: console

      # rpm --import https://packages.fortishield.com/key/GPG-KEY-FORTISHIELD

#. Add the repository:

    .. code-block:: console

      # cat > /etc/yum.repos.d/fortishield.repo << EOF
      [fortishield]
      gpgcheck=1
      gpgkey=https://packages.fortishield.com/key/GPG-KEY-FORTISHIELD
      enabled=1
      name=EL-\$releasever - Fortishield
      baseurl=https://packages.fortishield.com/4.x/yum/
      protect=1
      EOF 

.. End of include file
