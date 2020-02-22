#!/bin/bash
set -e

if [ -d .venv ]; then
  exit 0
fi

python -m venv .venv
source .venv/bin/activate

pip install jupyterlab ipywidgets
jupyter nbextension install --py --sys-prefix widgetsnbextension
jupyter labextension install @jupyter-widgets/jupyterlab-manager
