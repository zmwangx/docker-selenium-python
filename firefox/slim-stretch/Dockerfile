ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-slim-stretch

RUN apt-get -yqq update && \
    apt-get install -yq --no-install-recommends firefox-esr 

COPY get-geckodriver.py /tmp
# GITHUB_API_TOKEN is optional and raises API rate limit if specified.
ARG GITHUB_API_TOKEN
RUN GITHUB_API_TOKEN=$GITHUB_API_TOKEN /tmp/get-geckodriver.py

RUN pip install selenium
