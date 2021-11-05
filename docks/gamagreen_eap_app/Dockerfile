FROM python:3.9.6


RUN mkdir /opt/gamagreen-eap-py

COPY . /opt/gamagreen-eap-py

WORKDIR /opt/gamagreen-eap-py/src

RUN pip install --upgrade pip setuptools

RUN pip install --no-cache-dir -r ../requirements.txt

ENV FLASK_ENV development

ENV FLASK_DEBUG 1

EXPOSE 8080