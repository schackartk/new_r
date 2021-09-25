.PHONY: test install

test:
	python3 -m pytest -xv --flake8 --pylint