.PHONY: all install list test version

all: list

install:
	pip install --upgrade -r requirements.txt

list:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

test:
	pytest

version:
	pip list
