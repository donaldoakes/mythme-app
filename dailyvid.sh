#!/bin/bash
# Launch the mythme dailyvid app.

cd "$(dirname "$0")/../.."
PYTHONPATH=src python3 -m app.dailyvid
