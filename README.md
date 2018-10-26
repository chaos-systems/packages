# Chaos Systems Packages

## Bootstrapping an OS

### RPM
`rpm -ivh https://s3-eu-west-1.amazonaws.com/chaossystems-repositories/artifacts/rpm/chaossystems/noarch/chaossystems-repos-1.0-1.noarch.rpm`

### DNF
`dnf install -y https://s3-eu-west-1.amazonaws.com/chaossystems-repositories/artifacts/rpm/chaossystems/noarch/chaossystems-repos-1.0-1.noarch.rpm`

### Apt/Deb
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 379CE192D401AB61
echo "deb https://dl.bintray.com/chaos-systems/deb bionic main" | sudo tee /etc/apt/sources.list.d/chaossystems.list
```

## Reference
https://github.com/nebula-plugins/gradle-ospackage-plugin  
https://github.com/nebula-plugins/gradle-ospackage-plugin/wiki/Deb-Plugina  
https://github.com/nebula-plugins/gradle-ospackage-plugin/wiki/RPM-Plugin  

https://github.com/bintray/gradle-bintray-plugin  
