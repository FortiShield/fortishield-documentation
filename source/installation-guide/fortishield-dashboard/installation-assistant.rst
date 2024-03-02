.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to install the Fortishield dashboard using the assisted installation method. The Fortishield dashboard is a flexible and intuitive web interface for mining and visualizing security events and archives. 

Installing the Fortishield dashboard using the assisted installation method
=====================================================================

Install and configure the Fortishield dashboard using the assisted installation method. Fortishield dashboard is a flexible and intuitive web interface for mining and visualizing security events and archives.

Fortishield dashboard installation
-----------------------------

#. Download the Fortishield installation assistant. You can skip this step if you have already installed Fortishield indexer on the same server.

   .. code-block:: console

      # curl -sO https://packages.fortishield.com/|FORTISHIELD_CURRENT_MINOR|/fortishield-install.sh

#. Run the Fortishield installation assistant with the option ``--fortishield-dashboard`` and the node name to install and configure the Fortishield dashboard. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``dashboard``.
   
   .. note::
      
      Make sure that a copy of the ``fortishield-install-files.tar`` file, created during the initial configuration step, is placed in your working directory.

   .. code-block:: console

      # bash fortishield-install.sh --fortishield-dashboard dashboard

   The default Fortishield web user interface port is 443, used by the Fortishield dashboard. You can change this port using the optional parameter ``-p|--port <port_number>``. Some recommended ports are 8443, 8444, 8080, 8888, and 9000.

   Once the Fortishield installation is completed, the output shows the access credentials and a message that confirms that the installation was successful.

   .. code-block:: none
      :emphasize-lines: 3,4          
    
      INFO: --- Summary ---
      INFO: You can access the web interface https://<fortishield-dashboard-ip>
         User: admin
         Password: <ADMIN_PASSWORD>

      INFO: Installation finished.

   You now have installed and configured Fortishield. Find all passwords that the Fortishield installation assistant generated in the ``fortishield-passwords.txt`` file inside the ``fortishield-install-files.tar`` archive. To print them, run the following command:
   
   .. code-block:: console
   
      # tar -O -xvf fortishield-install-files.tar fortishield-install-files/fortishield-passwords.txt

#. Access the Fortishield web interface with your credentials. 

   -  URL: *https://<fortishield-dashboard-ip>*
   -  **Username**: *admin*
   -  **Password**: *<ADMIN_PASSWORD>*

   When you access the Fortishield dashboard for the first time, the browser shows a warning message stating that the certificate was not issued by a trusted authority. An exception can be added in the advanced options of the web browser. For increased security, the ``root-ca.pem`` file previously generated can be imported to the certificate manager of the browser instead. Alternatively, a certificate from a trusted authority can be configured. 


Next steps
----------

All the Fortishield central components are successfully installed.

.. raw:: html

  <div class="link-boxes-group layout-3" data-step="4">
    <div class="steps-line">
      <div class="steps-number past-step">1</div>
      <div class="steps-number past-step">2</div>
      <div class="steps-number past-step">3</div>
    </div>
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="../fortishield-indexer/index.html">
        <p class="link-boxes-label">Install the Fortishield indexer</p>

.. image:: ../../images/installation/Indexer-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="../fortishield-server/index.html">
        <p class="link-boxes-label">Install the Fortishield server</p>

.. image:: ../../images/installation/Server-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="index.html">
        <p class="link-boxes-label">Install the Fortishield dashboard</p>

.. image:: ../../images/installation/Dashboard-Circle.png
     :align: center
     :height: 61px
     
.. raw:: html

      </a>
    </div>
  </div>

The Fortishield environment is now ready, and you can proceed with installing the Fortishield agent on the endpoints to be monitored. To perform this action, see the :doc:`Fortishield agent </installation-guide/fortishield-agent/index>` section.
