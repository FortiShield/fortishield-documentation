.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Check out this guide to learn how to build an environment composed of a Fortishield cluster integrated with the Elastic Stack using Kubernetes. 
   
Deployment on Kubernetes
========================

This section shows the process of installing, upgrading, and cleaning up Fortishield on Kubernetes.

`Kubernetes <https://kubernetes.io/>`_ is an open source container orchestration engine. Containers are microservices packaged with their dependencies and configurations. Kubernetes is meant to run across a cluster automating deployment, scaling, and management of containerized applications. It simplifies the operation of applications that span multiple containers deployed across multiple servers. For easy management and discovery, containers are grouped into pods, the basic operational unit for Kubernetes. Kubernetes pods are distributed among nodes to provide high availability. Kubernetes helps with networking, load-balancing, security, and scaling across all Kubernetes nodes running your containers. 

In this section of the documentation, you will see how to clone the `Fortishield Kubernetes repository <https://github.com/fortishield/fortishield-kubernetes>`_, set up certificates, apply the manifests, and deploy the necessary pods and services for installing Fortishield on Kubernetes in the cloud and local environments. In addition, you will find the :doc:`/deployment-options/deploying-with-kubernetes/kubernetes-conf` subsection, and you will learn to upgrade your implementation in the :doc:`/deployment-options/deploying-with-kubernetes/kubernetes-upgrade` subsection. Finally, you will see how to clean up both clusters and volumes in the :doc:`/deployment-options/deploying-with-kubernetes/kubernetes-clean-up` subsection.

.. toctree::
   :maxdepth: 1
   :hidden:

   kubernetes-conf
   kubernetes-deployment
   kubernetes-upgrade
   kubernetes-clean-up