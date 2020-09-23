#!/bin/bash
echo "Installing pico Text-To-Speech module"
echo "====================================="
sudo wget -q https://ftp-master.debian.org/keys/release-10.asc -O- | sudo apt-key add -
sudo su -c "echo 'deb http://deb.debian.org/debian buster non-free' >> /etc/apt/sources.list"
sudo apt update
sudo apt install libttspico-utils