#!/usr/bin/env bash

# Enable i386 for ironkey
dpkg --add-architecture i386

# Additional repos' keys
# Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
