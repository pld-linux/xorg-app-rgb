# $Rev: 3360 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	rgb application
Summary(pl):	Aplikacja rgb
Name:		xorg-app-rgb
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/rgb-%{version}.tar.bz2
# Source0-md5:	f893387b619394707e83a4118ca484a1
Patch0:		rgb-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/rgb-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
rgb application.

%description -l pl
Aplikacja rgb.


%prep
%setup -q -n rgb-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_bindir}/*
%{_libdir}/rgb.txt
%{_mandir}/man1/*.1*
