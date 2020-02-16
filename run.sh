#!/bin/bash
set -e

if [ ! -e requirements-lock.txt ]; then
  ./lock.sh
fi

[ ! -d .venv ] && python -m venv .venv
source .venv/bin/activate
pip install -r requirements-lock.txt

python setup.py develop

jupyter lab ./notebooks
