.. Copyright (C) 2015, Fortishield, Inc.

.. tabs::

   .. group-tab:: Yum

      #. Import the GPG key:

         .. code-block:: console

            # rpm --import https://fortishield.github.io/packages/key/GPG-KEY-FORTISHIELD

      #. Add the repository:

         .. code-block:: console

            # cat > /etc/yum.repos.d/fortishield.repo << EOF
            [fortishield]
            gpgcheck=1
            gpgkey=https://fortishield.github.io/packages/key/GPG-KEY-FORTISHIELD
            enabled=1
            name=EL-\$releasever - Fortishield
            baseurl=https://fortishield.github.io/packages/4.x/yum/
            protect=1 
            EOF 

   .. group-tab:: APT

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
