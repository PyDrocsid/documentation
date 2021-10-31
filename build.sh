#!/bin/sh

pip install -r requirements.txt

python build.py
mkdocs build
