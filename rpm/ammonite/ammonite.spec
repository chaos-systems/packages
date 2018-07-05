# Ammonite scala REPL.
 
%define name      ammonite
%define version   1.0.3
%define release   1

%define buildroot %{_topdir}/%{name}-%{version}-root

BuildArch:  noarch
BuildRoot:  %{buildroot}
Summary:    Ammonite scala REPL.
License:    BSD
Name:       %{name}
Version:    %{version}
Release:    %{release}
Group:      Development/Tools
Requires:   java-9-openjdk-devel sbt scala

 
%description
The ammonite scala REPL.
 
%prep
exit 0
 
%build
curl -Lso amm https://github.com/lihaoyi/Ammonite/releases/download/1.0.3/2.12-1.0.3
chmod +x amm

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mv $RPM_BUILD_DIR/amm $RPM_BUILD_ROOT/usr/local/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/local/bin/amm

%post

%changelog
* Mon Nov 20 2017 1.0.3
- First release.
