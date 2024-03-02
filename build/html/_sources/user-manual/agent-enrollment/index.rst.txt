.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn more about how to register Fortishield agents on Linux, Windows, or macOS X in this section of our documentation.
  
.. _agent_enrollment:

Fortishield agent enrollment
=======================

Agent enrollment is the process of registering Fortishield agents as authorized members of the Fortishield solution. Agent enrollment allows:

- The Fortishield manager to register agents and generate unique keys for them.

- The use of the key to encrypt communication between the agent and the manager.

- Validation of the identity of the agents communicating with the manager.

Please note that, when following our :doc:`Installation guide </installation-guide/index>`, it is recommended to use environment variables to automatically configure the Fortishield agent. This allows the agent to enroll and connect to the Fortishield manager. This documentation provides additional information on the different enrollment options.


Enrollment methods
------------------

There are two options for enrolling agents with the Fortishield manager.      

#. :doc:`Enrollment via agent configuration <via-agent-configuration/index>`: Once the IP address of the manager has been set, the agent will be able to automatically request the key and import it. This is the recommended enrollment method.

#. :doc:`Enrollment via manager API <via-manager-API/index>`: The user requests the key from the manager API and then manually imports it to the agent.

Requirements
------------

The following has to be in place to ensure the Fortishield agent enrollment is done:

#. An installed and running Fortishield manager. 

#. An installed and running Fortishield agent on the endpoint that the user needs to enroll. 

#. Outbound connectivity from the Fortishield agent to the Fortishield manager services. The following ports are configurable:

   - 1514/TCP for agent communication.
   - 1515/TCP for enrollment via automatic agent request.
   - 55000/TCP for enrollment via manager API.


.. note:: You can find instructions to install and enroll agents in the Fortishield dashboard making use of the deployment variables. Go to **Endpoints Summary**, and click on **Deploy new agent**.


Troubleshooting
---------------

Refer to the :doc:`Troubleshooting <../agent-enrollment/troubleshooting>` section for details on how to test the connectivity between the agent and the manager. 


.. toctree::
    :hidden:
    :maxdepth: 1

    via-agent-configuration/index
    via-manager-API/index
    security-options/index
    troubleshooting
    
    
