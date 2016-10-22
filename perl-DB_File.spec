%{?scl:%scl_package perl-DB_File}

Name:           %{?scl_prefix}perl-DB_File
Version:        1.838
Release:        3%{?dist}
Summary:        Perl5 access to Berkeley DB version 1.x
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DB_File/
Source0:        http://www.cpan.org/authors/id/P/PM/PMQS/DB_File-%{version}.tar.gz
# Destroy DB_File objects only from original thread context, bug #1107732,
# CPAN RT#96357
Patch0:         DB_File-1.838-Destroy-DB_File-objects-only-from-original-thread-co.patch
BuildRequires:  coreutils
BuildRequires:  findutils
%if 0%{?rhel} < 7
BuildRequires:  db4-devel
%else
BuildRequires:  libdb-devel
%endif
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Constant)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 5.16
# File::Copy not needed if ExtUtils::Constant is available
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
# DynaLoader not needed if XSLoader is available
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(Tie::Hash)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(threads)
%if !%{defined perl_bootstrap} && !%{defined perl_small}
# Optional tests:
# Data::Dumper not useful
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Fcntl)
Requires:       %{?scl_prefix}perl(XSLoader)

%{?perl_default_filter}

%description
DB_File is a module which allows Perl programs to make use of the facilities
provided by Berkeley DB version 1.x (if you have a newer version of DB, you
will be limited to functionality provided by interface of version 1.x). The
interface defined here mirrors the Berkeley DB interface closely.

%prep
%setup -q -n DB_File-%{version}
%patch0 -p1
find -type f -exec chmod -x {} +
%{?scl:scl enable %{scl} '}perl -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(qw{dbinfo})"%{?scl:'}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes dbinfo README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DB_File*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1.838-3
- SCL

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.838-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Petr Pisar <ppisar@redhat.com> - 1.838-1
- 1.838 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.835-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.835-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.835-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.835-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.835-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.835-2
- Perl 5.22 rebuild

* Fri Jan 02 2015 Petr Pisar <ppisar@redhat.com> - 1.835-1
- 1.835 bump

* Thu Dec 11 2014 Petr Pisar <ppisar@redhat.com> - 1.834-1
- 1.834 bump

* Wed Dec 10 2014 Petr Pisar <ppisar@redhat.com> - 1.833-1
- 1.833 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.831-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.831-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.831-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.831-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Petr Pisar <ppisar@redhat.com> - 1.831-5
- Build-require Test::More always because of the new thread tests

* Thu Aug 07 2014 Petr Pisar <ppisar@redhat.com> - 1.831-4
- Initialize db_DESTROY return variable (bug #1107732)

* Thu Aug 07 2014 Petr Pisar <ppisar@redhat.com> - 1.831-3
- Destroy DB_File objects only from original thread context (bug #1107732)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.831-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Petr Pisar <ppisar@redhat.com> - 1.831-1
- 1.831 bump

* Mon Nov 04 2013 Petr Pisar <ppisar@redhat.com> - 1.830-1
- 1.830 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.829-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.829-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.829-2
- Perl 5.18 rebuild

* Wed Jul 10 2013 Petr Pisar <ppisar@redhat.com> - 1.829-1
- 1.829 bump

* Thu May 09 2013 Petr Pisar <ppisar@redhat.com> - 1.828-1
- 1.828 bump

* Thu Mar 21 2013 Petr Pisar <ppisar@redhat.com> 1.827-1
- Specfile autogenerated by cpanspec 1.78.
