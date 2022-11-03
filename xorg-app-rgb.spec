Summary:	rgb color-name database and showrgb application
Summary(pl.UTF-8):	Baza danych nazw kolorów rgb i aplikacja showrgb
Name:		xorg-app-rgb
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/rgb-%{version}.tar.xz
# Source0-md5:	d35515ecf63531f4b2c84c4ff2a7a39b
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
# just for dir
Requires:	xorg-lib-libX11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains color-name database (rgb.txt) and showrgb
application to uncompile such database from dbm to source format.

%description -l pl.UTF-8
Ten pakiet zawiera bazę danych nazw kolorów (rgb.txt) oraz aplikację
showrgb do dekompilacji takiej bazy z formatu dbm do źródłowego.

%prep
%setup -q -n rgb-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/showrgb
%{_mandir}/man1/showrgb.1*
%{_datadir}/X11/rgb.txt
