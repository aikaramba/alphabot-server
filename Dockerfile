FROM python:2.7.13
MAINTAINER Aikaramba

WORKDIR /usr/
COPY . /usr/

RUN pip install flask
RUN pip install RPi.GPIO

CMD python server.py

EXPOSE 5000
