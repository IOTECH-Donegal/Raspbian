#!/bin/bash
# by: JOR
# Date: 10JAN20
# Function: Configure GIT
# Script: GITInstall.sh

clear
echo "*******************************************************"
echo "Welcome" $USER
echo "This script will create keys for new RPi"
echo "Edit the script as needs"
echo "*******************************************************"

echo "Creating Unique Key"
ssh-keygen -t rsa -b 4096 -f ~/.ssh/git.rsa -C admin@iotech.ie
echo "Now copy this up to the GIT account"

# eval `ssh-agent`
ssh-add ~/.ssh/git.rsa

git clone git@github.com:IOTECH-Donegal/Raspbian.git
git status
git config --global user.name "IOTECH-Donegal"
git config --global user.email "ansible1@iotech.ie"
git config --list
echo '*************************************************'
echo 'Hey' $USER ', all done!'
