%define upstream_name    Array-Compare
%define upstream_version 2.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Perl extension for comparing arrays
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl-devel

BuildArch: 	noarch

%description 
If you have two arrays and you want to know if they are the same or different,
then Array::Compare will be useful to you.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Array
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.10.0-4mdv2012.0
+ Revision: 765060
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.10.0-2
+ Revision: 667029
- mass rebuild

* Mon Aug 31 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.10.0-1mdv2011.0
+ Revision: 422839
- changing buildrequires:
- adding missing buildrequires:
- update to 2.01

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.170.0-1mdv2010.0
+ Revision: 402979
- rebuild using %%perl_convert_version

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2009.1
+ Revision: 320422
- update to new version 1.17

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2009.0
+ Revision: 230267
- update to new version 1.16

* Fri Mar 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2009.0
+ Revision: 181154
- update to new version 1.15

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.14-2mdv2008.1
+ Revision: 180366
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.14-1mdv2008.0
+ Revision: 19246
-New version


* Mon Apr 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-2mdk
- spec cleanup
- drop useless buildrequires
- better source URL
- better buildrequires syntax

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.13-1mdk
- New release 1.13

* Mon Aug 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-2mdk
- perl-Test-Pod is not mandatory for building

* Wed Mar 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.12-1mdk
- 1.12

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.11-2mdk
- fix buildrequires in a backward compatible way

* Thu Nov 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.11-1mdk 
- new version
- rpmbuildupdate aware

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-2mdk 
- fix directory ownership (distlint)

* Mon Mar 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-1mdk
- first mdk release

