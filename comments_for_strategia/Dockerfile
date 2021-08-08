FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN pip install pipenv

COPY . /comments-api
WORKDIR /comments-api

RUN pipenv install --dev --deploy --system
