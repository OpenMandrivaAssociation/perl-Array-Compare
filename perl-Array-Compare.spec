%define module  Array-Compare
%define name	perl-%{module}
%define version 1.14
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Perl extension for comparing arrays
License: 	GPL or Artistic
Group: 		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
Buildrequires:	perl(Module::Build)
BuildArch: 	noarch

%description 
If you have two arrays and you want to know if they are the same or different,
then Array::Compare will be useful to you.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%check
./Build test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Array
%{_mandir}/*/*

