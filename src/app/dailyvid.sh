#!/bin/bash
# Runs daily background logic for mythme dailyvid.
# Schedule via cron to execute every day at 3:00 am:
#   0 3 * * * /path/to/src/app/dailyvid.sh

cd "$(dirname "$0")/../.."
PYTHONPATH=src python3 -m app.utils.background
