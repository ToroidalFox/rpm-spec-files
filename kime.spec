%global srcname copr-tito-quickdoc
Name: kime
Version: 3.0.2
Release: 1
License: GPLv3
Summary: Korean IME
Url: https://github.com/Riey/kime
Source0: https://github.com/Riey/kime/archive/refs/tags/v3.0.2.tar.gz

# hopefully noarch
# BuildArch: noarch

# build dependencies from kime(package name):
#     cmake(cmake)
#     libclang(clang-devel)
#     cargo(cargo)
#     pkg-config(pkgconf-pkg-config)
# optional dependencies from kime:
#     gtk3(gtk3-devel)
#     gtk4(gtk4-devel)
#     qtbase5-private(qt5-qtbase-private-devel)
#     qtbase6-private(qt6-qtbase-private-devel)
#     libdbus(dbus-devel)
#     xcb(libxcb-devel)
#     fontconfig(fontconfig-devel)
#     freetype(freetype-devel)
BuildRequires: cmake clang-devel cargo pkgconf-pkg-config gtk3-devel gtk4-devel qt5-qtbase-private-devel qt6-qtbase-private-devel dbus-devel libxcb-devel fontconfig-devel freetype-devel

%define kime_out build/out

%description

Kime is a fast and reliable input engine.

%prep
%autosetup

%build
scripts/build.sh -ar

%install
install -Dm755 %{kime-out}/kime-check %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-indicator %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-candidate-window %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-xim %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-wayland %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime %{buildroot}%{_bindir}


install -Dm755 %{kime_out}/libkime-gtk3.so %{buildroot}%{_libdir}/gtk-3.0/3.0.0/immodules/libim-kime.so
install -Dm755 %{kime_out}/libkime-gtk4.so %{buildroot}%{_libdir}/gtk-4.0/4.0.0/immodules/libim-kime.so
install -Dm755 %{kime_out}/libkime-qt5.so %{buildroot}%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
install -Dm755 %{kime_out}/libkime-qt6.so %{buildroot}%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

install -Dm644 %{kime_out}/kime_engine.hpp %{buildroot}%{_includedir}
install -Dm644 %{kime_out}/kime_engine.h %{buildroot}%{_includedir}

# etc
install -Dm644 %{kime_out}/default_config.yaml %{buildroot}/etc/xdg/%{name}/config.yaml
install -Dm755 %{kime_out}/kime-xdg-autostart %{buildroot}%{_bindir}
install -Dm644 %{kime_out}/kime.desktop %{buildroot}/etc/xdg/autostart/kime.desktop
install -Dm644 %{kime_out}/icons/* %{buildroot}%{_datadir}/%{name}/icons/

%files
%license LICENSE*
%doc README.md
%doc NOTICE.md
%doc docs/CONFIGURATION.md
%doc docs/CHANGELOG.md

%{_bindir}/kime-check
%{_bindir}/kime-indicator
%{_bindir}/kime-candidate-window
%{_bindir}/kime-xim
%{_bindir}/kime-wayland
%{_bindir}/kime

%{_libdir}/gtk-3.0/3.0.0/immodules/libim-%{name}.so
%{_libdir}/gtk-4.0/4.0.0/immodules/libim-%{name}.so
%{_libdir}/qt5/plugins/platforminputcontexts/lib%{name}platforminputcontextplugin.so
%{_libdir}/qt6/plugins/platforminputcontexts/lib%{name}platforminputcontextplugin.so

/etc/xdg/%{name}/config.yaml
%{_bindir}/kime-xdg-autostart
/etc/xdg/autostart/kime.desktop
%{_datadir}/%{name}/icons/*

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Thu Dec 21 2023 - 3.0.2
- Created with version 3.0.2
