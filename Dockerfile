FROM python:3.7.7-alpine

WORKDIR /usr/src/mytasks

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN python -m pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

COPY . .