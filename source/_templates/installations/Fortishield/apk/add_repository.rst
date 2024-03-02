.. Copyright (C) 2015, Fortishield, Inc.

#. Import the RSA key:

   .. code-block:: console

      # wget -O /etc/apk/keys/alpine-devel@fortishield.com-633d7457.rsa.pub https://packages.fortishield.com/key/alpine-devel%40fortishield.com-633d7457.rsa.pub

#. Add the repository:

   .. code-block:: console

      # echo "https://packages.fortishield.com/4.x/alpine/v3.12/main" >> /etc/apk/repositories

#. Update the metadata information:

   .. code-block:: console

      # apk update
      
.. End of include file
