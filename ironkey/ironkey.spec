# Iron Key dependencies.
 
%define name   ironkey
%define version   1.0
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
Requires:   glibc.i686 libgcc_s.so.1

 
%description
Install dependencies for using an Iron Key.
 
%prep
exit 0
 
%build
 
%install

%clean
rm -rf $RPM_BUILD_ROOT
 
%files

%post

%changelog
* Mon Nov 27 2017 1.0
- First release.
