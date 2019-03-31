ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-slim-stretch

RUN apt-get -yqq update && \
    apt-get install -yq --no-install-recommends chromium unzip wget

# http://chromedriver.chromium.org/downloads
ENV CHROMEDRIVER_VERSION 2.46
RUN wget --progress=dot:mega -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin

RUN pip install selenium
