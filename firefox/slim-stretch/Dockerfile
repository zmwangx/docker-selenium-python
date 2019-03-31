ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-slim-stretch

RUN apt-get -yqq update && \
    apt-get install -yq --no-install-recommends firefox-esr

COPY get-geckodriver.py /tmp
RUN /tmp/get-geckodriver.py

RUN pip install selenium
