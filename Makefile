install:
	poetry install

lint:
	poetry run flake8 proxy_server

run:
	poetry run gunicorn proxy.app:app --config gunicorn.conf.py

test:
	poetry run pytest -vv

coverage:
	poetry run pytest tests/* --cov=proxy_server --cov-report xml

local-coverage:
	poetry run pytest tests/* --cov=proxy_server