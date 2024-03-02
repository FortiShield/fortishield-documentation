.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: The Fortishield dashboard gives you a quick view of your agents, alerts, and cluster. Learn how to configure its features in this section. 
  
.. _fortishield_dashboard_settings:

Settings
========

The **Settings** module allows you to configure and customize your Fortishield dashboard experience.

API
---

In this section, you can list all your inserted API credentials. The star icon indicates the currently used API to show information on the app. Each entry has multiple available actions to manage it. Keep in mind that a working API is needed to add or edit an entry. Check your API connection status before adding them to the app.

.. thumbnail:: ../../images/kibana-app/features/settings/api.png
  :align: center
  :width: 100%

Configuration
-------------

You can take a quick look at the Fortishield dashboard configuration file here. The documentation for the ``fortishield.yml`` file can be found in the config section.

.. thumbnail:: ../../images/kibana-app/features/settings/configuration.png
  :align: center
  :width: 100%

Logs
----

The Fortishield dashboard stores log information on the ``/usr/share/fortishield-dashboard/data/fortishield/logs/fortishieldapp.log`` file. These logs can be helpful for troubleshooting purposes. 

.. thumbnail:: ../../images/kibana-app/features/settings/logs.png
  :align: center
  :width: 100%

About
-----

This section provides information about your currently installed Fortishield dashboard package, such as version, revision, and installation date. If you want to discover what's new on each release, you can go to our `Changelog file <https://github.com/fortishield/fortishield-dashboard-plugins/blob/master/CHANGELOG.md>`_ to check it out.

.. thumbnail:: ../../images/kibana-app/features/settings/about.png
  :align: center
  :width: 100%
