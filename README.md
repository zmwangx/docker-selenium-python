# docker-selenium-python

This repository provides images with Python 3, the `selenium` package, as well as the Chromium/chromedriver combo or the Firefox/geckodriver combo preinstalled.

```sh
docker pull zmwangx/docker-selenium-python:$TAG
```

where tags are based on Python version, browser, and base image:

```
REPOSITORY                       TAG
zmwangx/docker-selenium-python   python-3.7-firefox-alpine
zmwangx/docker-selenium-python   python-3.6-firefox-alpine
zmwangx/docker-selenium-python   python-3.5-firefox-alpine
zmwangx/docker-selenium-python   python-3.7-firefox-slim-stretch
zmwangx/docker-selenium-python   python-3.6-firefox-slim-stretch
zmwangx/docker-selenium-python   python-3.5-firefox-slim-stretch
zmwangx/docker-selenium-python   python-3.7-chromium-alpine
zmwangx/docker-selenium-python   python-3.6-chromium-alpine
zmwangx/docker-selenium-python   python-3.5-chromium-alpine
zmwangx/docker-selenium-python   python-3.7-chromium-slim-stretch
zmwangx/docker-selenium-python   python-3.6-chromium-slim-stretch
zmwangx/docker-selenium-python   python-3.5-chromium-slim-stretch
```

## Development

Run

```
./build
```

to build all images.

`CHROMEDRIVER_VERSION` in `chromium/slim-stretch/Dockerfile` may need manual update to suit the Chromium version being installed.
