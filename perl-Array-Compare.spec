%define upstream_name Array-Compare

Summary:	Perl extension for comparing arrays
Name:		perl-%{upstream_name}
Version:	3.0.8
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Array::Compare
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/Array-Compare-v%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Moo)
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
# For tests
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Types::Standard)

%description 
If you have two arrays and you want to know if they are the same or different,
then Array::Compare will be useful to you.

%prep
%autosetup -n %{upstream_name}-v%{version} -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Array
%doc %{_mandir}/man3/*
