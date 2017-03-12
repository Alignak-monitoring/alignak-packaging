=================
alignak-scheduler
=================

------------------------
Alignak scheduler daemon
------------------------

:Author:            Alignak Team
:Date:              2015-10-31
:Version:           1.0.0
:Manual section:    8
:Manual group:      Alignak commands


SYNOPSIS
========

  **alignak-scheduler** [-dr] [-c *CONFIGFILE*] [--debugfile *DEBUGFILE*]

DESCRIPTION
===========

Alignak scheduler daemon.

The **alignak-scheduler** manages the dispatching of checks and actions sent to
alignak-reactionner and alignak-poller based on configuration sent to it by alignak-arbiter.

OPTIONS
=======

  -c INI-CONFIG-FILE, --config=INI-CONFIG-FILE  Daemon configuration file
  -d, --daemon                                  Run in daemon mode
  -r, --replace                                 Replace previous running scheduler
  -h, --help                                    Show this help message
  --debugfile=DEBUGFILE                         Enable debug logging to *DEBUGFILE*
  --version                                     Show program's version number