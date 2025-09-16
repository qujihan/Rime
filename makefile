.PHONY: all

all: dict

dict:
	pip install requests
	cd dicts
	python download.py
	cd -