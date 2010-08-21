%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Validate_PL
Summary:	%{_pearname} - Validation class for PL
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Polski
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	eccc66ffc128a0fb3468480be93458d0
URL:		http://pear.php.net/package/Validate_PL/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for PL such as:
- NIP
- Bank Numbers
- PESEL
- REGON

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Polski danych takich jak:
- NIP
- numery kont bankowych
- PESEL
- REGON

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/PL.php

%{php_pear_dir}/data/%{_pearname}
