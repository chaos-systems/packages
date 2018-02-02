# Chaos Systems development tools setup.
 
%define name    chaossystems-devtools
%define version   1.2
%define release   1

%define buildroot %{_topdir}/%{name}-%{version}-root

BuildArch:  noarch
BuildRoot:  %{buildroot}
Summary:    Chaos Systems development tools setup.
License:    BSD
Name:       %{name}
Version:    %{version}
Release:    %{release}
Group:      Development/Tools
Requires:   adobe-source-code-pro-fonts curl fish fzf go hostname make sudo the_silver_searcher tmux tmux-powerline
Requires:   traceroute util-linux-user vim vim-powerline
Requires:   wget git java-9-openjdk-devel nodejs python python-pip ruby sbt scala

 
%description
Package that installs and configures my favorite dev tools.
 
%prep
exit 0
 
%build
 
%install

%clean
rm -rf $RPM_BUILD_ROOT
 
%files
%defattr(-,root,root,-)

%post
sbt update

%changelog
* Mon Jan 22 2018 1.2
- Add linux user utils.

* Mon Nov 20 2017 1.0
- First release.
