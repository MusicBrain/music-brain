#!/bin/sh

set -e

DIR=$(dirname "$0")

"${DIR}/openneuro/node_modules/.bin/openneuro" download --snapshot 1.0.2 ds003774 "${DIR}/musin-g"
"${DIR}/venv/bin/python" -c "import mne; mne.datasets.sample.data_path('${DIR}')"
