.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Find out more about the process of upgrading the Fortishield central components, Open Distro for Elasticsearch, Elastic Stack, and Fortishield agents in this section.
  
Upgrade guide
=============

This guide includes instructions to upgrade the :doc:`Fortishield components </getting-started/components/index>`. 

Check the :doc:`compatibility-matrix/index` section to learn about the compatibility requirements between components.

Upgrade the Fortishield central components
------------------------------------

The :doc:`upgrading-central-components` section includes instructions to upgrade the Fortishield server, the Fortishield indexer, and the Fortishield dashboard.

.. note::
  
   Since Fortishield v4.6.0, we don't provide the Kibana plugin and Splunk app anymore. To integrate Fortishield with Elastic or Splunk, refer to our :doc:`/integrations-guide/index`.

Upgrade the Fortishield agents
------------------------

You can upgrade the Fortishield agents either remotely from the Fortishield manager or locally. Upgrading the Fortishield agents remotely is possible by using the ``agent_upgrade`` tool and the Fortishield API. See the :doc:`Remote agent upgrade </user-manual/agents/remote-upgrading/upgrading-agent>` section to learn more.

To perform the upgrade locally, select your operating system and follow the instructions. 

.. raw:: html

  <div class="link-boxes-group layout-6">
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/linux.html">
        <p class="link-boxes-label">Linux</p>

.. image:: /images/installation/linux.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/windows.html">
        <p class="link-boxes-label">Windows</p>

.. image:: /images/installation/windows-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/macos.html">
        <p class="link-boxes-label">macOS</p>

.. image:: /images/installation/macOS-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/solaris.html">
        <p class="link-boxes-label">Solaris</p>

.. image:: /images/installation/solaris.png
      :align: center
      :width: 150px

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/aix.html">
        <p class="link-boxes-label">AIX</p>

.. image:: /images/installation/AIX.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./fortishield-agent/hp-ux.html">
        <p class="link-boxes-label">HP-UX</p>

.. image:: /images/installation/hpux.png
      :align: center

.. raw:: html

      </a>
    </div>
  </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   upgrading-central-components
   fortishield-agent/index
   compatibility-matrix/index
