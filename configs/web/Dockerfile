FROM        python:3.8-slim

ENV         LANG C.UTF-8
ENV         PROJECTPATH=/home/app/project
ENV         USER app

RUN         set -x && apt-get -qq update \
            && apt-get install -y --no-install-recommends \
            libpq-dev python3-dev git \
            && apt-get purge -y --auto-remove\
            && rm -rf /var/lib/apt/lists/*

RUN         useradd -m -d /home/${USER} ${USER} \
            && chown -R ${USER} /home/${USER}

RUN         mkdir -p ${PROJECTPATH}

ADD         https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait ${PROJECTPATH}/wait
RUN         chmod +x ${PROJECTPATH}/wait

RUN         curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
            cd /usr/local/bin && \
            ln -s /opt/poetry/bin/poetry && \
            poetry config virtualenvs.create false

WORKDIR     ${PROJECTPATH}

ADD         poetry.lock ${PROJECTPATH}
ADD         pyproject.toml ${PROJECTPATH}

RUN         poetry install

COPY        ./src/* ${PROJECTPATH}

USER        ${USER}

