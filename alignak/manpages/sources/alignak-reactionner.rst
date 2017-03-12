===================
alignak-reactionner
===================

--------------------------
Alignak reactionner daemon
--------------------------

:Author:            Alignak Team
:Date:              2015-10-31
:Version:           1.0.0
:Manual section:    8
:Manual group:      Alignak commands


SYNOPSIS
========

  **alignak-reactionner** [-dr] [-c *CONFIGFILE*] [--debugfile *DEBUGFILE*]

DESCRIPTION
===========

Alignak reactionner daemon.

The **alignak-reactionner** is similar to alignak-poller but handles actions such as
notifications and event-handlers from the schedulers rather than checks.

OPTIONS
=======

  -c INI-CONFIG-FILE, --config=INI-CONFIG-FILE  Daemon configuration file
  -d, --daemon                                  Run in daemon mode
  -r, --replace                                 Replace previous running reactionner
  -h, --help                                    Show this help message
  --debugfile=DEBUGFILE                         Enable debug logging to *DEBUGFILE*
  --version                                     Show program's version number