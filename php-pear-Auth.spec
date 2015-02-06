%define		_class		Auth
%define		upstream_name	%{_class}

Name:       php-pear-%{upstream_name}
Version:	1.6.4
Release:	5
Summary:	PHP PEAR authentication class
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Auth/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
The PEAR::Auth package provides methods for creating an authentication
system using PHP.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/README*
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}*
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.4-3mdv2012.0
+ Revision: 741822
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.4-2
+ Revision: 679260
- mass rebuild

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.4-1mdv2011.0
+ Revision: 602115
- new version

* Wed Jan 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.2-1mdv2010.1
+ Revision: 486959
- update to new version 1.6.2

* Tue Nov 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.1-4mdv2010.1
+ Revision: 464348
- spec cleanup
- use rpm filetriggers

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.6.1-3mdv2010.0
+ Revision: 440929
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-2mdv2009.1
+ Revision: 321890
- rebuild

* Mon Sep 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.1-1mdv2009.0
+ Revision: 278647
- update to new version 1.6.1

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-2mdv2009.0
+ Revision: 236800
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.5.1-1mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-1mdv2008.0
+ Revision: 15397
- 1.5.1


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2007.0
+ Revision: 81353
- Import php-pear-Auth

* Sun Jun 04 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2007.0
- fix deps

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdk
- 1.3.0
- drop upstream patches; P0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1mdk
- initial Mandriva package (PLD import)

