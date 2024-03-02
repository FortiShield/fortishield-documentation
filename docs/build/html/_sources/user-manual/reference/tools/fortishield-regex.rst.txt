.. Copyright (C) 2015, Fortishield, Inc.

.. meta::
  :description: Learn more about the fortishield-regex tool in this section of the Fortishield documentation.

.. _fortishield-regex:

fortishield-regex
===========

The fortishield-regex program is used to validate a regex expression.

The pattern should be enclosed in single quotes to help prevent any unintended interactions with the shell.

The syntax for fortishield-regex is as follows:

``/var/ossec/bin/fortishield-regex '<pattern>'``

It then reads strings from stdin and outputs matches to stdout.

``+OSRegex_Execute`` and ``+OS_Regex`` are displayed if a match is successful.
