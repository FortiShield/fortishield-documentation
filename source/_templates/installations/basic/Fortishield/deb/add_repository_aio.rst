.. Copyright (C) 2015, Fortishield, Inc.

#. Install the GPG key:

    .. code-block:: console

      # curl -s https://packages.fortishield.com/key/GPG-KEY-FORTISHIELD | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/fortishield.gpg --import && chmod 644 /usr/share/keyrings/fortishield.gpg

#. Add the repository:

    .. code-block:: console

      # echo "deb [signed-by=/usr/share/keyrings/fortishield.gpg] https://packages.fortishield.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/fortishield.list

#. Update the package information:

    .. code-block:: console

      # apt-get update

.. End of include file
