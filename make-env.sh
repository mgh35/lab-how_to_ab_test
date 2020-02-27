#!/bin/bash
set -e

if [ -d .venv ]; then
  exit 0
fi

python -m venv .venv
source .venv/bin/activate
if [ ! -f requirements-lock.txt ]; then
  ./lock.sh
fi
pip install -r requirements-lock.txt

jupyter nbextension install --py --sys-prefix widgetsnbextension
jupyter labextension install @jupyter-widgets/jupyterlab-manager
