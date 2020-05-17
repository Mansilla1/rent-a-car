FROM python:3.7-buster as base

ENV PYTHONUNBUFFERED 1
WORKDIR /api
# System deps:
RUN apt-get update
RUN apt-get install openssl
RUN apt-get install -y\
    build-essential \
    postgresql-client \
    libpq-dev

# App deps
ADD requirements.txt .
RUN pip install -r requirements.txt
