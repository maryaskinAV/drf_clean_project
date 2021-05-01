FROM        python:3.8-slim

ENV         LANG C.UTF-8
ENV         PROJECTPATH=/home/app/
ENV         USER app

RUN         set -x \
            && apt-get -qq update \
            && apt-get install -yq libpq-dev python3-dev gcc git curl \
            && apt-get purge -y --auto-remove \
            && rm -rf /var/lib/apt/lists/*

RUN         useradd -m -d /home/${USER} ${USER} \
            && chown -R ${USER} /home/${USER}

RUN         mkdir -p ${PROJECTPATH} \
            && mkdir -p /home/{USER}/media \
            && mkdir -p /home/{USER}/static

ADD         . ${PROJECTPATH}

RUN         pip install --no-cache-dir -r ${PROJECTPATH}/requirements.txt

ADD         https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait ${PROJECTPATH}/wait
RUN         chmod +x ${PROJECTPATH}/wait

WORKDIR     ${PROJECTPATH}
USER        ${user}