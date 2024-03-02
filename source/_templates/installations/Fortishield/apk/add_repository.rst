.. Copyright (C) 2015, Fortishield, Inc.

#. Import the RSA key:

   .. code-block:: console

      # wget -O /etc/apk/keys/alpine-devel@fortishield.github.io-633d7457.rsa.pub https://fortishield.github.io/packages/key/alpine-devel%40fortishield.github.io-633d7457.rsa.pub

#. Add the repository:

   .. code-block:: console

      # echo "https://fortishield.github.io/packages/4.x/alpine/v3.12/main" >> /etc/apk/repositories

#. Update the metadata information:

   .. code-block:: console

      # apk update
      
.. End of include file
