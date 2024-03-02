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

.. note::

   For Debian 7, 8, and Ubuntu 14 systems import the GCP key and add the Fortishield repository (steps 1 and 2) using the following commands.

   .. code-block:: console

      # apt-get install gnupg apt-transport-https
      # curl -s https://packages.fortishield.com/key/GPG-KEY-FORTISHIELD | apt-key add -
      # echo "deb https://packages.fortishield.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/fortishield.list

.. End of include file
