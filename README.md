# python-flask

## Running locally

### One-time setup

1. Make sure you're using Python 3.6+
1. Create your virtual environment: `python3 -m venv ./env`
1. Activate your virtual environment: `source ./env/bin/activate`
1. Install all necessary dependencies: `pip install -r requirements.txt`

### Each time you want to run locally

1. Make sure your virtual environment is active: `which python` should be a path to the virtual
   environment you set up in the one-time setup. If your virtual environment is not active, run
   `source ./env/bin/activate` to activate it.
1. Start the server: `flask run`
1. Check that the server is running: `curl localhost:5000/hello`

## Running with Docker

I assume that you've gotten [docker-compose](https://docs.docker.com/compose/install/) set up on your
machine.

1. Launch with docker-compose: `docker-compose up`
1. Check that the server is running: `curl localhost:5000/hello`

## High-level overview

You can see all of the important files in this project by running `tree -a -I env -I .git`

## Configuration

* [Dockerfile](https://docs.docker.com/engine/reference/builder/): tells Docker how to build our
  docker image
* [docker-compose.yml](https://docs.docker.com/compose/compose-file/#service-configuration-reference):
  tells docker-compose how to launch our docker container running that image
* [.flaskenv](http://flask.pocoo.org/docs/dev/cli/#environment-variables-from-dotenv): Flask-specific
  configuration
* [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files): tells `pip` which
  dependencies to install when we launch the docker container

## Making changes

### Changing docker-compose.yml or .flaskenv

1. Save your changes
1. Kill the docker-compose process (either ^C or via `docker-compose down` from another tab)
1. `docker-compose up`

### Changing Dockerfile or requirements.txt

1. Save your changes
1. Kill the docker-compose process (either ^C or via `docker-compose down` from another tab)
1. `docker-compose up --build` (you must rebuild the Docker image for these changes)

### Changing code files

1. Save your changes
1. Refresh your browser

That's it: the Flask server is running in development mode (set in .flaskenv) and this directory is
bind-mounted into the Docker container (set in docker-compose.yml), so any changes you make to the
code should immediately be reflected on the server when you refresh.

## Debugging

You can launch an interactive Python shell with access to your Flask object by using the
[flask shell](http://flask.pocoo.org/docs/1.0/shell/): `docker-compose exec web flask shell`
