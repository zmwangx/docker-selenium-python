ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-alpine

RUN apk update && \
    apk add chromium chromium-chromedriver 

RUN pip install selenium
