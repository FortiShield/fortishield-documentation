.. Copyright (C) 2015, Fortishield, Inc.

#. Replace ``<dashboard-node-name>`` with your Fortishield dashboard node name, the same one used in ``config.yml`` to create the certificates, and move the certificates to their corresponding location. 

    .. code-block:: console

      # NODE_NAME=<dashboard-node-name>
      
    .. code-block:: console  
    
      # mkdir /etc/fortishield-dashboard/certs
      # tar -xf ./fortishield-certificates.tar -C /etc/fortishield-dashboard/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./root-ca.pem
      # mv -n /etc/fortishield-dashboard/certs/$NODE_NAME.pem /etc/fortishield-dashboard/certs/dashboard.pem
      # mv -n /etc/fortishield-dashboard/certs/$NODE_NAME-key.pem /etc/fortishield-dashboard/certs/dashboard-key.pem
      # chmod 500 /etc/fortishield-dashboard/certs
      # chmod 400 /etc/fortishield-dashboard/certs/*
      # chown -R fortishield-dashboard:fortishield-dashboard /etc/fortishield-dashboard/certs

.. End of include file
