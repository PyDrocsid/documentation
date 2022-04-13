#!/bin/bash

tmux new -s docs -d mkdocs serve
ff http://localhost:8000/
