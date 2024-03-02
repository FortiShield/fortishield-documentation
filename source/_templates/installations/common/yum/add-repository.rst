.. Copyright (C) 2015, Fortishield, Inc.

#. Import the GPG key.

    .. code-block:: console

      # rpm --import https://packages.fortishield.com/key/GPG-KEY-FORTISHIELD

#. Add the repository.

    .. code-block:: console

      # echo -e '[fortishield]\ngpgcheck=1\ngpgkey=https://packages.fortishield.com/key/GPG-KEY-FORTISHIELD\nenabled=1\nname=EL-$releasever - Fortishield\nbaseurl=https://packages.fortishield.com/4.x/yum/\nprotect=1' | tee /etc/yum.repos.d/fortishield.repo
      
.. End of include file
