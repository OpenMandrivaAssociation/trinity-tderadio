%bcond clang 1
%bcond lirc 1
%bcond lame 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg tderadio
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	0.1.1.1
Release:	%{?tde_version:%{tde_version}_}3
Summary:	Comfortable Radio Application for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:  	cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:  trinity-tde-cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires:  pkgconfig(sndfile)

%{?with_lirc:BuildRequires:	lirc-devel}

# LAME support
%{?with_lame:BuildRequires:  pkgconfig(lame)}

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes:		trinity-kradio < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kradio = %{?epoch:%{epoch}:}%{version}-%{release}


%description
TDERadio is a comfortable radio application for Trinity with support for 
V4L and V4L2 radio cards drivers.

TDERadio currently provides

 * V4L/V4L2 radio support
%if 0%{?with_lirc}
 * Remote control support (LIRC)
%endif
 * Alarms, sleep Countdown
 * Several GUI Controls (Docking Menu, Station Quickbar, Radio Display)
 * Recording capabilities, including MP3 and Ogg/Vorbis encoding
 * Timeshifter functionality
 * Extendable plugin architecture

This package also includes a growing collection of station preset
files for many cities around the world contributed by TDERadio users.

As TDERadio is based on an extendable plugin architecture, contributions
of new plugins (e.g. Internet Radio Streams, new cool GUIs) are welcome.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"


%install -a
# Remove devel files
%__rm -f %{?buildroot}%{tde_prefix}/%{_lib}/libtderadio.la
%__rm -f %{?buildroot}%{tde_prefix}/%{_lib}/libtderadio.so

# Remove pixmas
%__rm -fr %{?buildroot}%{tde_prefix}/share/pixmaps/


%files
%defattr(-,root,root,-)
%{tde_prefix}/bin/convert-presets
%{tde_prefix}/bin/tderadio
%{tde_prefix}/%{_lib}/libtderadio.so.0
%{tde_prefix}/%{_lib}/libtderadio.so.0.0.0
%dir %{tde_prefix}/%{_lib}/tderadio
%dir %{tde_prefix}/%{_lib}/tderadio/plugins
%{tde_prefix}/%{_lib}/tderadio/plugins/*.la
%{tde_prefix}/%{_lib}/tderadio/plugins/*.so
%{tde_prefix}/share/applications/tde/tderadio.desktop
%{tde_prefix}/share/apps/tderadio/
%dir %{tde_prefix}/share/icons/hicolor/256x256
%dir %{tde_prefix}/share/icons/hicolor/256x256/actions
%{tde_prefix}/share/icons/hicolor/*/*/tderadio*.png
%{tde_prefix}/share/icons/locolor/*/*/tderadio*.png
%lang(de) %{tde_prefix}/share/locale/de/LC_MESSAGES/*.mo
%lang(es) %{tde_prefix}/share/locale/es/LC_MESSAGES/*.mo
%lang(it) %{tde_prefix}/share/locale/it/LC_MESSAGES/*.mo
%lang(ka) %{tde_prefix}/share/locale/ka/LC_MESSAGES/*.mo
%lang(nl) %{tde_prefix}/share/locale/nl/LC_MESSAGES/*.mo
%lang(pl) %{tde_prefix}/share/locale/pl/LC_MESSAGES/*.mo
%lang(pt) %{tde_prefix}/share/locale/pt/LC_MESSAGES/*.mo
%lang(ru) %{tde_prefix}/share/locale/ru/LC_MESSAGES/*.mo
%{tde_prefix}/share/doc/tde/HTML/en/tderadio/
%{tde_prefix}/share/man/man1/convert-presets.1*
%{tde_prefix}/share/man/man1/tderadio.1*

