#!/bin/sh

set -ex

pip install -r requirements.txt

export PYTHONPATH=library

mkdocs build

cp redirects.txt site/_redirects
