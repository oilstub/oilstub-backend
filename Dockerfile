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
    wget \
    iputils-ping \
    vim


COPY --chown=pythonrunner:pythonrunner --from=builder /home/pythonrunner/.local /usr/local
COPY --chown=pythonrunner:pythonrunner oilstubdata /app/

RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
RUN chmod +x cloud_sql_proxy
CMD ["sh", "-c", "./cloud_sql_proxy -instances=oilstub-backend1:us-south1:oilstub-db=tcp:0.0.0.0:5432"]
USER pythonrunner

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 oilstubdata.wsgi:application

FROM builder As dev-container

USER root

COPY requirements.txt /tmp/requirements.txt
RUN cp -r /home/pythonrunner/.local/* /usr/local

WORKDIR /app/oilstubdata
USER pythonrunner

CMD ["bash"]

