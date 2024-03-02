.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn more about Kubernetes configuration for Fortishield: prerequisites, overview, how to verify the deployment, and more. 

.. _kubernetes_conf:

Kubernetes configuration
========================   

Pre-requisites
--------------

-  A Kubernetes cluster already deployed.
-  For Amazon EKS deployments using Kubernetes version 1.23 and later, an Amazon EBS CSI driver IAM role. The CSI driver requires that you assign an IAM role to work properly. Read AWS documentation to find instructions on `Creating the Amazon EBS CSI driver IAM role <https://docs.aws.amazon.com/eks/latest/userguide/csi-iam-role.html>`__. You need to install the CSI driver for both, new and old deployments. The CSI driver is an essential Kubernetes feature.
   
Resource Requirement
--------------------

To deploy Fortishield on Kubernetes, the cluster should have at least the following resources available:

- 2 CPU units
- 3 Gi of memory
- 2 Gi of storage
   
   
Overview
--------

StatefulSet and deployment controllers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a *Deployment*, a *StatefulSet* manages Pods that are based on an identical container specification, but it maintains an identity attached to each of its pods. These pods are created from the same specification, but they are not interchangeable: each one has a persistent identifier maintained across any rescheduling.

It is useful for stateful applications like databases that save the data to persistent storage. The states of each Fortishield manager and each Fortishield indexer should be maintained, so we declare them using StatefulSet to ensure that they maintain their states in every startup.

Deployments are intended for stateless use and are quite lightweight, and seem to be appropriate for the Fortishield dashboard, where it is not necessary to maintain the states.

Persistent volumes (PV) are pieces of storage in the provisioned cluster. It is a resource in the cluster just like a node is a cluster resource. Persistent volumes are volume plugins like Volumes but have a lifecycle independent of any individual pod that uses the PV. This API object captures the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.

Here, we use persistent volumes to store data from both the Fortishield manager and the Fortishield indexer.

Refer to the `persistent volumes <https://kubernetes.io/docs/concepts/storage/persistent-volumes/>`_ page for more information.

Pods
^^^^

You can check how we build our Fortishield docker containers in our `repository <https://github.com/fortishield/fortishield-docker>`_.

**Fortishield master**

This pod contains the master node of the Fortishield cluster. The master node centralizes and coordinates worker nodes, making sure the critical and required data is consistent across all nodes. The management is performed only in this node, so the agent enrollment service (authd) is placed here.

+-------------------------------+-------------+
| Image                         | Controller  |
+===============================+=============+
| fortishield/fortishield-manager           | StatefulSet |
+-------------------------------+-------------+

**Fortishield worker 0 / 1**

These pods contain a worker node of the Fortishield cluster. They will receive the agent events.

+-------------------------------+-------------+
| Image                         | Controller  |
+===============================+=============+
| fortishield/fortishield-manager           | StatefulSet |
+-------------------------------+-------------+

**Fortishield indexer**

The Fortishield indexer pod ingests events received from Filebeat.

+--------------------------------------------+-------------+
| Image                                      | Controller  |
+============================================+=============+
| fortishield/fortishield-indexer                        | StatefulSet |
+--------------------------------------------+-------------+

**Fortishield dashboard**

The Fortishield dashboard pod lets you visualize your Fortishield indexer data, along with other features such as the Fortishield app.

+--------------------------------------+-------------+
| Image                                | Controller  |
+======================================+=============+
| fortishield/fortishield-dashboard                | Deployment  |
+--------------------------------------+-------------+

Services
^^^^^^^^

**Fortishield indexer and dashboard**

+----------------------+-------------------------------------------------------------------------------------+
| Name                 | Description                                                                         |
+======================+=====================================================================================+
| fortishield-indexer        | Communication for Fortishield indexer nodes.                                              |
+----------------------+-------------------------------------------------------------------------------------+
| indexer              | This is the Fortishield indexer API used by the Fortishield dashboard to read/write alerts.     |
+----------------------+-------------------------------------------------------------------------------------+
| dashboard            | Fortishield dashboard service. \https://fortishield.your-domain.com:443                         |
+----------------------+-------------------------------------------------------------------------------------+

**Fortishield**

+----------------------+-------------------------------------------------------------------------+
| Name                 | Description                                                             |
+======================+=========================================================================+
| fortishield                | Fortishield API: fortishield-master.your-domain.com:55000                           |
|                      +-------------------------------------------------------------------------+
|                      | Agent registration service (authd): fortishield-master.your-domain.com:1515   |
+----------------------+-------------------------------------------------------------------------+
| fortishield-workers        | Reporting service: fortishield-manager.your-domain.com:1514                   |
+----------------------+-------------------------------------------------------------------------+
| fortishield-cluster        | Communication for Fortishield manager nodes.                                  |
+----------------------+-------------------------------------------------------------------------+

