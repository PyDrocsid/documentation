#!/bin/sh

set -ex

pip install -r requirements.txt

python build.py
mkdocs build
