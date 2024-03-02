.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The Fortishield-Logtest solution is distributed by different components of the Fortishield environment: core logtest, fortishield RESTful API, and fortishield-logtest tool. 
  
.. _dev-fortishield-logtest:


Fortishield-Logtest
=============

The Fortishield-Logtest solution is distributed by different components of the Fortishield environment:

**Core Logtest**

    The logtest core is part of the :ref:`fortishield-analysisd <fortishield-analysisd>`.

**Fortishield RESTful API**

    Provides Core Logtest remote interface to test rules and decoders.

**fortishield-logtest tool**

     Fortishield-Logtest replacement for ossec-logtest tool.


Fortishield API and :ref:`fortishield-logtest tool <fortishield-logtest>` connect to the fortishield-analysisd session manager, this acts as a
sandbox with the rules engine, allowing to isolate different users with their own rules and decoders.
The below show image illustrations how the user logs test flow through the Fortishield environment.

.. thumbnail:: ../images/development/logtest-flow.png
  :title: Fortishield Logtest
  :align: center
  :width: 100%



Sessions
--------

Fortishield-Logtest is based on the use of isolated sessions, identified with a “token”. Each session stores its own history
of events, rules and decoders loaded. When the log evaluation is requested for the first time, the session manager
creates a new session, processing and returning the result along with the alphanumeric token as identification
of the new session.

Idle session collector
^^^^^^^^^^^^^^^^^^^^^^

The idle session collector, runs every ``session_timeout`` seconds. This parameter is defined in the
:ref:`rule_test <reference_ossec_rule_test>` section of the :ref:`ossec.conf <reference_ossec_conf>` file.
Every time the collector starts, it searches for sessions that have been idle longer than the time specified in
``session_timeout`` to close them.

The following illustration shows how the collector runs on T0, T1, T2 ... At the moment the session generates its
last request, between T0 and T1, its timeout is between T1 and T2, then on T2 the collector closes the session.

.. thumbnail:: ../images/manual/fortishield-logtest/logtest-session-collector.png
  :title: Idle session collector
  :align: center
  :width: 100%



Session lifetime
^^^^^^^^^^^^^^^^

Sessions have a default expiration time of 15 minutes. When a session remains idle with no log processing requests
during that period, the idle session collector closes the session. Requests with an expired session token are
also processed, generate a new session token and notify the user.
