FROM python:3.9-slim-buster

RUN apt-get update; \
	apt-get install -y --no-install-recommends;

COPY requirements.txt /

RUN pip3 install --upgrade pip; \
    pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000