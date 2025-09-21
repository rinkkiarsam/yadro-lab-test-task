FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apache2 \
    openssh-server && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

ARG SSH_USER
ARG SSH_PASSWORD

RUN id "$SSH_USER" >/dev/null 2>&1 || useradd -m -s /bin/bash "$SSH_USER" && \
    echo "${SSH_USER}:${SSH_PASSWORD}" | chpasswd && \
    usermod -aG www-data "$SSH_USER"

COPY ./index/index.html /var/www/html/index.html

RUN chown -R ${SSH_USER} /var/log/apache2

EXPOSE 80 22

CMD service ssh start && apache2ctl -D FOREGROUND