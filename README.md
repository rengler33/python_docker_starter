# python_docker_starter

A basic configuration for doing _Docker container development_ and deployment. A lot of the basic structure is inspiration from [sourcery-ai python best practices cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter).

This will eventually be turned into a cookiecutter template but it's not there yet.

This project has a .devcontainer folder which is designed to allow development completely inside a Docker container through VS Code. Note that it also has a .vscode folder for settings. It's not necessary to develop using VS code even for the container setup but it's pretty nifty.

## Project Setup with container developement

### Option A: Use VS Code
Install "remote development" pack and use remote containers extension to build and enter the container. This will use items inside the `.devcontainer/` folder and install some extensions I find useful.

### Option B: Use terminal
Spin up a container using an infinite wait command, give it a name of "appy"
```sh
 docker-compose -f local.yml run --name appy -d py /bin/sh -c "while sleep 1000; do :; done"
 ```
 
 Enter the container "appy" using
 ```sh
 docker exec -it appy /bin/bash
 ```
 
 Stop the container "appy" using
 ```sh
 docker-compose -f local.yml down
 ```

## Project Setup with **no** container development

Development does not have to be done inside the container. A project setup (after cookiecutter is finished) would look like:

### Install dependencies

```sh
pip install pipenv
pipenv install --dev
```

### Setup pre-commit hooks

```sh
pipenv run pre-commit install -t pre-commit
```
