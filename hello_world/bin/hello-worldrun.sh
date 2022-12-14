#!/bin/bash
set -e
export FLASK_DEBUG=True
export FLASK_APP=hello_world
yarn build
mv build/static/* build/
rm -fR hello_world/static
mv build hello_world/static
cp hello_world/static/index.html hello_world/templates
flask run --port 8000
