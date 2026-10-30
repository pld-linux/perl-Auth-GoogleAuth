#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Auth
%define		pnam	GoogleAuth
Summary:	Auth::GoogleAuth - Google Authenticator TOTP abstraction
Summary(pl.UTF-8):	Auth::GoogleAuth - uproszczony interfejs do TOTP z Google Authenticatora
Name:		perl-Auth-GoogleAuth
Version:	1.10
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/G/GR/GRYPHON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70b4bbf1a464b0e595c05f7f39984bc7
URL:		https://metacpan.org/dist/Auth-GoogleAuth
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Convert-Base32
BuildRequires:	perl-CryptX
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test2-Suite
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a simplified interface to supporting typical
two-factor authentication (i.e. "2FA") with Google Authenticator using
the TOTP Algorithm as defined by RFC 6238.

%description -l pl.UTF-8
Ten moduł udostępnia uproszczony interfejs do typowego
uwierzytelniania dwuskładnikowego (2FA) z użyciem Google
Authenticatora i algorytmu TOTP opisanego w RFC 6238.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README SECURITY.md
%{perl_vendorlib}/Auth/GoogleAuth.pm
%{_mandir}/man3/Auth::GoogleAuth.3pm*
