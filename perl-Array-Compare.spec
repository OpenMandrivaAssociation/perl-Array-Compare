%define upstream_name    Array-Compare
%define upstream_version 2.02

Summary:	Perl extension for comparing arrays
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Array/Array-Compare-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires: perl(Test::NoWarnings)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)

%description 
If you have two arrays and you want to know if they are the same or different,
then Array::Compare will be useful to you.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

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
%{_mandir}/man3/*


