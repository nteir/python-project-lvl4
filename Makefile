runserver:
	poetry run python manage.py runserver

makemessages:
	poetry run django-admin makemessages -l ru

compilemessages:
	poetry run django-admin compilemessages

requirements:
	poetry export -f requirements.txt -o requirements.txt

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

test-cov: 
	poetry run coverage run manage.py test
	poetry run coverage xml

.PHONY: runserver makemessages requirements lint test test-cov