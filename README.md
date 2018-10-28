# Chaos Systems Packages

## Bootstrapping an OS

### RPM
`rpm -ivh https://s3-eu-west-1.amazonaws.com/chaossystems-repositories/artifacts/rpm/chaossystems/noarch/chaossystems-repos-1.0-1.noarch.rpm`

### DNF
`dnf install -y https://s3-eu-west-1.amazonaws.com/chaossystems-repositories/artifacts/rpm/chaossystems/noarch/chaossystems-repos-1.0-1.noarch.rpm`

### Apt/Deb
```
apt-get update
apt-get install -y ca-certificates gnupg2 lsb-release software-properties-common
apt-key adv --keyserver keyserver.ubuntu.com --recv-key 379CE192D401AB61
apt-add-repository "deb https://dl.bintray.com/chaos-systems/deb $(lsb_release -cs) main"
apt-get install -y chaossystems-repos
```

## Reference
https://github.com/nebula-plugins/gradle-ospackage-plugin  
https://github.com/nebula-plugins/gradle-ospackage-plugin/wiki/Deb-Plugina  
https://github.com/nebula-plugins/gradle-ospackage-plugin/wiki/RPM-Plugin  

https://github.com/bintray/gradle-bintray-plugin  
