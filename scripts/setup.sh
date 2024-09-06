#!/bin/sh

sudo apt update
sudo apt install ntpdate
sudo chmod u+s /usr/sbin/ntpdate

# An alternative is 

# sudo visudo
# your_username ALL=(ALL) NOPASSWD: /usr/sbin/ntpdate