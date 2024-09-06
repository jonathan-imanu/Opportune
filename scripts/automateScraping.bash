#!/bin/bash

ntpdate pool.ntp.org # Avoid JWT Token Errors
cd "/home/jonathan-imanu/dev/opportune"
source "/home/jonathan-imanu/dev/opportune/venv/bin/activate"
python -u "/home/jonathan-imanu/dev/opportune/main.py" # Run the script