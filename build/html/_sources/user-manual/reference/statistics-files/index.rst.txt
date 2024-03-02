.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The statistics files are documents that show real-time information about the Fortishield environment. Learn more about it in this section of the documentation.

.. _reference_statistics_files:

Statistics files
================

The **statistics files** are documents that show real-time information about the Fortishield environment as the processed events, received messages, and the state of the remote connections.

Agents statistical files:

  * :ref:`fortishield-agentd.state <fortishield_agentd_state_file>` - It shows the amount of events generated,
    last connection date and agent status, among other useful information related to the agent.

Manager statistical files:

  * :ref:`fortishield-remoted.state <fortishield_remoted_state_file>` - It shows information
    about the :ref:`remote daemon <fortishield-remoted>`
  * :ref:`fortishield-analysisd.state <fortishield_analysisd_state_file>` - It shows information
    about the :ref:`analysis daemon <fortishield-analysisd>`.

Manager and Agents statistical files:

  * :ref:`fortishield-logcollector.state <fortishield_logcollector_state_file>` - It shows information about :ref:`logcollector daemon <fortishield-logcollector>`.

.. topic:: Contents

  .. toctree::
      :maxdepth: 1

      fortishield-agentd-state
      fortishield-remoted-state
      fortishield-analysisd-state
      fortishield-logcollector-state
