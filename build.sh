#!/bin/sh

set -ex

pip install -r requirements.txt

mkdocs build

cp redirects.txt site/_redirects
