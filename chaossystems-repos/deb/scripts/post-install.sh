#!/usr/bin/env bash

# Enable i386 for ironkey
dpkg --add-architecture i386

# Additional repos

# Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

# Azul
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9
apt-add-repository "deb http://repos.azulsystems.com/ubuntu stable main"

# SBT
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
add-apt-repository "deb https://dl.bintray.com/sbt/debian /"

# Google Cloud
curl -sL https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
apt-add-repository "deb http://packages.cloud.google.com/apt cloud-sdk-bionic main"

# Kubernetes
curl -sL https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"

# Atom
curl -sL https://packagecloud.io/AtomEditor/atom/gpgkey | apt-key add -
apt-add-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main"

# VS Code
curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
apt-add-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

# Slack
curl -sL https://packagecloud.io/slacktechnologies/slack/gpgkey | apt-key add -
apt-add-repository "deb https://packagecloud.io/slacktechnologies/slack/debian/ jessie main"

# Nodejs
curl -sL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
apt-add-repository "deb https://deb.nodesource.com/node_10.x $(lsb_release -cs) main"

# i3
#/usr/lib/apt/apt-helper download-file http://debian.sur5r.net/i3/pool/main/s/sur5r-keyring/sur5r-keyring_2018.01.30_all.deb keyring.deb SHA256:baa43dbbd7232ea2b5444cae238d53bebb9d34601cc000e82f11111b1889078a
#dpkg -i ./keyring.deb
#add-apt-repository "deb http://debian.sur5r.net/i3/ $(lsb_release -cs) universe"
