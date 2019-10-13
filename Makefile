.PHONY: all install list test version


MAINTAINER := $(shell head -n 1 MAINTAINER.md)


all: list

install:
	pip install --upgrade -r requirements.txt

list:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

readme:
	pip install md-toc
	md_toc -p README.md github --header-levels 3
	sed -i '/(#testsuite-extended)/,+1d' README.md

templates:
	sed -i -E "s/@(\w*)/@$(MAINTAINER)/" .github/issue_template.md
	sed -i -E "s/@(\w*)/@$(MAINTAINER)/" .github/pull_request_template.md

test:
	pytest

version:
	pip list
