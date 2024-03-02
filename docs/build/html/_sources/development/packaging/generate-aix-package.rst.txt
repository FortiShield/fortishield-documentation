.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Fortishield provides an automated way of building AIX packages. Learn how to build your own Fortishield AIX packages in this section of our documentation.
  
.. _create-aix:

AIX
===

Fortishield provides an automated way of building AIX packages, keep in mind that to build an AIX package you must run this tool in an AIX system.

To create an AIX package follow these steps:

Requirements
^^^^^^^^^^^^

 * curl

Download our fortishield-packages repository from GitHub and go to the aix directory.

.. code-block:: console

 $ curl -L https://github.com/fortishield/fortishield-packages/tarball/v|FORTISHIELD_CURRENT| | tar zx
 $ cd fortishield-fortishield-packages-*
 $ cd aix

Execute the ``generate_fortishield_packages.sh`` script, with the different options you desire.

.. code-block:: console

  # ./generate_fortishield_packages.sh -h

.. code-block:: none
  :class: output

  Usage: ./generate_fortishield_packages.sh [OPTIONS]

      -b, --branch <branch>               Select Git branch or tag e.g. v|FORTISHIELD_CURRENT_AIX|
      -e, --environment                   Install all the packages necessaries to build the RPM package
      -s, --store  <rpm_directory>        Directory to store the resulting RPM package. By default: /tmp/build
      -p, --install-path <rpm_home>       Installation path for the package. By default: /var
      -c, --checksum <path>               Compute the SHA512 checksum of the RPM package.
      --chroot                            Create a chroot jail to build the package in /usr/pkg
      -h, --help                          Shows this help

First, install the needed dependencies:

.. code-block:: console

 # ./generate_fortishield_packages.sh -e

Below, you will find some examples of how to build an AIX package.

.. code-block:: console

  # ./generate_fortishield_packages.sh -b v|FORTISHIELD_CURRENT_AIX|

This will generate a |FORTISHIELD_CURRENT_AIX| Fortishield agent AIX package.

.. code-block:: console

  # ./generate_fortishield_packages.sh -b v|FORTISHIELD_CURRENT_AIX| -c

This will generate a |FORTISHIELD_CURRENT_AIX| Fortishield agent AIX package with checksum.

.. code-block:: console

  # ./generate_fortishield_packages.sh -b v|FORTISHIELD_CURRENT_AIX|  -p /opt/ossec

This will generate a |FORTISHIELD_CURRENT_AIX| Fortishield agent AIX package with ``/opt/ossec`` as installation directory.
