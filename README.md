# Chaos Systems Packages

## Bootstrapping an OS

### Apt/Deb
```
curl -fsSL https://apt.cha0s.dev/pub.gpg | (OUT=$(sudo apt-key add - 2>&1) || echo $OUT)
echo "deb https://apt.cha0s.dev stable main" | sudo tee -a /etc/apt/sources.list.d/chaos-dev.list
```

## Additional Repos

### Docker
[Full Instructions](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)

```sh
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### i3
[Full Instructions](https://i3wm.org/docs/repositories.html)

```sh
sudo /usr/lib/apt/apt-helper download-file https://debian.sur5r.net/i3/pool/main/s/sur5r-keyring/sur5r-keyring_2019.02.01_all.deb keyring.deb SHA256:176af52de1a976f103f9809920d80d02411ac5e763f695327de9fa6aff23f416
sudo dpkg -i ./keyring.deb
sudo echo "deb https://debian.sur5r.net/i3/ $(grep '^DISTRIB_CODENAME=' /etc/lsb-release | cut -f2 -d=) universe" >> /etc/apt/sources.list.d/sur5r-i3.list
```

### Azul Java
[Full Instructions](https://docs.azul.com/zulu/zuludocs/ZuluUserGuide/PrepareZuluPlatform/AttachAPTRepositoryUbuntuOrDebianSys.htm)

```sh
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9
sudo apt-add-repository 'deb http://repos.azulsystems.com/ubuntu stable main'
```

### Slack


### VSCode
[Full Instructions](https://code.visualstudio.com/docs/setup/linux)

```sh
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
```
## Reference
https://github.com/nebula-plugins/gradle-ospackage-plugin  
https://github.com/nebula-plugins/gradle-ospackage-plugin/wiki/Deb-Plugina  
https://github.com/nebula-plugins/gradle-ospackage-plugin/wiki/RPM-Plugin  

https://github.com/bintray/gradle-bintray-plugin  
