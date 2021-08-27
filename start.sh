#!/bin/bash
port=8009

if [ ! -d "logs/" ]; then
    mkdir "logs/"
fi
gunicorn server:app -b 0.0.0.0:${port} -w 4 -k uvicorn.workers.UvicornH11Worker -D -p .pid --access-logfile=logs/access.log --error-logfile=logs/error.log