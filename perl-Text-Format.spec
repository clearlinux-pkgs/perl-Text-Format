#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Text-Format
Version  : 0.63
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Text-Format-0.63.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Text-Format-0.63.tar.gz
Summary  : 'Various subroutines to format text.'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Text-Format-license = %{version}-%{release}
Requires: perl-Text-Format-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Text-Format,
version 0.63:
Various subroutines to format text.

%package dev
Summary: dev components for the perl-Text-Format package.
Group: Development
Provides: perl-Text-Format-devel = %{version}-%{release}
Requires: perl-Text-Format = %{version}-%{release}

%description dev
dev components for the perl-Text-Format package.


%package license
Summary: license components for the perl-Text-Format package.
Group: Default

%description license
license components for the perl-Text-Format package.


%package perl
Summary: perl components for the perl-Text-Format package.
Group: Default
Requires: perl-Text-Format = %{version}-%{release}

%description perl
perl components for the perl-Text-Format package.


%prep
%setup -q -n Text-Format-0.63
cd %{_builddir}/Text-Format-0.63
pushd ..
cp -a Text-Format-0.63 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Format
cp %{_builddir}/Text-Format-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Format/38e94f89ec602e1a6495ef7c30477d01aeefedc9 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Format.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Format/38e94f89ec602e1a6495ef7c30477d01aeefedc9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
