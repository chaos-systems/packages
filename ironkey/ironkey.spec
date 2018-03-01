# Iron Key dependencies.
 
%define name   ironkey
%define version   2.0
%define release   1

%define buildroot %{_topdir}/%{name}-%{version}-root

BuildArch:  noarch
BuildRoot:  %{buildroot}
Summary:    Iron Key dependencies.
License:    BSD
Name:       %{name}
Version:    %{version}
Release:    %{release}
Group:      Development/Tools
Requires:   glibc(x86-32) libgcc_s.so.1 libu2f-host-devel

 
%description
Install dependencies for using an Iron Key and a YubiKey.
 
%prep
exit 0
 
%build
 
%install

%clean
rm -rf $RPM_BUILD_ROOT
 
%files

%post

%changelog
* Wed Feb 28 2018 2.0
- Add YubiKey libs.

* Mon Nov 27 2017 1.0
- First release.
