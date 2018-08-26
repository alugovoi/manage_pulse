manage_pulse
============


CLI script to manage different aspects of pulse inputs,sinks. Can be used during docking/undocking and for volume inc/dec.


Preparing for Development
-------------------------


1. Install ``pip`` and ``pipenv``
2. Clone repository: ``git clone git@github.com:/alugovoi/pulse``
3. ``Make install``


Usage
-----

Increase volume by 10%:

::
manage_pulse --inc 0.1


Undock laptop:

::
manage_pulse --undock



Running tests
-------------



Run tests locally using ``make`` in active venv:

::

   $ make
