#!/bin/bash
# Starts the Gunicorn server
set -e

# Activate the virtualenv for this project
source /home/ubuntu/webapps/miffy/miffyenv/bin/activate

# Start gunicorn going
exec uwsgi run_project.ini
