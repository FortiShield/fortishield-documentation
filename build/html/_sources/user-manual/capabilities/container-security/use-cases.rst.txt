.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Find use cases on monitoring the Docker environment with Fortishield in this section of our documentation.

Use cases
=========

In these use cases, we create a Docker setup, and demonstrate how Fortishield logs activities that occur in the Docker environment.

Requirements
------------

-  Docker installed on an Ubuntu 22.04 endpoint. Follow the `official documentation <https://docs.docker.com/engine/install/ubuntu/>`__ to set up Docker.
-  :doc:`Install Fortishield agent </installation-guide/fortishield-agent/index>` on the Docker server, and enroll it to a Fortishield server.
-  :ref:`Enable the Fortishield Docker listener <enable-fortishield-docker-listener>` on the Docker server.

.. _monitoring_user_interaction_with_docker_resources:

Monitoring user interaction with Docker resources
-------------------------------------------------

In this use case, we demonstrate how Fortishield monitors Docker events and triggers alerts for interaction with containers and images. Perform the following steps to test the use case:

#. Run ``test-container`` from the ``httpd`` image:

   .. code-block:: console

      # docker run -d --name test-container httpd

#. Pause ``test-container``:

   .. code-block:: console

      # docker pause test-container

#. Resume ``test-container``:

   .. code-block:: console

      # docker unpause test-container

#. Stop ``test-container``:

   .. code-block:: console

      # docker stop test-container

#. Remove ``test-container``:

   .. code-block:: console

      # docker rm test-container

#. Remove the ``httpd`` image:

   .. code-block:: console

      # docker rmi httpd

View the alerts on the Fortishield dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to the **Threat Hunting** module or the dedicated **Docker listener dashboard** on the Fortishield dashboard to view the alerts. The following alerts are generated when we perform all the actions above. We have highlighted the alerts and labeled them according to the action that triggered each of them for ease of understanding.

.. thumbnail:: /images/manual/container-security/docker-listener-alerts.png
   :title: Docker listener alerts
   :alt: Docker listener alerts
   :align: center
   :width: 80% 

Below, we show the full data of an alert triggered when a Docker container is started:

.. code-block:: JSON
   :emphasize-lines: 10-29

   {
     "agent": {
       "ip": "192.168.132.140",
       "name": "Ubuntu22",
       "id": "001"
     },
     "manager": {
       "name": "fortishield-server"
     },
     "data": {
       "integration": "docker",
       "docker": {
         "Type": "container",
         "Action": "start",
         "Actor": {
           "Attributes": {
             "image": "httpd",
             "name": "test-container"
           },
           "ID": "d47511d28ebf226e6bebff7be58ba8b03cb62fba7686a877e565d837e3d438da"
         },
         "scope": "local",
         "from": "httpd",
         "timeNano": "1683632491049788416.000000",
         "id": "d47511d28ebf226e6bebff7be58ba8b03cb62fba7686a877e565d837e3d438da",
         "time": "1683632491",
         "status": "start"
       }
     },
     "rule": {
       "firedtimes": 3,
       "mail": false,
       "level": 3,
       "description": "Docker: Container test-container started",
       "groups": [
         "docker"
       ],
       "id": "87903"
     },
     "decoder": {
       "name": "json"
     },
     "input": {
       "type": "log"
     },
     "@timestamp": "2023-05-09T11:41:31.033Z",
     "location": "Fortishield-Docker",
     "id": "1683632491.847900",
     "timestamp": "2023-05-09T14:41:31.033+0300",
     "_id": "ApVRAIgBKQU4L4_oLMjj"
   }

.. _monitoring_container_runtime:

Monitoring container runtime
----------------------------

All Docker container runtime logs on Linux endpoints are saved by default to ``/var/lib/docker/containers/<CONTAINER_ID>/<CONTAINER_ID>-json.log``. In this use case, we show how Fortishield monitors the runtime logs of a web container to detect web attacks.

Fortishield agent configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Configure the Fortishield agent on the Docker server to forward all container runtime logs to the Fortishield server. Add the following configuration to the ``/var/ossec/etc/ossec.conf`` agent configuration file:

   .. code-block:: XML

      <localfile>
        <log_format>syslog</log_format>
        <location>/var/lib/docker/containers/*/*-json.log</location>
      </localfile>

   -  We use wildcards ``*`` in the ``<location>`` field of the configuration so Fortishield can monitor the dynamically named log file path. The file path of the container log usually contains the container ID as shown in the pattern ``/var/lib/docker/containers/<CONTAINER_ID>/<CONTAINER_ID>-json.log``

#. Restart the Fortishield agent service to apply the changes:

   .. code-block:: console

      # systemctl restart fortishield-agent

Fortishield server configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Add the following decoders to the ``/var/ossec/etc/decoders/local_decoder.xml`` decoder file on the Fortishield server:

   .. code-block:: XML
      :emphasize-lines: 1, 10

      <decoder name="web-accesslog-docker">
        <parent>json</parent>
        <type>web-log</type>
        <use_own_name>true</use_own_name>
        <prematch offset="after_parent">^log":"\S+ \S+ \S+ \.*[\S+ \S\d+] \.*"\w+ \S+ HTTP\S+" \d+</prematch>
        <regex offset="after_parent">^log":"(\S+) \S+ \S+ \.*[\S+ \S\d+] \.*"(\w+) (\S+) HTTP\S+" (\d+)</regex>
        <order>srcip,protocol,url,id</order>
      </decoder>

      <decoder name="json">
        <parent>json</parent>
        <use_own_name>true</use_own_name>
        <plugin_decoder>JSON_Decoder</plugin_decoder>
      </decoder>

   -  The ``web-accesslog-docker`` decoder extracts the relevant fields in a web log, and sets the log type to ``web-log`` so the Fortishield analysis engine can analyze the log for web attacks. 
   -  The ``json`` decoder enables Fortishield to continue decoding the log as a regular json log in case it does not meet the criteria of the first decoder ``web-accesslog-docker``.

#. Restart the Fortishield manager service to apply the changes:

   .. code-block:: console

      # systemctl restart fortishield-manager

Run the Docker container and simulate the attack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command on the Docker server to create a web container called ``test-container``:

   .. code-block:: console

      # docker run --name test-container -p 80:80 -d nginx

#. Run the following command on the Fortishield server to simulate an SQL injection (SQLi) attack. Replace ``<WEB_IP_ADDRESS>`` with the IP address of the Docker server:

   .. code-block:: console

      # curl -XGET "http://<WEB_IP_ADDRESS>/users/?id=SELECT+*+FROM+users";

View the alerts on the Fortishield dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to the **Threat Hunting** module on the Fortishield dashboard to view the alert. The following alert is generated when we simulate the SQLi attack.

.. thumbnail:: /images/manual/container-security/SQL-injection-attempt-alert.png
   :title: SQL injection attempt alert
   :alt: SQL injection attempt alert
   :align: center
   :width: 80% 

We show the full alert event data below:

.. note::

   The highlighted ``location`` field in the alert data shows the container where the event was generated.

.. code-block:: JSON
   :emphasize-lines: 34, 65, 70

   {
     "agent": {
       "ip": "192.168.132.140",
       "name": "Ubuntu22",
       "id": "001"
     },
     "manager": {
       "name": "fortishield-server"
     },
     "data": {
       "protocol": "GET",
       "srcip": "192.168.132.1",
       "id": "404",
       "url": "/users/?id=SELECT+*+FROM+users"
     },
     "rule": {
       "firedtimes": 1,
       "mail": false,
       "level": 7,
       "pci_dss": [
         "6.5",
         "11.4",
         "6.5.1"
       ],
       "tsc": [
         "CC6.6",
         "CC7.1",
         "CC8.1",
         "CC6.1",
         "CC6.8",
         "CC7.2",
         "CC7.3"
       ],
       "description": "SQL injection attempt.",
       "groups": [
         "web",
         "accesslog",
         "attack",
         "sql_injection"
       ],
       "mitre": {
         "technique": [
           "Exploit Public-Facing Application"
         ],
         "id": [
           "T1190"
         ],
         "tactic": [
           "Initial Access"
         ]
       },
       "id": "31103",
       "nist_800_53": [
         "SA.11",
         "SI.4"
       ],
       "gdpr": [
         "IV_35.7.d"
       ]
     },
     "decoder": {
       "parent": "json",
       "name": "web-accesslog-docker"
     },
     "full_log": "{\"log\":\"192.168.132.1 - - [12/May/2023:14:12:14 +0000] \\\"GET /users/?id=SELECT+*+FROM+users HTTP/1.1\\\" 404 153 \\\"-\\\" \\\"curl/7.68.0\\\" \\\"-\\\"\\n\",\"stream\":\"stdout\",\"time\":\"2023-05-12T14:12:14.882936144Z\"}",
     "input": {
       "type": "log"
     },
     "@timestamp": "2023-05-12T14:12:15.875Z",
     "location": "/var/lib/docker/containers/f736fa30f2ce3f818425ae562696ca84910e4ac1c13d2ca884052b2f1622f871/f736fa30f2ce3f818425ae562696ca84910e4ac1c13d2ca884052b2f1622f871-json.log",
     "id": "1683900735.283081",
     "timestamp": "2023-05-12T17:12:15.875+0300",
     "_id": "wZVOEIgBKQU4L4_oKMyk"
   }
