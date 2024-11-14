Name:		xprop
Version:	1.2.8
Release:	1
Summary:	Property displayer for X
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xmu) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)

%description
The xprop utility is for displaying window and font properties in an X server.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xprop
%doc %{_mandir}/man1/xprop.*
