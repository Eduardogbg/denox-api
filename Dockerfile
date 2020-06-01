from python:3.8-alpine

WORKDIR /usr/app
COPY . .
RUN pip install pipenv
RUN pipenv install
