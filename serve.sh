#!/bin/bash

./build.py
tmux new -s docs -d mkdocs serve
ff http://localhost:8000/
