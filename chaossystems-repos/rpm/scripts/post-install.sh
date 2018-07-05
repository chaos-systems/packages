#!/usr/bin/env bash

dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
curl -Lso /etc/yum.repos.d/bintray-sbt-rpm.repo https://bintray.com/sbt/rpm/rpm
