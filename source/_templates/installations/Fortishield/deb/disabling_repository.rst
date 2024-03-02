.. Copyright (C) 2015, Fortishield, Inc.

.. code-block:: console

  # sed -i "s/^deb/#deb/" /etc/apt/sources.list.d/fortishield.list
  # apt-get update

Alternatively, you can set the package state to ``hold``. This action stops updates but you can still upgrade it manually using ``apt-get install``.

.. code-block:: console

  # echo "fortishield-agent hold" | dpkg --set-selections

.. End of include file
