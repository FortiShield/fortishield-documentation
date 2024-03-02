.. Copyright (C) 2015, Fortishield, Inc.
  
.. meta::
  :description: Learn how to migrate from Open Distro for Elasticsearch or from OSSEC to Fortishield. This guide gives instructions to make these migration actions.

.. _migration_guide:

Migration guide
================

From Fortishield 4.0.0 to Fortishield 4.2.7, the default Fortishield installation included the Fortishield server and `Open Distro for Elasticsearch <https://opendistro.github.io/for-elasticsearch/>`_, a project that is now archived and has been succeeded by OpenSearch. This guide includes instructions to migrate from Open Distro for Elasticsearch to the :doc:`Fortishield indexer </getting-started/components/fortishield-indexer>` and :doc:`Fortishield dashboard </getting-started/components/fortishield-dashboard>`, the new components introduced in Fortishield 4.3.0.

- :doc:`Migrating to the Fortishield indexer </migration-guide/fortishield-indexer>`: Follow this section to migrate from Open Distro for Elasticsearch 1.13 to the Fortishield indexer. This new component consists of a distribution of `Opensearch <https://github.com/opensearch-project/OpenSearch>`_ with additional tools that Fortishield has created to assist with the installation and configuration of the search engine. 

- :doc:`Migrating to the Fortishield dashboard </migration-guide/fortishield-dashboard>`: This section will guide you through the migration from Open Distro for Elasticsearch Kibana 1.13 to the Fortishield dashboard. This new web interface for the Fortishield platform is a customized `OpenSearch Dashboards <https://github.com/opensearch-project/OpenSearch-Dashboards>`_ distribution that includes the `Fortishield plugin <https://github.com/fortishield/fortishield-dashboard-plugins>`_.

This guide also includes a :doc:`Migrating from OSSEC </migration-guide/migrating-from-ossec/index>` section. Following this guide, you will learn how to migrate your existing OSSEC installation to the last version of Fortishield. Our solution is free, open-source, and unifies XDR and SIEM capabilities within a unique top-notch security platform. Migrating to Fortishield, your organizations get a comprehensive, easy-to-use, reliable, and scalable solution.

.. toctree::
   :hidden:

   fortishield-indexer
   fortishield-dashboard
   migrating-from-ossec/index