# Chaos Systems i3 window manager and configuration files.
 
%define name    chaossystems-i3
%define version   1.0
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
Requires:   conky dmenu feh i3 i3lock i3status terminator xbacklight
 
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
echo "exec /usr/libexec/gnome-settings-daemon" >> /etc/i3/config

%changelog
* Mon Nov 20 2017 1.0
- First release.
