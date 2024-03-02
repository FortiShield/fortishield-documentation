.. Copyright (C) 2015, Fortishield, Inc.

#. Import the GPG key:

    .. code-block:: console

      # rpm --import https://fortishield.github.io/packages/key/GPG-KEY-FORTISHIELD

#. Add the repository:

    .. code-block:: console

      # cat > /etc/zypp/repos.d/fortishield.repo <<\EOF
      [fortishield]
      gpgcheck=1
      gpgkey=https://fortishield.github.io/packages/key/GPG-KEY-FORTISHIELD
      enabled=1
      name=EL-$releasever - Fortishield
      baseurl=https://fortishield.github.io/packages/4.x/yum/
      protect=1
      EOF 

#. Refresh the repository:

    .. code-block:: console
 
      # zypper refresh

      
.. End of include file
