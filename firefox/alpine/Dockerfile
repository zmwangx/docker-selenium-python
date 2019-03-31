ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-alpine

RUN apk update && \
    apk add firefox-esr

COPY get-geckodriver.py /tmp
RUN /tmp/get-geckodriver.py

RUN pip install selenium
