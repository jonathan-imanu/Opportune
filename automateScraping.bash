#!/bin/bash

# Avoid JWT Token Errors
sudo ntpdate pool.ntp.org
python -u "/home/jonathan-imanu/dev/opportune/main.py" 