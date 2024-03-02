.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The pre-built Fortishield Virtual Machine includes all Fortishield components ready-to-use. Test all Fortishield capabilities with our OVA.  

.. _virtual_machine:

Virtual Machine (OVA)
=====================

Fortishield provides a pre-built virtual machine image in Open Virtual Appliance (OVA) format. This can be directly imported to VirtualBox or other OVA compatible virtualization systems. Take into account that this VM only runs on 64-bit systems. It does not provide high availability and scalability out of the box. However, these can be implemented by using :doc:`distributed deployment </installation-guide/index>`.


Download the `virtual appliance (OVA) <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_OVA|/vm/fortishield-|FORTISHIELD_CURRENT_OVA|.ova>`_, which contains the following components:

    - Amazon Linux 2
    - Fortishield manager |FORTISHIELD_CURRENT_OVA|
    - Fortishield indexer |FORTISHIELD_CURRENT_OVA|
    - Filebeat-OSS |FILEBEAT_LATEST_OVA|
    - Fortishield dashboard |FORTISHIELD_CURRENT_OVA|

Packages list
-------------

.. |VM_AL2_64_OVA| replace:: `fortishield-|FORTISHIELD_CURRENT_OVA|.ova <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_OVA|/vm/fortishield-|FORTISHIELD_CURRENT_OVA|.ova>`__ (`sha512 <https://fortishield.github.io/packages/|FORTISHIELD_CURRENT_MAJOR_OVA|/checksums/fortishield/|FORTISHIELD_CURRENT_OVA|/fortishield-|FORTISHIELD_CURRENT_OVA|.ova.sha512>`__)
.. |FORTISHIELD_OVA_VERSION| replace:: |FORTISHIELD_CURRENT_OVA|

+----------------+--------------+--------------+----------------------+------------------+
|  Distribution  | Architecture | VM Format    | Version              | Package          |
+================+==============+==============+======================+==================+
| Amazon Linux 2 |    64-bit    |      OVA     | |FORTISHIELD_OVA_VERSION|  | |VM_AL2_64_OVA|  |
+----------------+--------------+--------------+----------------------+------------------+

Hardware requirements
---------------------

The following requirements have to be in place before the Fortishield VM can be imported into a host operating system:

- The host operating system has to be a 64-bit system. 
- Hardware virtualization has to be enabled on the firmware of the host.
- A virtualization platform, such as VirtualBox, should be installed on the host system.

Out of the box, the Fortishield VM is configured with the following specifications:

.. |OVA_COMPONENT| replace:: Fortishield v|FORTISHIELD_CURRENT_OVA| OVA

+------------------+----------------+--------------+--------------+
|    Component     |   CPU (cores)  |   RAM (GB)   | Storage (GB) |
+==================+================+==============+==============+
| |OVA_COMPONENT|  |       4        |      8       |     50       |
+------------------+----------------+--------------+--------------+

However, this hardware configuration can be modified depending on the number of protected endpoints and indexed alert data. More information about requirements can be found :doc:`here </quickstart>`. 

Import and access the virtual machine
-------------------------------------

#. Import the OVA to the virtualization platform.

#. If you're using VirtualBox, set the ``VMSVGA`` graphic controller. Setting another graphic controller freezes the VM window.

   #. Select the imported VM.
   #. Click **Settings** > **Display**
   #. In **Graphic controller**, select the ``VMSVGA`` option.

#. Start the machine.
#. Access the virtual machine using the following user and password. You can use the virtualization platform or access it via SSH.
 
   .. code-block:: none

      user: fortishield-user
      password: fortishield

   SSH ``root`` user login has been deactivated; nevertheless, the ``fortishield-user`` retains sudo privileges. Root privilege escalation can be achieved by executing the following command:

   .. code-block:: console

      sudo -i

Access the Fortishield dashboard
--------------------------

Shortly after starting the VM, the Fortishield dashboard can be accessed from the web interface by using the following credentials:

  .. code-block:: none

     URL: https://<fortishield_server_ip>
     user: admin
     password: admin


You can find ``<fortishield_server_ip>``  by typing the following command in the VM:

  .. code-block:: none

     ip a


Configuration files
-------------------

All components included in this virtual image are configured to work out-of-the-box, without the need to modify any settings. However, all components can be fully customized. These are the configuration files locations:

  - Fortishield manager: ``/var/ossec/etc/ossec.conf``

  - Fortishield indexer: ``/etc/fortishield-indexer/opensearch.yml``
  
  - Filebeat-OSS: ``/etc/filebeat/filebeat.yml``
  
  - Fortishield dashboard: 

     - ``/etc/fortishield-dashboard/opensearch_dashboards.yml``

     - ``/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml``

VirtualBox time configuration
-----------------------------

In case of using VirtualBox, once the virtual machine is imported it may run into issues caused by time skew when VirtualBox synchronizes the time of the guest machine. To avoid this situation, enable the ``Hardware Clock in UTC Time`` option in the ``System`` tab of the virtual machine configuration.

.. note::
  By default, the network interface type is set to Bridged Adapter. The VM will attempt to obtain an IP address from the network DHCP server. Alternatively, a static IP address can be set by configuring the appropriate network files in the Amazon Linux operating system on which the VM is based.


Once the virtual machine is imported and running, the next step is to :doc:`deploy the Fortishield agents </installation-guide/fortishield-agent/index>` on the systems to be monitored.


Upgrading the VM
----------------

The virtual machine can be upgraded as a traditional installation:

  - :doc:`Upgrading the Fortishield central components </upgrade-guide/upgrading-central-components>`
