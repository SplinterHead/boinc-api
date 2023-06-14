.PHONY: fmt
fmt:
	poetry run black src/ tests/
	poetry run isort --profile=black src/ tests/

.PHONY: test
test: fmt
	poetry run pytest -vv -s