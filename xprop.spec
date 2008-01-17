Name: xprop
Version: 1.0.3
Release: %mkrel 2
Summary: Property displayer for X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.0.0
BuildRequires: libxmu-devel	>= 1.0.3

%description
The xprop utility is for displaying window and font properties in an X server.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xprop
%{_mandir}/man1/xprop.*
