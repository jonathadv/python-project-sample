# python-project-sample
Structure for new Python Projects


## Project 
* [Pipenv](https://github.com/pypa/pipenv) as packaging tool.
* [Make](https://www.gnu.org/software/make/) as task runner.
* [pylint](https://github.com/PyCQA/pylint) as source code analyzer.
* [pytest](https://github.com/pytest-dev/pytest) as testing ramework. 
* [pytest-mock](https://github.com/pytest-dev/pytest-mock) - Thin-wrapper around the mock package for easier use with py.test
* [isort](https://github.com/timothycrosley/isort) - A Python utility / library to sort imports. 


## Make tasks

In order to `make` long commands short *(got the pun?)* this project comes up with a list of built-in make taks:  

It's good practice to read the `Makefile` and understand what each task does, and so it's possible to one improve the task for the one's better using.


#### Current task list:

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