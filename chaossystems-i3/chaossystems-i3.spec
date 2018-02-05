# Chaos Systems i3 window manager and configuration files.
 
%define name    chaossystems-i3
%define version   1.4
%define release   1
 
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildArch:  noarch
BuildRoot:  %{buildroot}
Summary:    Chaos Systems i3 Window Manager
License:    BSD
Name:       %{name}
Version:    %{version}
Release:    %{release}
Group:      Development/Tools
Requires:   arandr arc-theme conky dmenu feh fontawesome-fonts i3 i3lock i3status lxappearance
Requires:   powerline powerline-fonts python-devel redhat-rpm-config rxvt-unicode-256color-ml xbacklight
 
%description
Package that installs and configures the i3 window manager with helpful tools.
 
%prep
exit 0
 
%build
 
%install

%clean
rm -rf $RPM_BUILD_ROOT
 
%files
%defattr(-,root,root,-)

%post
pip install netifaces psutil requests powerline-status
mkdir -p /opt
git clone git://github.com/tobi-wan-kenobi/bumblebee-status /opt/bumblebee-status
ln -s /opt/bumblebee-status/bumblebee-status /usr/local/bin/bumblebee-status

%changelog
* Thu Dec 14 2017 1.4
- Correct the rxvt version, -ml is needed for font support.
- Add powerline.

* Fri Dec 01 2017 1.3
- Add rxvt-unicode-256color

* Fri Dec 01 2017 1.2
- Fix bumblebee install.
- Add X configuration utilities.

* Fri Dec 01 2017 1.1
- Add some more utilities and install a better status bar.

* Mon Nov 20 2017 1.0
- First release.
