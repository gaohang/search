#!/bin/bash
port=8008

if [ ! -d "logs/" ]; then
    mkdir "logs/"
fi
gunicorn server:app -b 0.0.0.0:${port} -w 4 -k uvicorn.workers.UvicornH11Worker -D -e debug=true -p .pid_debug --access-logfile=logs/access_debug.log --error-logfile=logs/error_debug.log