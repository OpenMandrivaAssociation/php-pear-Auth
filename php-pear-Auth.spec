%define		_class		Auth
%define		_status		stable
%define		_pearname	%{_class}

%define		_requires_exceptions pear(IMAPContainer.php)\\|pear(MDBContainer.php)\\|pear(DBLiteContainer.php)\\|pear(PHPUnit.php)

Summary:	%{_pearname} - PHP PEAR authentication class
Name:		php-pear-%{_pearname}
Version:	1.6.1
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Auth/
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The PEAR::Auth package provides methods for creating an authentication
system using PHP.

In PEAR status of this package is: %{_status}.


%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/{Auth,Container,Frontend}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}/Auth/*.php %{buildroot}%{_datadir}/pear/%{_class}/Auth
install %{_pearname}-%{version}/Container/*.php %{buildroot}%{_datadir}/pear/%{_class}/Container
install %{_pearname}-%{version}/Frontend/* %{buildroot}%{_datadir}/pear/%{_class}/Frontend

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{README*,tests,examples}
%dir %{_datadir}/pear/%{_class}
%dir %{_datadir}/pear/%{_class}/Auth
%dir %{_datadir}/pear/%{_class}/Container
%dir %{_datadir}/pear/%{_class}/Frontend
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/Auth/*.php
%{_datadir}/pear/%{_class}/Container/*.php
%{_datadir}/pear/%{_class}/Frontend/*
%{_datadir}/pear/packages/%{_pearname}.xml
