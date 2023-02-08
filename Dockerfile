FROM python:3.9-bullseye AS builder

RUN useradd -ms /bin/bash pythonrunner

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    libxml2

USER pythonrunner

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -U --no-cache-dir uwsgi pip setuptools wheel
RUN pip3 install --no-cache-dir --user -r /tmp/requirements.txt


FROM python:3.9-slim-bullseye AS prod-container


RUN useradd -ms /bin/bash pythonrunner

WORKDIR /app
RUN chown -R pythonrunner:pythonrunner /app

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    libxml2 \
    redis-server \
    wget \
    iputils-ping \
    vim


COPY --chown=pythonrunner:pythonrunner --from=builder /home/pythonrunner/.local /usr/local
COPY --chown=pythonrunner:pythonrunner oilstubdata /app


USER pythonrunner

CMD exec systemctl --user enable redis-server.service

CMD exec service redis-server restart & gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 oilstubdata.wsgi:application & celery -A oilstubdata worker -Q celery --loglevel=info
