#!/bin/bash

sudo ntpdate pool.ntp.org # Avoid JWT Token Errors
python -u "/home/jonathan-imanu/dev/opportune/main.py" 