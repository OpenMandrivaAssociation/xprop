Name: xprop
Version: 1.2.2
Release: 6
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
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xprop
%{_mandir}/man1/xprop.*


%changelog
* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.1-1mdv2012.0
+ Revision: 699280
- update to new version 1.2.1

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2
+ Revision: 671359
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 591904
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464747
- New version: 1.1.0

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.4-3mdv2009.1
+ Revision: 350811
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-2mdv2009.0
+ Revision: 266149
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 193028
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 154366
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 11 2007 Colin Guthrie <cguthrie@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 61923
- New version 1.0.3


* Tue Aug 29 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-08-29 19:59:28 (58711)
- new upstream release (1.0.2)
   * Don't abort() when actual_format from XGetWindowAttributes is 0.
- This release also (partially) fixes #23308

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:09:04 (31709)
- fill in a few more missing descriptions

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

