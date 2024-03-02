.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn how Fortishield helps to increase the security of AWS infrastructure, monitoring AWS instances and AWS services, in this section of our documentation. 
  
.. _amazon:

Using Fortishield to monitor AWS
==========================

Fortishield helps to increase the security of an AWS infrastructure in two different, complementary ways:

- **Installing the Fortishield agent on the instances** to monitor the activity inside them. It collects different types of system and application data and forwards it to the Fortishield manager. Different agent tasks or processes are used to monitor the system in different ways (e.g., monitoring file integrity, reading system log messages, and scanning system configurations).
- **Monitoring AWS services** to collect and analyze log data about the infrastructure. Thanks to the module for AWS, Fortishield can trigger alerts based on the events obtained from these services, which provide rich and complete information about the infrastructure, such as the instances configuration, unauthorized behavior, data stored on S3, and more.

In this section, you can learn about these two methods, what they do and how to configure and set them up.

.. topic:: Contents

  .. toctree::
    :maxdepth: 1

    instances
    services/index
