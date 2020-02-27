#!/bin/bash
set -e

source .venv/bin/activate
pip install -r requirements-jupyter.txt
pip install -r requirements.txt
pip freeze > requirements-lock.txt
