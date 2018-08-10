# python-project-sample
Structure for new Python Projects


## Project 
* [Pipenv](https://github.com/pypa/pipenv) as packaging tool.
* [Make](https://www.gnu.org/software/make/) as task runner.
* [pylint](https://github.com/PyCQA/pylint) as source code analyzer.
* [pytest](https://github.com/pytest-dev/pytest) as testing framework. 
* [pytest-mock](https://github.com/pytest-dev/pytest-mock) - Thin-wrapper around the mock package for easier use with py.test
* [isort](https://github.com/timothycrosley/isort) - A Python utility / library to sort imports. 


## Make tasks

In order to `make` long commands short *(got the pun?)* this project comes up with a list of built-in make tasks:  

It's good practice to read the `Makefile` and understand what each task does, and so it's possible to one improve the task for the one's better using.


#### Task list:

```
$ make

  Usage:

        make <target>

  Targets:

    build         Create wheel from source
    clean         Remove build files
    help          Display this help
    install       Install packages from Pipfile
    isort         Sort imports as PEP8
    lint          Run pylint
    test-cov      Run tests with pytest and coverage
    test          Run tests with pytest
    upload-test   Upload dist content to test.pypi.org
    upload        Upload dist content to pypi.org

```

### First steps with this project

Clone this project:
```
user@machine: ~ git clone https://github.com/jonathadv/python-project-sample.git
user@machine: ~ cd python-project-sample
```

Install the project and dev dependencies:
```
user@machine: ~/python-project-sample (master)$ make install
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

Activate the virtual env:
 ```
user@machine: ~/python-project-sample (master)$ pipenv shell
Spawning environment shell (/bin/bash). Use 'exit' to leave.
source /home/user/.local/share/virtualenvs/python-project-sample-nScfC6eI/bin/activate
user@machine: ~/python-project-sample (master)$ source /home/user/.local/share/virtualenvs/python-project-sample-nScfC6eI/bin/activate
(python-project-sample-nScfC6eI) user@machine: ~/python-project-sample (master)$ 

```
