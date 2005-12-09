Summary:	rgb application
Summary(pl):	Aplikacja rgb
Name:		xorg-app-rgb
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/app/rgb-%{version}.tar.bz2
# Source0-md5:	b8b58f314056ac4253d7920934562251
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
# just for dir
Requires:	xorg-lib-libX11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rgb application.

%description -l pl
Aplikacja rgb.

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
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/X11/rgb.txt
%{_mandir}/man1/*.1x*
