run-unit-tests:
	python -m pytest -k "not integration"

run-integration-tests:
	python -m pytest -k "not unit"

run-all-tests:
	python -m pytest --cov=src --cov-report term-missing

run-local-server:
	python app.py