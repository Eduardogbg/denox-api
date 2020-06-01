from python:3.8-alpine

WORKDIR /usr/app
COPY . .
# must upgrade because of bug
Run pip install --upgrade setuptools pip
RUN pip install pipenv
RUN pipenv install
