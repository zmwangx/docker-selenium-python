#!/usr/bin/env python3

import json
import os
import tarfile
import urllib.request

req = urllib.request.Request("https://api.github.com/repos/mozilla/geckodriver/releases/latest")
req.add_header("Accept", "application/vnd.github.v3+json")
token = os.getenv("GITHUB_API_TOKEN")
if token:
    req.add_header("Authorization", "token %s" % token)
with urllib.request.urlopen(req) as r:
    status = r.getcode()
    assert status == 200, "api.github.com: HTTP %d" % status
    for asset in json.loads(r.read().decode("utf-8"))["assets"]:
        asset_url = asset["browser_download_url"]
        if "linux64" in asset_url:
            break
    else:
        raise ValueError("linux64 download not found in latest release of mozilla/geckodriver")

tarball, _ = urllib.request.urlretrieve(asset_url)
with tarfile.open(tarball) as tf:
    tf.extract("geckodriver", path="/usr/local/bin")
os.unlink(tarball)
