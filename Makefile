install:
	poetry install

lint:
	poetry run flake8 proxy_server

run:
	poetry run gunicorn --chdir proxy_server app:app