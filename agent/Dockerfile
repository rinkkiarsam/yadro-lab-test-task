FROM debian:bookworm-slim

RUN apt-get update && \
apt-get install -y --no-install-recommends \
python3 python3-venv python3-pip \
wget unzip curl ca-certificates \
default-jre-headless && \
rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/python -m pip install --upgrade pip setuptools wheel \
    && /opt/venv/bin/pip install --no-cache-dir -r ./requirements.txt

ENV PATH="/opt/venv/bin:${PATH}"

COPY ./tests ./tests

RUN mkdir -p ./allure
RUN wget -O /tmp/allure.deb "https://github.com/allure-framework/allure2/releases/download/2.35.1/allure_2.35.1-1_all.deb" && \
    dpkg -i /tmp/allure.deb

EXPOSE 8080
ENV PATH="/opt/venv/bin:${PATH}"

CMD ["/bin/bash", "-c", "\
pytest tests/ --alluredir=allure-results -v --cache-clear && \
allure generate allure-results -o allure-report --clean && \
allure open allure-report --port 8080"]