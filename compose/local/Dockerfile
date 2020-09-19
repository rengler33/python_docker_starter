FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

RUN pip install pipenv
# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements

WORKDIR /requirements
RUN pipenv lock --pre
RUN pipenv install --dev --system
