===============
alignak-arbiter
===============

----------------------
Alignak arbiter daemon
----------------------

:Author:            Alignak Team
:Date:              2015-10-31
:Version:           1.0.0
:Manual section:    8
:Manual group:      Alignak commands


SYNOPSIS
========

  **alignak-arbiter** [-dr] [-c *INI-CONFIG-FILE*] [-a *CONFIG-FILE*] [--debugfile *DEBUGFILE*]
  **alignak-arbiter** -V [-c *INI-CONFIG-FILE*] [-a *CONFIG-FILE*]

DESCRIPTION
===========

Alignak arbiter daemon

The **alignak-arbiter** daemon reads the configuration, divides it into parts
(N schedulers = N parts), and distributes the configuration to the appropriate
Alignak daemons.
Additionally, it manages the high availability features: if a particular daemon dies,
it re-routes the configuration managed by this failed  daemon to the configured spare.
There can only be one active arbiter in the architecture.


OPTIONS
=======

  -V, --verify-config                           Verify monitoring configuration file and exit
  -a CONFIGFILE, --arbiter=CONFIGFILE           Monitored objects configuration file (eg. nagios.cfg). Multiple -a can be used, it will be like if all files was just one
  -c INI-CONFIG-FILE, --config=INI-CONFIG-FILE  Daemon configuration file
  -d, --daemon                                  Run in daemon mode
  -r, --replace                                 Replace previous running arbiter
  -h, --help                                    Show this help message
  --debugfile=DEBUGFILE                         Enable debug logging to *DEBUGFILE*
  --version                                     Show program's version number