====================
Python CommandLineFu
====================

:Author: Olivier Hervieu
:Author Email: olivier.hervieu@gmail.com
:License: MIT License

CommandLineFu is a python class that implements CommandLineFu API and more.
You can :
- browse current commands sorted by dates or votes,
- get commands from a specified user,
- match everythings that contains a search word,
- search commands that contains a search word.

This modules do not required special dependencies (it use only standard python
modules). So it can be used easily on many platforms.
CommandlineFu is compatible with python2 and python3.

This modules can't post new commands on commandlinefu since there is no API to
authenticate users and post new tips and tricks on CommandLineFu.

Changelog
=========

v0.1
----

- Initial release of python-commandlinefu

Todo
====

- Implement a command line utility nammed fu to search, browse and retrieve tips from commandlinefu.com. The syntax could be :

  - fu search 'grep' --limit 20 --sort-by-votes
  - fu match  'grep' --limit 100 --sort-by-dates
  - fu by 'user'
  - fu browse --sort-by-dates --limit 50

- Searching to implement an authentication procedure to authenticate users on commandlinefu.com so, they can post new commands.
