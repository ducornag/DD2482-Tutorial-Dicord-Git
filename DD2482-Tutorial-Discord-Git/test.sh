#!/bin/sh
echo This is a file to see if there was any issues with installation of the required tools > /root/log.txt
pip install -U discord.py >> /root/log.txt
