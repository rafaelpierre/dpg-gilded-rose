CMD:=poetry run
PYMODULE:=gilded_rose
TESTS:=tests

lint:
	$(CMD) flake8 $(PYMODULE) $(TESTS) $(EXTRACODE)

test:
	$(CMD) pytest $(TESTS)

coverage:
	$(CMD) coverage run -m pytest && poetry run coverage report -m

black-check:
	black --check --diff .

black-fix:
	black .