.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Visit the Fortishield installation guide and learn more about the deployment process, available installation alternatives, and requirements.
  
.. _installation_guide:


Installation guide
==================

Fortishield is a security platform that provides unified XDR and SIEM protection for endpoints and cloud workloads. The solution is composed of a single universal agent and three central components: the Fortishield server, the Fortishield indexer, and the Fortishield dashboard. For more information, check the :doc:`Getting Started </getting-started/index>` documentation. 

Fortishield is free and open source. Its components abide by the `GNU General Public License, version 2 <https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html>`_, and the `Apache License, Version 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_ (ALv2). 

In this installation guide, you will learn how to install Fortishield in your infrastructure. We also offer `Fortishield Cloud <https://fortishield.github.io/cloud/>`_, our software as a service (SaaS) solution. Fortishield cloud is ready to use, with no additional hardware or software required, driving down the cost and complexity. Check the :doc:`Cloud service </cloud-service/index>` documentation for more information and take advantage of the `Cloud trial <https://console.cloud.fortishield.github.io/sign-up?landing=trial>`_ to explore this service.


Installing the Fortishield central components
---------------------------------------

The Fortishield indexer and Fortishield server can be installed on a single host or be distributed in cluster configurations. You can choose between two installation methods for each Fortishield central component. Both options provide instructions to install the central components on a single host or on separate hosts.

You can check our :doc:`Quickstart </quickstart>` documentation to perform an all-in-one installation. This is the fastest way to get the Fortishield central components up and running.

For more deployment flexibility and customization, install the Fortishield central components by starting with the :doc:`Fortishield indexer <fortishield-indexer/index>` deployment. This deployment method allows the all-in-one installation, and the installation of the components on separate servers.

This is the installation workflow you will follow:

.. raw:: html

  <div class="link-boxes-group layout-3" data-step="0">
    <div class="steps-line">
      <div class="steps-number future-step">1</div>
      <div class="steps-number future-step">2</div>
      <div class="steps-number future-step">3</div>
    </div>
    <div class="link-boxes-item future-step">
      <a class="link-boxes-link" href="fortishield-indexer/index.html">
        <p class="link-boxes-label">Install the Fortishield indexer</p>

.. image:: ../images/installation/Indexer-noBG.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item future-step">
      <a class="link-boxes-link" href="fortishield-server/index.html">
        <p class="link-boxes-label">Install the Fortishield server</p>

.. image:: ../images/installation/Server-noBG.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item future-step">
      <a class="link-boxes-link" href="fortishield-dashboard/index.html">
        <p class="link-boxes-label">Install the Fortishield dashboard</p>

.. image:: ../images/installation/Dashboard-noBG.png
     :align: center
     :height: 61px
     
.. raw:: html

      </a>
    </div>
  </div>


Installing the Fortishield agent
--------------------------

The Fortishield agent is a single and lightweight monitoring software. It is a multi-platform component that can be deployed to laptops, desktops, servers, cloud instances, containers, or virtual machines. It provides visibility into the endpoint's security by collecting critical system and application records, inventory data, and detecting anomalies. 

If the Fortishield central components are already installed in your environment, select your operating system below and follow the installation steps to deploy the agent on the endpoints. 


.. raw:: html

  <div class="link-boxes-group layout-6">
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/fortishield-agent-package-linux.html">
        <p class="link-boxes-label">Linux</p>

.. image:: /images/installation/linux.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/fortishield-agent-package-windows.html">
        <p class="link-boxes-label">Windows</p>

.. image:: /images/installation/windows-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/fortishield-agent-package-macos.html">
        <p class="link-boxes-label">macOS</p>

.. image:: /images/installation/macOS-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/fortishield-agent-package-solaris.html">
        <p class="link-boxes-label">Solaris</p>

.. image:: /images/installation/solaris.png
      :align: center
      :width: 150px

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/fortishield-agent-package-aix.html">
        <p class="link-boxes-label">AIX</p>

.. image:: /images/installation/AIX.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/fortishield-agent-package-hpux.html">
        <p class="link-boxes-label">HP-UX</p>

.. image:: /images/installation/hpux.png
      :align: center

.. raw:: html

      </a>
    </div>
  </div>



Packages list
-------------

In the :doc:`Packages list </installation-guide/packages-list>` section, you will find all the packages required for the installation of Fortishield.

Other installation alternatives
-------------------------------

Fortishield provides other :doc:`installation alternatives </deployment-options/index>`. These are complementary to the installation methods of this installation guide. You will find instructions on how to deploy Fortishield using ready-to-use machines, containers, and orchestration tools. There is also information on how to install the solution offline, from sources, and with commercial options.


.. toctree::
    :hidden:
    :maxdepth: 1

    fortishield-indexer/index
    fortishield-server/index
    fortishield-dashboard/index
    fortishield-agent/index
    packages-list
