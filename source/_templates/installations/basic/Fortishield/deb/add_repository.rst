.. Copyright (C) 2015, Fortishield, Inc.

#. For this, the ``curl``, ``apt-transport-https`` and ``lsb-release`` packages must be installed on the system. The ``zip`` package will be necessary for the certificates management. If they are not already present, they must be installed using the commands below:

    .. code-block:: console

      # apt-get update
      # apt-get install curl apt-transport-https lsb-release unzip

#. Install the GPG key:

    .. code-block:: console

      # curl -s https://fortishield.github.io/packages/key/GPG-KEY-FORTISHIELD | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/fortishield.gpg --import && chmod 644 /usr/share/keyrings/fortishield.gpg

#. Add the repository:

    .. code-block:: console

      # echo "deb [signed-by=/usr/share/keyrings/fortishield.gpg] https://fortishield.github.io/packages/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/fortishield.list

#. Update the package information:

    .. code-block:: console

      # apt-get update

.. End of include file
