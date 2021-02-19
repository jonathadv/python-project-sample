# python-project-sample
Structure for new Python Projects


## Project 
* [Pipenv](https://github.com/pypa/pipenv) as packaging tool.
* [Make](https://www.gnu.org/software/make/) as task runner.
* [pylint](https://github.com/PyCQA/pylint) as source code analyzer.
* [pytest](https://github.com/pytest-dev/pytest) as testing framework. 
* [pytest-mock](https://github.com/pytest-dev/pytest-mock) - Thin-wrapper around the mock package for easier use with py.test.
* [pytest-cov](https://github.com/pytest-dev/pytest-cov) - This plugin produces coverage reports.
* [pytest-pspec](https://github.com/gowtham-sai/pytest-pspec) - A pspec format reporter for pytest
* [isort](https://github.com/timothycrosley/isort) - A Python utility / library to sort imports. 


## Make tasks

In order to `make` long commands short *(got the pun?)* this project comes up with a list of built-in make tasks:  

It's good a practice to read the `Makefile` and understand what each task does, and so it's possible to one improve the task for the one's better using.


#### Task list

```
$ make

  Usage:

        make <target>

  Targets:

    build         Create wheel from source
    clean         Remove build files
    format        Format with black
    help          Display this help
    install-dev   Install packages and dev packages from Pipfile
    install       Install packages from Pipfile
    isort         Sort imports as PEP8
    lint          Run pylint
    sync          Install packages from Pipfile.lock
    test-cov      Run tests with pytest and coverage
    test          Run tests with pytest
    upload-test   Upload dist content to test.pypi.org
    upload        Upload dist content to pypi.org


```

## Clone this project
```
$ git clone https://github.com/jonathadv/python-project-sample.git
$ cd python-project-sample
```

## Install the project and dev dependencies
```
$ make install-dev

pipenv install --dev
Creating a virtualenv for this project…
⠋Using base prefix '/usr'
New python executable in /home/user/.local/share/virtualenvs/python-project-sample-nScfC6eI/bin/python3
Also creating executable in /home/user/.local/share/virtualenvs/python-project-sample-nScfC6eI/bin/python
Installing setuptools, pip, wheel...done.

Virtualenv location: /home/user/.local/share/virtualenvs/python-project-sample-nScfC6eI
Installing dependencies from Pipfile.lock…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 14/14 — 00:00:07
To activate this project's virtualenv, run the following:
 $ pipenv shell
 ```

## Activate the virtual env
 ```
$ pipenv shell
Spawning environment shell (/bin/bash). Use 'exit' to leave.
source /home/user/.local/share/virtualenvs/python-project-sample-nScfC6eI/bin/activate
$ source /home/user/.local/share/virtualenvs/python-project-sample-nScfC6eI/bin/activate
(python-project-sample-nScfC6eI) $ 

```

## Running formatting, linter, test and coverage 
```bash
$ make format lint test-cov 
pipenv run black my_module tests
All done! ✨ 🍰 ✨
3 files left unchanged.
pipenv run pylint my_module

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

pipenv run pytest --cov-report term-missing --cov=my_module
========================================================================================================== test session starts ===========================================================================================================
platform linux -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: python-project-sample, configfile: pytest.ini
plugins: mock-3.5.1, pspec-0.0.4, cov-2.11.1
collected 3 items                                                                                                                                                                                                                        

tests/test_math_operations.py                                                                                                                                                                                                                                           
math operations
 ✓ it adds two integers and returns integer
 ✓ it adds an integer and a float and returns float
 ✓ It divides an integer by another integer and returns an integer
                                                                                                                                                                                                                                   [100%]

----------- coverage: platform linux, python 3.8.5-final-0 -----------
Name                    Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------
my_module/__init__.py       5      0      0      0   100%
-------------------------------------------------------------------
TOTAL                       5      0      0      0   100%

Required test coverage of 95.0% reached. Total coverage: 100.00%

=========================================================================================================== 3 passed in 0.06s ============================================================================================================
```
