.PHONY: all develop list test

all: list

develop-git:
	pip install -r requirements.git.txt

develop-pypi:
	pip install -r requirements.pypi.txt

list:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

test:
	behave features/datapackage
	behave features/jsontableschema
