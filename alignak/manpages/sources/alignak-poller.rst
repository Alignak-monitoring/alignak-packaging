==============
alignak-poller
==============

---------------------
Alignak poller daemon
---------------------

:Author:            Alignak Team
:Date:              2015-10-31
:Version:           1.0.0
:Manual section:    8
:Manual group:      Alignak commands


SYNOPSIS
========

  **alignak-poller** [-dr] [-c *CONFIGFILE*] [--debugfile *DEBUGFILE*]

DESCRIPTION
===========

Alignak poller daemon.

The **alignak-poller** daemon is in charge of launching plugins as requested by schedulers.
When the check is finished it returns the result to the schedulers.

OPTIONS
=======

  -c INI-CONFIG-FILE, --config=INI-CONFIG-FILE  Daemon configuration file
  -d, --daemon                                  Run in daemon mode
  -r, --replace                                 Replace previous running poller
  -h, --help                                    Show this help message
  --debugfile=DEBUGFILE                         Enable debug logging to *DEBUGFILE*
  --version                                     Show program's version number