.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Fortishield collects, analyzes, and stores logs from endpoints, network devices, and applications. Find more information in this getting started use-case.
  
Log data analysis
=================

Log data analysis is a crucial process that involves examining and extracting valuable insights from log files created by different systems, applications, or devices. These logs contain records of events that provide useful information for troubleshooting, security analysis and monitoring,  and optimizing performance. Log data analysis is an essential practice that contributes to a secure, efficient, and reliable IT ecosystem.

Fortishield collects, analyzes, and stores logs from endpoints, network devices, and applications. The Fortishield agent, running on a monitored endpoint collects and forwards system and application logs to the Fortishield server for analysis. Additionally, you can send log messages to the Fortishield server via syslog or third-party API integrations.

Log data collection
-------------------

Fortishield collects logs from a wide range of sources, enabling comprehensive monitoring of various aspects of your IT environment. You can check our documentation on :doc:`Log data collection </user-manual/capabilities/log-data-collection/index>` to understand better how Fortishield collects and analyzes logs from monitored endpoints. Some of the common log sources supported by Fortishield include:

-  **Operating system logs**: Fortishield collects logs from several operating systems, including :ref:`Linux <how-to-collect-linuxlogs>`, :ref:`Windows <how-to-collect-windowslogs>`, and :ref:`macOS <how-to-collect-macoslogs>`.

   Fortishield can collect syslog, auditd, application logs, and others from Linux endpoints.

   Fortishield collects logs on Windows endpoints using the Windows event channel and Windows event log format. By default, the Fortishield agent monitors the System, Application, and Security Windows event channels on Windows endpoints. The Fortishield agent offers the flexibility to configure and monitor other :ref:`Windows event channels <windows_event_channel_log_collection>`. 

   Fortishield utilizes the unified logging system (ULS) to collect logs on macOS endpoints. The macOS ULS centralizes the management and storage of logs across all the system levels.

   The image below shows an event collected from the ``Microsoft-Windows-Sysmon/Operational`` event channel on a Windows endpoint.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/sysmon-operational-event-channel-alert.png
      :title: Sysmon operational Event channel alert
      :alt: Sysmon operational Event channel alert
      :align: center
      :width: 80%

-  **Syslog events**: Fortishield gathers logs from :doc:`syslog-enabled </user-manual/capabilities/log-data-collection/how-it-works>` devices, encompassing a wide array of sources including Linux/Unix systems and network devices that do not support agent installation. The image below shows an alert triggered when a new user is created on the Linux endpoint and the log is forwarded to the Fortishield server via rsyslog.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/new-user-added-alert.png
      :title: New user added to the system alert
      :alt: New user added to the system alert
      :align: center
      :width: 80%

-  **Agentless monitoring**: The Fortishield agentless monitoring module monitors endpoints that don't support agent installation. It requires an SSH connection between the endpoint and the Fortishield server. The Fortishield :doc:`agentless monitoring </user-manual/capabilities/agentless-monitoring/how-it-works>` module monitors files, directories, or configurations and runs commands on the endpoint. The image below is an alert from an agentless device on the Fortishield dashboard.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/agentless-device-alert.png
      :title: Agentless device alert
      :alt: Agentless device alert
      :align: center
      :width: 80%

-  **Cloud provider logs**: Fortishield integrates with cloud providers like :doc:`AWS </cloud-security/amazon/index>`, :doc:`Azure </cloud-security/azure/index>`, :doc:`Google Cloud </cloud-security/gcp/index>`, and :doc:`Office 365 </cloud-security/office365/index>` to collect logs from cloud services such as EC2 instances, S3 buckets, Azure VMs, and more. The image below shows the various cloud provider modules on the Fortishield dashboard.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/cloud-provider-modules.png
      :title: Cloud provider modules
      :alt: Cloud provider modules
      :align: center
      :width: 80%

-  **Custom logs**: You can configure Fortishield to collect and parse logs from several applications and third-party security tools like :doc:`VirusTotal </user-manual/capabilities/malware-detection/virus-total-integration>`, :doc:`Windows Defender </user-manual/capabilities/malware-detection/win-defender-logs-collection>`, and :doc:`ClamAV </user-manual/capabilities/malware-detection/clam-av-logs-collection>`. The image below shows an alert of a log from VirusTotal processed by the Fortishield server.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/virustotal-log-alert.png
      :title: VirusTotal log alert
      :alt: VirusTotal log alert
      :align: center
      :width: 80%

Rules and decoders
------------------

Fortishield :doc:`rules and decoders </user-manual/ruleset/index>` are core components in log data analysis and threat detection and response. Fortishield provides a powerful platform for log data analysis, allowing organizations to enhance their security posture by promptly detecting and responding to potential security threats.

Fortishield decoders are responsible for parsing and normalizing log data collected from various sources. Decoders are essential for converting the raw log data in several formats into a unified and structured format that Fortishield can process effectively. Fortishield has pre-built decoders for common log formats such as syslog, Windows event channel, macOS ULS, and more. Additionally, Fortishield allows you to define :doc:`custom decoders </user-manual/ruleset/custom>` for parsing logs from specific applications or devices with unique log formats. By using decoders, Fortishield can efficiently interpret log data and extract relevant information, such as timestamps, log levels, source IP addresses, user names, and more. As shown below, you can view Fortishield out-of-the-box and custom decoders on the **Decoders** module of the Fortishield dashboard.

.. thumbnail:: /images/getting-started/use-cases/log-data-analysis/decoders-in-fortishield-dashboard.png
   :title: Decoders in Fortishield dashboard
   :alt: Decoders in Fortishield dashboard
   :align: center
   :width: 80%

Fortishield ruleset detects security events and anomalies in log data. These rules are written in a specific format and they trigger alerts when certain conditions are met. The rules are defined based on certain criteria like log fields, values, or patterns to match specific log entries that may indicate security threats. Fortishield provides a wide range of pre-built rules covering common security use cases. Additionally, administrators can create :doc:`custom rules </user-manual/ruleset/custom>` tailored to their specific environment and security requirements. The **Rules** module of the Fortishield dashboard lets you view the default and custom rules.

.. thumbnail:: /images/getting-started/use-cases/log-data-analysis/rules-in-fortishield-dashboard.png
   :title: Rules in Fortishield dashboard
   :alt: Rules in Fortishield dashboard
   :align: center
   :width: 80%

For example, the rule below includes a ``match`` field used to define the pattern that the rule looks for. The rule also has a ``level`` field that specifies the priority of the resulting alert. Additionally, rules enrich events with technique identifiers from the MITRE ATT&CK framework and map them to regulatory compliance controls.

.. code-block:: xml

   <rule id="5715" level="3">
     <if_sid>5700</if_sid>
     <match>^Accepted|authenticated.$</match>
     <description>sshd: authentication success.</description>
     <mitre>
       <id>T1078</id>
       <id>T1021</id>
     </mitre>
     <group>authentication_success,gdpr_IV_32.2,gpg13_7.1,gpg13_7.2,hipaa_164.312.b,nist_800_53_AU.14,nist_800_53_AC.7,pci_dss_10.2.5,tsc_CC6.8,tsc_CC7.2,tsc_CC7.3,</group>
   </rule>

Log data indexing and storage
-----------------------------

The :doc:`Fortishield indexer </getting-started/components/fortishield-indexer>` is a highly scalable, distributed real-time search and analytics engine. The Fortishield indexer is critical in log analysis as it stores and indexes alerts generated by the Fortishield server. These alerts are stored as JSON documents.

The Fortishield indexer guarantees redundancy by storing the JSON documents across several containers called shards and distributing the shards across multiple nodes.  This implementation prevents downtime when hardware failures or cyber-attacks occur and increases query capacity as nodes are added to a cluster.

Fortishield uses four indices to store several event types:

-  **fortishield-alerts** stores alerts generated by the Fortishield server when an event triggers a rule with high enough priority. The image below shows alerts in the **Threat Hunting** module of the Fortishield dashboard. The index pattern is set to ``fortishield-alerts-*`` by default.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/alerts-in-index-pattern.png
      :title: Alerts in the fortishield-alerts-* index pattern
      :alt: Alerts in the fortishield-alerts-* index pattern
      :align: center
      :width: 80%

-  **fortishield-archives** index stores all events received from the Fortishield server regardless of whether they trigger an alert. The :doc:`Fortishield archives </user-manual/manager/fortishield-archives>` use this index to enable log retention and querying capabilities that offer deeper insight into events happening within monitored endpoints. Fortishield archives are disabled by default because of the huge storage requirements needed to store all the logs. The image below shows archived events in the **Discover** section of Fortishield dashboard with the index pattern set to ``fortishield-archives-*``.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/events-in-index-pattern.png
      :title: Events in fortishield-archives-* index pattern
      :alt: Events in fortishield-archives-* index pattern
      :align: center
      :width: 80%

-  **fortishield-monitoring** index stores data about the state of Fortishield agents over a period of time. The state of the agent could be ``Active``, ``Disconnected``, or ``Never connected``. This information is very useful in tracking Fortishield agents that are not reporting to the dashboard for several reasons that need investigation. The image below shows the connection status of the agents on the Fortishield dashboard. The agent information as shown in the image is collected from the ``fortishield-monitoring`` index.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/agent-monitoring-information.png
      :title: Agent information from fortishield-monitoring index
      :alt: Agent information from fortishield-monitoring index
      :align: center
      :width: 80%

-  **fortishield-statistics** index stores performance data related to the Fortishield server. This information is critical to ensuring the Fortishield server performs optimally with the available computing resources. The image below shows performance-related events on the Fortishield dashboard.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/performance-related-events.png
      :title: Performance-related events
      :alt: Performance-related events
      :align: center
      :width: 80%

Log data querying and visualization 
-----------------------------------

The Fortishield dashboard offers log data querying and visualization capabilities. You can leverage the dashboard’s intuitive interface to conduct complex searches and queries to extract meaningful insights from the log data collected by Fortishield.

Fortishield provides a set of predefined dashboards and visualizations out of the box, specifically tailored to security monitoring and compliance use cases. These dashboards provide insight into common security events such as failed logins, malware detection, and system anomalies. You can further customize these dashboards to suit your specific needs and requirements. Below is a sample image of the **Security event** dashboard showing several interesting information like **Top 5 PCI DSS Requirements**, **Top 5 alerts**, and **Alert groups evolution**.

   .. thumbnail:: /images/getting-started/use-cases/log-data-analysis/security-event-dashboard.png
      :title: Security event dashboard
      :alt: Security event dashboard
      :align: center
      :width: 80%

The Fortishield dashboard enables users to explore log entries in real time, apply various filters, and drill down into specific events or time ranges. This flexibility allows security analysts to identify trends, anomalies, and potential security incidents within their environment.

Fortishield allows users to :doc:`create customized dashboards </user-manual/fortishield-dashboard/creating-custom-dashboards>` that display key performance indicators, security metrics, and real-time monitoring of critical systems and applications. Users can assemble multiple visualizations, such as pie charts, line graphs, and heat maps, onto a single dashboard, providing a holistic view of their infrastructure's security posture. The following blog posts detailed how to query and create custom dashboards:

-  `Monitoring macOS resources with Fortishield <https://fortishield.github.io/blog/monitoring-macos-resources/>`__
-  `Monitoring Linux resources with Fortishield <https://fortishield.github.io/blog/monitoring-linux-resource-usage-with-fortishield/>`__
-  `Monitoring Windows resources with Performance Counters <https://fortishield.github.io/blog/monitoring-windows-resources-with-performance-counters/>`__
