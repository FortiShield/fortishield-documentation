.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Fortishield integrates with container platforms like Docker and Kubernetes. It actively monitors container runtime events, application logs, and overall container health. Learn more in this use case.
  
Container security
==================

Container security is an IT practice that is focused on safeguarding containers and their applications against security threats. Organizations can gain visibility into the usage of both containers and the applications they contain by implementing robust security measures in such an environment.

Containers offer lightweight, isolated environments with application code, runtime, and dependencies. They are widely used to deploy and scale applications both on-premises and in the cloud. As container applications and infrastructure become more popular, it becomes essential to protect them from potential threats. 

Fortishield for container security
----------------------------

Fortishield integrates with container platforms like Docker and Kubernetes and actively monitors container runtime events, application logs, and overall container health. Fortishield identifies anomalies by evaluating container logs against predefined rules. Additionally, it maintains a record of container engine actions to detect unauthorized activities in a containerized environment. It also monitors health metrics to prevent performance bottlenecks in an organization.

Fortishield container security features comprise monitoring container runtimes, tracking containerized application logs, monitoring container resource utilization, centralized logging, and container alert notifications. This comprehensive set of capabilities enhances security and streamlines incident response.

Container runtime monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Organizations can enhance the security of their containerized applications by monitoring container events. They can proactively address unexpected behavior by promptly responding to alerts triggered by predefined rules. Fortishield also provides insight into container engine interactions and detects irregularities in containerized applications. 

Monitoring the container engine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fortishield captures real-time events performed by the Docker engine via its :doc:`Docker listener </user-manual/capabilities/container-security/monitoring-docker>` module. This ensures that no crucial Docker event or operation goes undetected.

:ref:`monitoring_user_interaction_with_docker_resources` demonstrates how Fortishield enhances visibility into the interactions of the container engine with the containers and the images.

.. thumbnail:: /images/getting-started/use-cases/container-security/docker-container-interaction-alerts.png
   :title: Docker container user interaction alerts
   :alt: Docker container user interaction alerts
   :align: center
   :width: 80%

Fortishield also monitors the creation and destruction of resources in Kubernetes clusters to help identify unauthorized actions and potential security breaches.

The blog post on `Auditing Kubernetes with Fortishield <https://fortishield.github.io/blog/auditing-kubernetes-with-fortishield/>`__ demonstrates how to monitor Kubernetes resource interactions with Fortishield.

.. thumbnail:: /images/getting-started/use-cases/container-security/kubernetes-resource-interaction-alerts.png
   :title: Kubernetes resource interaction alerts
   :alt: Kubernetes resource interaction alerts
   :align: center
   :width: 80%

Monitoring containerized application logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fortishield allows organizations to monitor containerized applications. It provides visibility into the applications that are resident in the container. When the application events are forwarded to the Fortishield manager, Security engineers can create :doc:`custom rules </user-manual/ruleset/custom>` that align with the unique requirements of their organization. This facilitates a highly personalized approach that improves overall visibility into the containers and the applications they host.

The :ref:`Monitoring container runtime <monitoring_container_runtime>` documentation has more information about monitoring containerized application logs.

.. thumbnail:: /images/getting-started/use-cases/container-security/monitoring-containerized-application-logs.png
   :title: Monitoring containerized application logs
   :alt: Monitoring containerized application logs
   :align: center
   :width: 80%

Monitor container resource utilization with Fortishield
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fortishield tracks and analyzes the resource consumption of containerized applications. It provides insights into the CPU, memory, and network usage statistics of containers, assisting in identifying performance bottlenecks.

Fortishield provides customizable alerts and notifications, enabling organizations to detect and proactively respond to unusual resource spikes or consumption patterns.

The blog post on `Docker container security monitoring with Fortishield <https://fortishield.github.io/blog/docker-container-security-monitoring-with-fortishield/>`__ demonstrates how Fortishield monitors network utilization in a containerized environment.

.. thumbnail:: /images/getting-started/use-cases/container-security/monitoring-network-utilization.png
   :title: Monitoring network utilization in a containerized environment
   :alt: Monitoring network utilization in a containerized environment
   :align: center
   :width: 80%

Centralized logging and visualization of containers event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fortishield centralizes container event logging and visualization. Its scalable indexer aggregates logs into a powerful search and analytics engine, providing real-time insights. This indexer handles event influx while also supporting compliance needs such as log retention policies.

Fortishield enables organizations to view container logs from a customized dashboard. Security professionals can track and analyze unfolding activities, swiftly identifying threats and unauthorized actions. This early detection enables security professionals to respond to security incidents as they arise swiftly, establishing an active approach to minimizing risks.

The image below displays the customized container dashboard of Fortishield, where events from all containers are showcased.

.. thumbnail:: /images/getting-started/use-cases/container-security/customized-container-dashboard.png
   :title: Customized container dashboard
   :alt: Customized container dashboard
   :align: center
   :width: 80%

Container alert notification with Fortishield
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fortishield integrates with messaging platforms like :doc:`email </user-manual/manager/manual-email-report/index>` and :ref:`Slack <slack_manual_integration>`. It also integrates with case management solutions, like `Jira <https://fortishield.github.io/blog/how-to-integrate-external-software-using-integrator/>`__ , for incident response and real-time alerting. This ensures that security teams are promptly notified whenever potential threats or unauthorized actions occur in containerized environments.

The documentation on :doc:`/user-manual/manager/manual-integration` explains how the Integrator daemon allows Fortishield to connect to external APIs and case management systems tools like :ref:`PagerDuty <pagerduty_manual_integration>`.

.. thumbnail:: /images/getting-started/use-cases/container-security/connect-external-API.png
   :title: Connect to external APIs and case management systems
   :alt: Connect to external APIs and case management systems
   :align: center
   :width: 80%
