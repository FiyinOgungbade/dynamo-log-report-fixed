# Pinned to an official, secure Python image by its exact SHA256 digest
FROM python:3.11-slim@sha256:8370be8db7576a8bf8e6be0195ee8ec823cf30460367980998f0290196236b2c

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
