Name: xprop
Version: 1.2.4
Release: 1
Summary: Property displayer for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xprop utility is for displaying window and font properties in an X server.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xprop
%{_mandir}/man1/xprop.*
