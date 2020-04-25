include .env

install: 
	pip install -r requirements

install_test: install
	pip install -r requirements-test

test:
	python -m pytest

run:
	python abec.py
