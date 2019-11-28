#!/usr/bin/env bash

mkdir -p /opt
git clone git://github.com/tobi-wan-kenobi/bumblebee-status /opt/bumblebee-status
ln -s /opt/bumblebee-status/bumblebee-status /usr/local/bin/bumblebee-status
