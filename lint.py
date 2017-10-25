# -*- coding: utf-8 -*-

"""
Default lint function using some predefined rules.
  - The minimum score to be reached is 9.5.
  - The lint should be run against `module` and `tests` packages.

This script is run as part of `make lint` command.

Pylint is a default dependency for this project, so it can be run
independently if it's wished so.

"""
import sys

from pylint.lint import Run

min_score = 9.5

results = Run(['module', 'tests'], exit=False)
global_note = results.linter.stats['global_note']

if global_note > min_score:
    print('Minimum score reached! min_score = {}'.format(str(min_score)))
else:
    print('Minimum score not reached! min_score = {}'.format(str(min_score)))
    sys.exit(1)
