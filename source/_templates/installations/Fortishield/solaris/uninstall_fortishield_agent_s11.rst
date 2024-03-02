.. Copyright (C) 2015, Fortishield, Inc.

To uninstall the Fortishield agent in Solaris 11, run the following command:

.. code-block:: console

    # /var/ossec/bin/fortishield-control stop
    # pkg uninstall fortishield-agent

.. note:: 
  
  If you uninstall the Fortishield agent in Solaris 11.4 or later, the Solaris 11 package manager does not remove the group ``fortishield`` from the system. To remove it manually, run the ``groupdel fortishield`` command.


.. End of include file
