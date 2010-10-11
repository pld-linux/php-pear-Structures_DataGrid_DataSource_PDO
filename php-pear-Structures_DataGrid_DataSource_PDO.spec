%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_PDO
%define		subver	dev1
%define		rel		1
Summary:	%{_pearname} - DataSource driver using PHP Data Objects (PDO) and an SQL query
Summary(pl.UTF-8):	%{_pearname} - sterownik DataSource korzystający z PHP Data Objects (PDO) i zapytań SQL
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	0.%{subver}.%{rel}
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	b61246f5944312afe7ca244a2fa70705
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_PDO/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Structures_DataGrid >= 0.8.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a DataSource driver for Structures_DataGrid using PHP Data
Objects (PDO) and an SQL query.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza sterownik DataSource korzystający z obiektów
danych PHP (PDO, czyli PHP Data Objects) i zapytań języka SQL.

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
%{php_pear_dir}/Structures/DataGrid/DataSource/PDO.php
