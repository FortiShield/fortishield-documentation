.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The verify-agent-conf program verifies the Fortishield agent.conf configuration. Learn more about it in this section of the Fortishield documentation.

.. _verify-agent-conf:

verify-agent-conf
=================

The **verify-agent-conf** program verifies the Fortishield :ref:`agent.conf <reference_agent_conf>` configuration.

This program searches in ``/var/ossec/etc/shared`` the possible folders belonging to groups and verifies the ``agent.conf`` file
inside them if it exists. We can also specify the path of the file to be verified.

Usage:

.. code-block:: console

      verify-agent-conf [-f <agent.conf file>]
