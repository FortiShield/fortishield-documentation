.. Copyright (C) 2015, Fortishield, Inc.


#. Run the following commands replacing ``<indexer-node-name>`` with the name of the Fortishield indexer node you are configuring as defined in ``config.yml``. For example, ``node-1``. This deploys the SSL certificates to encrypt communications between the Fortishield central components.

   .. code-block:: console

     # NODE_NAME=<indexer-node-name>

   .. code-block:: console 
     
     # mkdir /etc/fortishield-indexer/certs
     # tar -xf ./fortishield-certificates.tar -C /etc/fortishield-indexer/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./admin.pem ./admin-key.pem ./root-ca.pem
     # mv -n /etc/fortishield-indexer/certs/$NODE_NAME.pem /etc/fortishield-indexer/certs/indexer.pem
     # mv -n /etc/fortishield-indexer/certs/$NODE_NAME-key.pem /etc/fortishield-indexer/certs/indexer-key.pem
     # chmod 500 /etc/fortishield-indexer/certs
     # chmod 400 /etc/fortishield-indexer/certs/*
     # chown -R fortishield-indexer:fortishield-indexer /etc/fortishield-indexer/certs
    
#. **Recommended action**: If no other Fortishield components are going to be installed on this node, remove the ``fortishield-certificates.tar`` file by running ``rm -f ./fortishield-certificates.tar`` to increase security.

.. End of include file
