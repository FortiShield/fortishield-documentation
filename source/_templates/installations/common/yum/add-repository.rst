.. Copyright (C) 2015, Fortishield, Inc.

#. Import the GPG key.

    .. code-block:: console

      # rpm --import https://fortishield.github.io/packages/key/GPG-KEY-FORTISHIELD

#. Add the repository.

    .. code-block:: console

      # echo -e '[fortishield]\ngpgcheck=1\ngpgkey=https://fortishield.github.io/packages/key/GPG-KEY-FORTISHIELD\nenabled=1\nname=EL-$releasever - Fortishield\nbaseurl=https://fortishield.github.io/packages/4.x/yum/\nprotect=1' | tee /etc/yum.repos.d/fortishield.repo
      
.. End of include file
