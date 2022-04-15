#!/bin/bash

if [[ -z "$VIRTUAL_ENV" ]]; then
    if ! [[ -e .venv ]]; then
        echo Creating virtualenv
        virtualenv .venv
        install=1
    fi

    echo Activating virtualenv
    . .venv/bin/activate
    [[ "$install" = 1 ]] && pip install -r requirements.txt
fi

open() {
    while ! curl -fso /dev/null http://127.0.0.1:8000; do
        sleep 1
    done
    xdg-open http://localhost:8000/
}

tmux new -s docs -d mkdocs serve
open &
tmux a -t docs
