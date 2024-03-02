.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: This PoC shows how the Fortishield module for AWS (aws-s3) enables log data gathering from different AWS sources. Learn more about it in our documentation.

Monitoring AWS infrastructure
=============================

This use case shows how the Fortishield module for AWS (aws-s3) enables the log data collection from different AWS sources.

To learn more about monitoring AWS resources, see the :doc:`Using Fortishield to monitor AWS </cloud-security/amazon/index>` section of the documentation.

Infrastructure
--------------

+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cloud service      | Description                                                                                                                                                                                                                                                                       |
+====================+===================================================================================================================================================================================================================================================================================+
| Amazon CloudTrail  | AWS Cloudtrail, like all other supported AWS services, requires setting the :ref:`necessary policies <policy_cloudtrail>` for user permissions and providing a valid authentication method. In this PoC, we use the :ref:`profile authentication <aws_profile>` method.           |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Configuration
-------------

Take the following steps to configure Fortishield to monitor Amazon CloudTrail services and identify security incidents.

CloudTrail
^^^^^^^^^^

#. Access the CloudTrail service using the AWS console.

#. Create a new trail.

#. Choose between creating a new S3 bucket or specifying an existing one to store CloudTrail logs. Note down the name of the S3 bucket used as it’s necessary to specify it in the Fortishield configuration.

The image below shows how to create a new CloudTrail service and attach a new S3 bucket.

.. thumbnail:: /images/poc/cloudtrail.gif
   :title: Creating a Cloudtrail service
   :align: center
   :width: 80%

Fortishield server
^^^^^^^^^^^^

#. Enable the Fortishield AWS module in the ``/var/ossec/etc/ossec.conf`` configuration file on the Fortishield server. Add only the AWS buckets of interest. Read our guide on how to :doc:`Configure AWS credentials </cloud-security/amazon/services/prerequisites/credentials>`:

   .. code-block:: xml
      :emphasize-lines: 8, 9

      <wodle name="aws-s3">
        <disabled>no</disabled>
        <interval>30m</interval>
        <run_on_start>yes</run_on_start>
        <skip_on_error>no</skip_on_error>

        <bucket type="cloudtrail">
          <name><AWS_BUCKET_NAME></name>
          <aws_profile><AWS_PROFILE_NAME></aws_profile>
        </bucket>
      </wodle>

#. Restart the Fortishield manager to apply the changes:

   .. code-block:: console

      $ sudo systemctl restart fortishield-manager

Test the configuration
----------------------

Once you configure Cloudtrail, you can generate events by simply creating a new IAM user account using the IAM service. This generates an event that Fortishield processes. 

The Fortishield default ruleset parses AWS logs and generates alerts automatically. The alerts appear as soon as Fortishield receives the logs from the AWS S3 bucket.

You can also find additional :ref:`CloudTrail use cases <cloudtrail-use-cases>` in our documentation. 

Visualize the alerts
--------------------

You can visualize the alert data in the Fortishield dashboard. To do this, navigate through **Amazon Web Services** module.

.. thumbnail:: /images/poc/AWS-alerts.png
   :title: Visualize Amazon Web Services alerts 
   :align: center
   :width: 80%
