.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
   :description: Learn how to restart the Fortishield agent to apply configuration changes using active response in this use case.

Restarting the Fortishield agent with active response
===============================================

You can use the ``restart-fortishield`` active response script to restart the Fortishield agent on a monitored endpoint. In this use case, we configure it to restart the Fortishield agent whenever the ``/var/ossec/etc/ossec.conf`` configuration file changes.

Infrastructure
--------------

================ ===========
Endpoint         Description
================ ===========
**Ubuntu 22.04** We save changes to the Fortishield agent configuration file on this endpoint to trigger an active response.
================ ===========

Fortishield server
------------

#. Open the Fortishield server ``/var/ossec/etc/ossec.conf`` file and verify that a ``<command>`` block called ``restart-fortishield`` with the following configuration is present within the ``<ossec_config>`` block:

   .. code-block::

      <command>
        <name>restart-fortishield</name>
        <executable>restart-fortishield</executable>
      </command>

   The ``<command>`` block contains information about the action to be executed on the Fortishield agent:

   -  ``<name>``: Sets a name for the command. In this case, ``restart-fortishield``.
   -  ``<executable>``: Specifies the active response script or executable that must run after a trigger. In this case, it’s the ``restart-fortishield`` executable.
   -  ``<timeout_allowed>``: Allows a timeout after a period of time. This tag is set to no here, which represents a stateless active response.

#. Add the ``<active-response>`` block below to the Fortishield server ``/var/ossec/etc/ossec.conf`` configuration file:

   .. code-block:: xml

      <ossec_config>
        <active-response>
          <command>restart-fortishield</command>
          <location>local</location>
          <rules_id>100009</rules_id>
        </active-response>
      </ossec_config>

   -  ``<command>``: Specifies the command to configure. This is the command name ``restart-fortishield`` defined in the previous step.
   -  ``<location>``: Specifies where the command executes. Using the ``local`` value here means that the command executes on the monitored endpoint where the trigger event occurs.
   -  ``<rules_id>``: The active response module executes the command if rule ID ``100009`` fires.

#. Add the rules below to the Fortishield server ``/var/ossec/etc/rules/local_rules.xml`` configuration file:

   .. code-block:: xml

      <group name="restart,">
        <rule id="100009" level="5">
          <if_sid>550</if_sid>
          <match>ossec.conf</match>
          <description>Changes made to the agent configuration file - $(file)</description>
        </rule>
      </group>

   This rule detects changes in the Fortishield agent configuration file.

#. Restart the Fortishield manager service to apply changes:

   .. code-block:: console

      $ sudo systemctl restart fortishield-manager

Ubuntu endpoint
---------------

#. Edit the ``/var/ossec/etc/ossec.conf`` file and add the following configuration to the ``<syscheck>`` section:

   .. code-block:: xml

      <directories realtime="yes">/var/ossec/etc/ossec.conf</directories>

   This monitors the Fortishield agent configuration file for any changes.

#. Restart the Fortishield agent service to apply changes:

   .. code-block:: console

      $ sudo systemctl restart fortishield-agent
   
Test the configuration
----------------------

#. Add the following block in the ``<syscheck>`` block of the Fortishield agent ``/var/ossec/etc/ossec.conf`` configuration file and save it:

   .. code-block:: xml

      <directories realtime="yes">/root</directories>

   This addition allows monitoring file changes in the ``/root`` directory of the monitored endpoint. You don’t need to actually add or modify files. It’s just to test the configuration.

   .. warning::

      Incorrect modifications to the Fortishield agent configuration file might cause the service to crash. It’s important to thoroughly review any changes before implementing them in a production environment.

Visualize the alerts
--------------------

You can visualize the alert data on the Fortishield dashboard.

.. thumbnail:: /images/manual/active-response/ar-alert-fired2.png
   :title: Active response alert: The Fortishield agent was restarted
   :alt: Active response alert: The Fortishield agent was restarted
   :align: center
   :width: 80%
