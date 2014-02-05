%define upstream_name    Perl-Critic-Tics
%define upstream_version 0.008

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	(this => is => not => good)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/Perl-Critic-Tics-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Perl::Critic)
BuildArch:	noarch

%description
The Perl-Critic-Tics distribution includes extra policies for Perl::Critic
to address a fairly random assortment of things that make me (rjbs) wince.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.6.0-2mdv2011.0
+ Revision: 653615
- rebuild for updated spec-helper

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 575422
- import perl-Perl-Critic-Tics



