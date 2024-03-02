.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Fortishield provides security and compliance monitoring for various cloud platforms, including Google Cloud Platform (GCP), Amazon Web Services (AWS), and Microsoft Azure.

Posture management
==================

Cloud Service Posture Management (CSPM) encompasses a set of practices aimed at safeguarding the security and compliance of cloud environments. This involves the ongoing assessment and monitoring of cloud workloads to pinpoint misconfigurations, vulnerabilities, and potential threats. CSPM also offers actionable remediation steps for addressing security risks, ultimately bolstering the overall security posture of cloud environments.

Fortishield provides security and compliance monitoring for various cloud platforms, including Google Cloud Platform (GCP), Amazon Web Services (AWS), and Microsoft Azure. We leverage Fortishield for CSPM across the platforms listed below.

Google Cloud Platform
---------------------

Fortishield connects with GCP through the Google Cloud publisher and subscriber services, also known as GCP Pub/Sub. These messaging services facilitate the transmission of log data from a GCP workload to a Fortishield instance. The image below shows the integration between GCP and Fortishield.

.. thumbnail:: /images/getting-started/use-cases/posture-management/fortishield-gcp-integration.png
   :title: Integration between Fortishield and Google Cloud Platform
   :alt: Integration between Fortishield and Google Cloud Platform
   :align: center
   :width: 80%

You can configure your Fortishield instance to receive GCP logs using the Pub/Sub service. Once configured, you can enable the Google Cloud Platform module via the Fortishield dashboard to view logs related to your GCP services. We provide detailed guidelines on configuring Fortishield to receive GCP logs using the Pub/Sub service in our :doc:`using Fortishield to monitor GCP services </cloud-security/gcp/index>` documentation.

.. thumbnail:: /images/getting-started/use-cases/posture-management/using-fortishield-to-monitor-gcp.gif
   :title: Using Fortishield to monitor Google Cloud Platform
   :alt: Using Fortishield to monitor Google Cloud Platform
   :align: center
   :width: 80%

The image below shows an example log received from a monitored GCP instance on the Fortishield dashboard.

.. thumbnail:: /images/getting-started/use-cases/posture-management/fortishield-dashboard-gcp-example-log.png
   :title: Example GCP log on the Fortishield dashboard
   :alt: Example GCP log on the Fortishield dashboard
   :align: center
   :width: 80%

Amazon Web Services
-------------------

Fortishield provides CSPM to your AWS workloads by monitoring the AWS services and instances. Monitoring your AWS services includes collecting and analyzing log data about your AWS infrastructure using the :doc:`Fortishield module for AWS </cloud-security/amazon/services/index>`.

You can enable the Amazon AWS module via your Fortishield dashboard to view logs related to AWS services.

.. thumbnail:: /images/getting-started/use-cases/posture-management/enabling-aws-module.png
   :title: Enabling AWS module in the Fortishield dashboard
   :alt: Enabling AWS module in the Fortishield dashboard
   :align: center
   :width: 80%

Follow the :doc:`AWS prerequisite </cloud-security/amazon/services/prerequisites/index>` documentation to set up your Fortishield instance for AWS log collection. The documentation shows a list of the :doc:`supported AWS services </cloud-security/amazon/services/supported-services/index>` that Fortishield can monitor. The image below shows an Amazon Security Hub log received using the CloudWatch service.

.. thumbnail:: /images/getting-started/use-cases/posture-management/amazon-security-hub-log.png
   :title: Amazon Security Hub log
   :alt: Amazon Security Hub log
   :align: center
   :width: 80%

.. thumbnail:: /images/getting-started/use-cases/posture-management/amazon-security-hub-log-details.png
   :title: Amazon Security Hub log – Details
   :alt: Amazon Security Hub log – Details
   :align: center
   :width: 80%

This control is designed to assess the security configuration of S3 buckets by verifying that user permissions are not granted through access control lists (ACLs). It is recommended to use AWS Identity and Access Management (IAM) policies rather than S3 bucket ACLs for managing user permissions.

Microsoft Azure
---------------

Fortishield integrates with Azure using the Log Analytics Workspace. The Azure Log Analytics workspace is a service that facilitates storing log data from Azure Monitor and other Azure services, such as Microsoft Defender for Cloud. Fortishield provides a native integration module for Azure that retrieves logs from the Log Analytics Workspace.

.. thumbnail:: /images/getting-started/use-cases/posture-management/azure-log-analytics-workspace-integration.png
   :title: Azure Log Analytics Workspace integration with Fortishield overview
   :alt: Azure Log Analytics Workspace integration with Fortishield overview
   :align: center
   :width: 80%

We provide detailed guidelines on configuring Fortishield to receive Azure Cloud logs using the Log Analytics Workspace in our :doc:`Azure Log Analytics </cloud-security/azure/activity-services/services/log-analytics>` documentation. Once configured, you can set up your Fortishield deployment to retrieve *Recommendations*, *Security alerts*, and *Regulatory compliance* logs for your Azure cloud infrastructure.

The image below shows Azure security posture management logs received on Fortishield.

.. thumbnail:: /images/getting-started/use-cases/posture-management/azure-security-posture-management-logs.png
   :title: Azure security posture management logs
   :alt: Azure security posture management logs
   :align: center
   :width: 80%
