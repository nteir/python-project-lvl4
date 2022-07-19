Task Manager
------------

### Hexlet tests and linter status:
[![Actions Status](https://github.com/nteir/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/nteir/python-project-lvl4/actions)
[![CI](https://github.com/nteir/python-project-lvl4/actions/workflows/ci_actions.yml/badge.svg)](https://github.com/nteir/python-project-lvl4/actions/workflows/ci_actions.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/018b6a00f26aade1e507/maintainability)](https://codeclimate.com/github/nteir/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/018b6a00f26aade1e507/test_coverage)](https://codeclimate.com/github/nteir/python-project-lvl4/test_coverage)

[Live on Heroku](https://taskmanager-nteir.herokuapp.com/)

Task manager web project, 4th project in the Hexlet Python learning course.

Features user database, creating, filtering and editing tasks, custom task statuses and tags.

Local installation via [Poetry](https://python-poetry.org/):
* clone the repository
* change directory to python-project-lvl4
* run the following commands in shell:
```
poetry install
make migrate
make runserver
```
This project is using environment variables for secrets:
SECRET_KEY for Django secret key,
ROLLBAR_TOKEN for [Rollbar](https://rollbar.com/) post_server_item token (exceptions tracking).
To provide them locally, make a file .env in python-project-lvl4 directory (see [python-dotenv](https://pypi.org/project/python-dotenv/) documentation for details).
