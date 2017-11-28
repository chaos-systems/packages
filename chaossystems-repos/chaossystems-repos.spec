# Chaos Systems RPM Repository configuration files.
 
%define name    chaossystems-repos
%define version   1.0
%define release   1
 
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildArch:  noarch
BuildRoot:  %{buildroot}
Summary:    Chaos Systems RPM Repository
License:    BSD
Name:       %{name}
Version:    %{version}
Release:    %{release}
Group:      Development/Tools
Requires:   dnf-plugins-core
 
%description
Package containing Chaos Systems RPM Repository configuration files.
 
%prep
exit 0
 
%build
 
%files
%defattr(-,root,root,-)
/etc/yum.repos.d/chaossystems.repo
/etc/yum.repos.d/google-cloud-sdk.repo
/etc/yum.repos.d/nodejs.repo
/etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
cp -p %{_srcdir}/chaossystems.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p %{_srcdir}/google-cloud-sdk.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p %{_srcdir}/nodejs.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p %{_srcdir}/NODESOURCE-GPG-SIGNING-KEY-EL $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

%post
dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
curl -Lso /etc/yum.repos.d/bintray-sbt-rpm.repo https://bintray.com/sbt/rpm/rpm

%clean
rm -rf $RPM_BUILD_ROOT
 
%changelog
* Mon Nov 20 2017 1.0
- First release.
