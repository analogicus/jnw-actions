#!/usr/bin/env python3
import yaml

print("Fixing base url")

with open("docs/_config.yml") as fi:
    conf = yaml.safe_load(fi)

with open("info.yaml") as fi:
    info = yaml.safe_load(fi)

if("baseurl" in info):
    conf["baseurl"] = info["baseurl"]

with open("docs/_config.yml","w") as fo:
    fo.write(yaml.dump(conf))
