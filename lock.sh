#!/bin/bash

[ ! -d .venv ] && python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements-lock.txt
