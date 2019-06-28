#!/usr/bin/env bash

# Enable i386 for ironkey
dpkg --add-architecture i386

# Additional repos' keys

# SBT
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823

# i3
/usr/lib/apt/apt-helper download-file http://debian.sur5r.net/i3/pool/main/s/sur5r-keyring/sur5r-keyring_2019.02.01_all.deb keyring.deb SHA256:176af52de1a976f103f9809920d80d02411ac5e763f695327de9fa6aff23f416
dpkg -i ./keyring.deb

# Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# Nodejs
# curl -sL https://deb.nodesource.com/setup_10.x | bash -
