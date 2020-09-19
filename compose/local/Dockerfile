FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

RUN pip install pipenv
# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements

# Set environment variable to tell pipenv where pipfile is location
RUN set -e PIPENV_PIPFILE /requirements
RUN pipenv lock
RUN pipenv install --dev --system
