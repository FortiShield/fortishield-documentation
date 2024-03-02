.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The Fortishield dashboard includes a configuration file where you can define custom values for several options. Learn more about it in this section.

.. _fortishield_dashboard_config_file:

Configuration file
==================

The Fortishield dashboard includes a configuration file located at ``/usr/share/fortishield-dashboard/data/fortishield/config/fortishield.yml`` where you can define custom values for several options. This section describes all the settings available in this file.

If you are using the Fortishield Kibana plugin, you can find this configuration file at ``/usr/share/kibana/data/fortishield/config/fortishield.yml``. 

The configuration file shows the default values for all of the possible options. You can edit the file, uncomment any of them and apply the desired values. You can also edit these settings from the Fortishield dashboard in **Indexer/dashboard management** > **App Settings**.

The configuration file reference is organized by sections:

.. contents::
   :local:
   :depth: 2
   :backlinks: none

General options
---------------

hosts
^^^^^

Defines the list of APIs to connect with your Fortishield managers.

.. code-block:: yaml

    hosts:
        - <id>:
            url: http(s)://<url>
            port: <port>
            username: <username>
            password: <password>

.. note::

    It is required to specify at least one host.

This is an example of a multi-host configuration:

.. code-block:: yaml

    hosts:
        - fortishield_prod:
            url: https://fortishield.github.io
            port: 55000
            username: fortishield-wui
            password: secret_password
            run_as: false
        - fortishield_test:
            url: https://localhost
            port: 55000
            username: fortishield-wui
            password: fortishield-wui
            run_as: false


pattern
^^^^^^^

Default index pattern to use on the app. If there are no valid index patterns on Elasticsearch, the app will automatically create one with the name indicated in this option.

+--------------------+-------------------------+
| **Default value**  | fortishield-alerts-*          |
+--------------------+-------------------------+
| **Allowed values** | Any valid index pattern |
+--------------------+-------------------------+

timeout
^^^^^^^

Defines the maximum time the app will wait for an API response when making requests to it. It will be ignored if the value is set under 1500 milliseconds.

+--------------------+-------------------------------+
| **Default value**  | 20000 (milliseconds)          |
+--------------------+-------------------------------+
| **Allowed values** | Any number starting from 1500 |
+--------------------+-------------------------------+

ip.selector
^^^^^^^^^^^

Defines if the user is allowed to change the selected index pattern directly from the top menu bar.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

ip.ignore
^^^^^^^^^

Disable certain index pattern names from being available in the index pattern selector from the Fortishield dashboard. An empty list (the default value) won't ignore any valid index pattern.

+--------------------+---------------------------------------------+
| **Default value**  | []                                          |
+--------------------+---------------------------------------------+
| **Allowed values** | Array of strings. Eg: ["fortishield-archives-\*"] |
+--------------------+---------------------------------------------+

logs.level
^^^^^^^^^^

Set the logging level for the Fortishield dashboard log files.

+--------------------+------------+
| **Default value**  | info       |
+--------------------+------------+
| **Allowed values** | info,debug |
+--------------------+------------+

hideManagerAlerts
^^^^^^^^^^^^^^^^^

Hide the manager alerts in the dashboard visualizations.

+--------------------+------------+
| **Default value**  | false      |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

Monitoring
----------

.. _fortishield_monitoring_enabled:

fortishield.monitoring.enabled
^^^^^^^^^^^^^^^^^^^^^^^^

Enable or disable the ``fortishield-monitoring`` index creation and/or visualization:

- When the value is set to ``true``, the app will show the *Agents status* visualization and will insert monitoring-related data.
- When the value is set to ``false``, the app won't show the visualization and won't insert monitoring-related data.
- When the value is set to ``worker``, the app will show the visualization, but won't insert monitoring-related data.

+--------------------+-------------------+
| **Default value**  | true              |
+--------------------+-------------------+
| **Allowed values** | true,false,worker |
+--------------------+-------------------+

.. warning::

    The Fortishield dashboard user interface allows selecting ``true`` and ``false`` only. To set the ``worker`` value, you must edit the configuration file instead.

.. _fortishield_monitoring_frequency:

fortishield.monitoring.frequency
^^^^^^^^^^^^^^^^^^^^^^^^^^

Define in seconds the frequency of API requests to get the state of the agents to create a new document in the `fortishield-monitoring` index with this data.

+--------------------+-----------------------------+
| **Default value**  | 900 (seconds)               |
+--------------------+-----------------------------+
| **Allowed values** | Any number starting from 60 |
+--------------------+-----------------------------+

.. warning::

    Although the minimum value can be ``60``, we recommend adjusting it to at least ``300`` seconds to avoid overloading issues due to the excessive creation of documents into the index.

fortishield.monitoring.pattern
^^^^^^^^^^^^^^^^^^^^^^^^

Default Fortishield monitoring index pattern to use for the app. This setting does not remove any existing patterns or templates, it just updates the app to add new ones.

+--------------------+-------------------------+
| **Default value**  | fortishield-monitoring-*      |
+--------------------+-------------------------+
| **Allowed values** | Any valid index pattern |
+--------------------+-------------------------+

.. _fortishield_monitoring_creation:

fortishield.monitoring.creation
^^^^^^^^^^^^^^^^^^^^^^^^^

Configure fortishield-monitoring-* indices custom creation interval.

+--------------------+------------------------------------------------+
| **Default value**  | w (weekly)                                     |
+--------------------+------------------------------------------------+
| **Allowed values** | h (hourly), d (daily), w (weekly), m (monthly) |
+--------------------+------------------------------------------------+

Health checks
-------------

checks.pattern
^^^^^^^^^^^^^^

Enable or disable the index pattern health check when opening the app.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

checks.template
^^^^^^^^^^^^^^^

Enable or disable the template health check when opening the app.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

checks.api
^^^^^^^^^^

Enable or disable the Fortishield API health check when opening the app.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

checks.setup
^^^^^^^^^^^^

Enable or disable the setup health check when opening the app.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

checks.fields
^^^^^^^^^^^^^

Enable or disable the known fields health check when opening the app.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

checks.metaFields
^^^^^^^^^^^^^^^^^

Enable or disable the metaFields health check when opening the app.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

checks.timeFilter
^^^^^^^^^^^^^^^^^

Enable or disable the timeFilter health check when opening the app.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

checks.maxBuckets
^^^^^^^^^^^^^^^^^

Enable or disable the maxBuckets health check when opening the app.

+--------------------+------------+
| **Default value**  | true       |
+--------------------+------------+
| **Allowed values** | true,false |
+--------------------+------------+

Advanced index options
----------------------

.. warning::

    These options are only valid if they're modified before starting the Fortishield dashboard for the very first time.

    You can read more about configuring the shards and replicas in :doc:`/user-manual/fortishield-indexer/fortishield-indexer-tuning`.


fortishield.monitoring.shards
^^^^^^^^^^^^^^^^^^^^^^^

Define the number of shards to use for the ``fortishield-monitoring-*`` indices.

+--------------------+----------------------------+
| **Default value**  | 1                          |
+--------------------+----------------------------+
| **Allowed values** | Any number starting from 1 |
+--------------------+----------------------------+

fortishield.monitoring.replicas
^^^^^^^^^^^^^^^^^^^^^^^^^

Define the number of replicas to use for the ``fortishield-monitoring-*`` indices.

+--------------------+----------------------------+
| **Default value**  | 0                          |
+--------------------+----------------------------+
| **Allowed values** | Any number starting from 0 |
+--------------------+----------------------------+

Sample alerts
-------------

alerts.sample.prefix
^^^^^^^^^^^^^^^^^^^^

Define the index name prefix of sample alerts. It must match the template used by the index pattern to avoid unknown fields in dashboards.

+--------------------+----------------------------+
| **Default value**  | fortishield-alerts-4.x-          |
+--------------------+----------------------------+
| **Allowed values** | Any valid index pattern    |
+--------------------+----------------------------+

Enrollment DNS
--------------

enrollment.dns
^^^^^^^^^^^^^^

Specifies the Fortishield registration server, used for the agent enrollment.

+--------------------+----------------------------+
| **Default value**  | ''                         |
+--------------------+----------------------------+
| **Allowed values** | Any string                 |
+--------------------+----------------------------+

enrollment.password
^^^^^^^^^^^^^^^^^^^

Specifies the password used to authenticate during the agent enrollment.

+--------------------+----------------------------+
| **Default value**  | ''                         |
+--------------------+----------------------------+
| **Allowed values** | Any string                 |
+--------------------+----------------------------+

Cron
----

cron.prefix
^^^^^^^^^^^

Define the index prefix of predefined jobs.

+--------------------+----------------------------+
| **Default value**  | ''                         |
+--------------------+----------------------------+
| **Allowed values** | Any string                 |
+--------------------+----------------------------+

cron.statistics.status
^^^^^^^^^^^^^^^^^^^^^^

Enable or disable the statistics tasks.

+--------------------+----------------------------+
| **Default value**  | true                       |
+--------------------+----------------------------+
| **Allowed values** | true,false                 |
+--------------------+----------------------------+

cron.statistics.apis
^^^^^^^^^^^^^^^^^^^^

Enter the ID of the hosts you want to save data from, and leave this empty to run the task on every host.

+--------------------+----------------------------+
| **Default value**  | []                         |
+--------------------+----------------------------+
| **Allowed values** | Array of APIs              |
+--------------------+----------------------------+

.. _cron_statistics_interval:

cron.statistics.interval
^^^^^^^^^^^^^^^^^^^^^^^^

Define the frequency of task execution using cron schedule expressions.

+--------------------+----------------------------+
| **Default value**  | ``0 */5 * * * *``          |
+--------------------+----------------------------+
| **Allowed values** | Any cron expressions       |
+--------------------+----------------------------+

cron.statistics.index.name
^^^^^^^^^^^^^^^^^^^^^^^^^^

Define the name of the index in which the documents will be saved.

+--------------------+----------------------------+
| **Default value**  | statistics                 |
+--------------------+----------------------------+
| **Allowed values** | Any valid index pattern    |
+--------------------+----------------------------+

.. _cron_statistics_index_creation:

cron.statistics.index.creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define the interval in which a new index will be created.

+--------------------+-------------------------------------------------+
| **Default value**  | w                                               |
+--------------------+-------------------------------------------------+
| **Allowed values** | h (hourly), d (daily), w (weekly), m (monthly)  |
+--------------------+-------------------------------------------------+

cron.statistics.shards
^^^^^^^^^^^^^^^^^^^^^^

Define the number of shards to use for the statistics indices.

+--------------------+----------------------------+
| **Default value**  | 1                          |
+--------------------+----------------------------+
| **Allowed values** | Any number starting from 1 |
+--------------------+----------------------------+

cron.statistics.replicas
^^^^^^^^^^^^^^^^^^^^^^^^

Define the number of replicas to use for the statistics indices.

+--------------------+----------------------------+
| **Default value**  | 0                          |
+--------------------+----------------------------+
| **Allowed values** | Any number starting from 0 |
+--------------------+----------------------------+

Custom branding
---------------

Edit the settings shown below to use custom branding elements such as logos, and header and footer text.

.. warning::

    Please, take into consideration the following notes: 
        - The value of any  ``customization.logo.*`` setting must follow the pattern ``custom/images/<setting_name>.<image_format>``.
        - The path ``custom/images/`` included in every ``customization.logo.*`` setting is relative to the ``/plugins/fortishield/public/assets/`` folder.
        - Setting or modifying any ``customization.logo.*`` setting by hand is not recommended. Use the UI instead.
        - The in-file ``customization.logo.*`` settings are flagged for deprecation, and will be no longer supported in future releases.

customization.enabled
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable or disable the custom branding.

+--------------------+----------------------------+
| **Default value**  | true                       |
+--------------------+----------------------------+
| **Allowed values** | true,false                 |
+--------------------+----------------------------+

customization.logo.app
^^^^^^^^^^^^^^^^^^^^^^

Define the image's path, name and extension for the main menu logo.

+--------------------+----------------------------+
| **Default value**  | ''                         |
+--------------------+----------------------------+
| **Allowed values** | Any string                 |
+--------------------+----------------------------+

customization.logo.healthcheck
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define the image's path, name and extension for the Healthcheck logo.

+--------------------+----------------------------+
| **Default value**  | ''                         |
+--------------------+----------------------------+
| **Allowed values** | Any string                 |
+--------------------+----------------------------+

customization.logo.reports
^^^^^^^^^^^^^^^^^^^^^^^^^^

Define the image's path, name and extension for the logo to use in the PDF reports generated by the app.

+--------------------+----------------------------+
| **Default value**  |''                          |
+--------------------+----------------------------+
| **Allowed values** | Any string                 |
+--------------------+----------------------------+

customization.reports.header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the header of the PDF reports. To use an empty header, type a space " " in the field. If this field is empty, it uses the default header.

+--------------------+----------------------------+
| **Default value**  |''                          |
+--------------------+----------------------------+
| **Allowed values** | Any string                 |
+--------------------+----------------------------+

customization.reports.footer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the footer of the PDF reports. To use an empty footer, type a space " " in the field. If this field is empty, it uses the default footer.

+--------------------+----------------------------+
| **Default value**  |''                          |
+--------------------+----------------------------+
| **Allowed values** | Any string                 |
+--------------------+----------------------------+


Example
-------

This is an example of the fortishield.yml configuration:

.. code-block:: yaml
    
    # General options
    hosts:
        - env-1:
            url: https://env-1.example
            port: 55000
            username: fortishield-wui
            password: fortishield-wui
            run_as: true
        - env-2:
            url: https://env-2.example
            port: 55000
            username: fortishield-wui
            password: fortishield-wui
            run_as: true
    pattern: 'fortishield-alerts-*'
    timeout: 20000
    ip.selector: true
    ip.ignore: []
    logs.level: info
    hideManagerAlerts: true

    # Monitoring
    fortishield.monitoring.enabled: true
    fortishield.monitoring.frequency: 900
    fortishield.monitoring.pattern: fortishield-monitoring-*
    fortishield.monitoring.creation: w

    # Health checks
    checks.pattern : true
    checks.template: true
    checks.fields  : true
    checks.api     : true
    checks.setup   : true
    checks.metaFields: true
    checks.timeFilter: true
    checks.maxBuckets: true

    #Advanced index options
    fortishield.monitoring.shards: 1
    fortishield.monitoring.replicas: 0    

    # Custom branding
    customization.enabled: true
    customization.logo.app: 'custom/images/customization.logo.app.jpg'
    customization.logo.healthcheck: 'custom/images/customization.logo.healthcheck.svg'
    customization.logo.reports: 'custom/images/customization.logo.reports.jpg'
    customization.reports.footer: '123 Custom footer Ave.\nSan Jose, CA 95148'
    customization.reports.header: 'Custom Company\ninfo@custom.com\n@social_reference'

    #Sample alerts
    alerts.sample.prefix: fortishield-alerts-4.x-

    # Cron
    cron.prefix: fortishield
    cron.statistics.status: true
    cron.statistics.apis: []
    cron.statistics.interval: 0 */5 * * * *
    cron.statistics.index.name: statistics
    cron.statistics.index.creation: w
    cron.statistics.shards: 1
    cron.statistics.replicas: 0

    # Enrollment DNS
    enrollment.dns: ''
    enrollment.password: ''
