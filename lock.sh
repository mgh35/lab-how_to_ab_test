#!/bin/bash
set -e

./make-env.sh
source .venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements-lock.txt
