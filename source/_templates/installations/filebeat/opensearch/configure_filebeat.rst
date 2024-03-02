.. Copyright (C) 2015, Fortishield, Inc.

#. ``hosts``: The list of Fortishield indexer nodes to connect to. You can use either IP addresses or hostnames. By default, the host is set to localhost ``hosts: ["127.0.0.1:9200"]``. Replace it with your Fortishield indexer address accordingly. 
  
    If you have more than one Fortishield indexer node, you can separate the addresses using commas. For example, ``hosts: ["10.0.0.1:9200", "10.0.0.2:9200", "10.0.0.3:9200"]`` 

    .. code-block:: yaml
      :emphasize-lines: 3

       # Fortishield - Filebeat configuration file
       output.elasticsearch:
       hosts: ["10.0.0.1:9200"]
       protocol: https
       username: ${username}
       password: ${password}
         

.. End of include file
