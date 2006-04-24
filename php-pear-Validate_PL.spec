%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	PL
%define		_status		alpha
%define		_pearname	Validate_PL

Summary:	%{_pearname} - Validation class for PL
Summary(pl):	%{_pearname} - Klasa sprawdzaj�ca poprawno�� dla Polski
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b2cd0211fcab3d3831d7d4652a59f7fe
URL:		http://pear.php.net/package/Validate_PL/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:4.1.0
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

%description -l pl
Pakiet do sprawdzania poprawno�ci danych dla Polski:
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/PL.php
