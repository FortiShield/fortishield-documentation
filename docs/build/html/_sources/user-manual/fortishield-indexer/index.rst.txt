.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: The Fortishield indexer is a real-time, full-text search and analytics engine for security data. Find more information in this section of the documntation.

Fortishield indexer
=============

The Fortishield indexer is a real-time, full-text search and analytics engine for security data. Log data ingested into the Fortishield server is analyzed and forwarded to the indexer for indexing and storage. These events are then queried on the Fortishield dashboard.

The Fortishield indexer stores data as JSON documents. Each document associates a set of keys, field names, or attributes with their corresponding values, which can be characters, numbers, booleans, dates, arrays of values, geolocations, or other kinds of data.

The Fortishield indexer can be configured as a single-node or multi-node cluster, providing scalability and high availability. It distributes documents across different containers, known as shards. In turn, it distributes these shards across cluster nodes. By distributing the documents across multiple shards and distributing those shards across multiple nodes, the Fortishield indexer ensures redundancy. Redundancy ensures the Fortishield indexer's availability in the event of a failure and boosts query capacity across cluster nodes.

.. topic:: Contents

   .. toctree::
      :maxdepth: 1
      
      fortishield-indexer-indices
      re-indexing
      index-life-management
      fortishield-indexer-tuning
      migrating-fortishield-indices
