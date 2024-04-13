Name: kime
Version: 3.0.2
Release: 5
License: GPLv3
Summary: Korean IME
Url: https://github.com/Riey/kime
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz

# NOTE: Currently(3.0.2^git_673_33603e0) `kime.desktop` relies on `kime-xdg-autostart` to be in `/usr/bin` which is same as %%{_bindir} for now. However, restructuring is needed if this changes in the future.

# hopefully noarch; not tested.
# BuildArch: noarch

# from README.md of kime github repository,
# build dependencies(package name):
#     cmake(cmake)
#     libclang(clang-devel)
#     cargo(cargo)
#     pkg-config(pkgconf-pkg-config)
# optional build dependencies:
#     gtk3(gtk3-devel)
#     gtk4(gtk4-devel)
#     qtbase5-private(qt5-qtbase-private-devel)
#     qtbase6-private(qt6-qtbase-private-devel)
#     libdbus(dbus-devel)
#     xcb(libxcb-devel)
#     fontconfig(fontconfig-devel)
#     freetype(freetype-devel)
BuildRequires: cmake
BuildRequires: clang-devel
BuildRequires: cargo
BuildRequires: pkgconf-pkg-config
BuildRequires: gtk3-devel
BuildRequires: gtk4-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: dbus-devel
BuildRequires: libxcb-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel

Conflicts: kime-git

%define kime_out build/out

%description

kime is a fast, lightweight, reliable and highly customizable input engine for Korean input.

%prep
%autosetup

%build
scripts/build.sh -ar

%install
install -Dm755 %{kime_out}/kime -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-check -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-indicator -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-candidate-window -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-xim -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-wayland -t %{buildroot}%{_bindir}

install -Dm755 %{kime_out}/libkime_engine.so -t %{buildroot}%{_libdir}
install -Dm755 %{kime_out}/libkime-gtk3.so %{buildroot}%{_libdir}/gtk-3.0/3.0.0/immodules/im-kime.so
install -Dm755 %{kime_out}/libkime-gtk4.so %{buildroot}%{_libdir}/gtk-4.0/4.0.0/immodules/libim-kime.so
install -Dm755 %{kime_out}/libkime-qt5.so %{buildroot}%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
install -Dm755 %{kime_out}/libkime-qt6.so %{buildroot}%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

install -Dm644 %{kime_out}/kime_engine.h -t %{buildroot}%{_includedir}
install -Dm644 %{kime_out}/kime_engine.hpp -t %{buildroot}%{_includedir}

# etc
install -Dm644 %{kime_out}/kime.desktop -t %{buildroot}/etc/xdg/autostart
install -Dm644 %{kime_out}/kime.desktop -t %{buildroot}%{_datadir}/applications
install -Dm644 %{kime_out}/icons/64x64/* -t %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

%files
%license LICENSE*
%doc README.md
%doc README.ko.md
%doc NOTICE.md
%doc docs/CONFIGURATION.md
%doc docs/CONFIGURATION.ko.md
%doc docs/CHANGELOG.md
%doc res/default_config.yaml

%{_bindir}/kime
%{_bindir}/kime-check
%{_bindir}/kime-indicator
%{_bindir}/kime-candidate-window
%{_bindir}/kime-xim
%{_bindir}/kime-wayland

%{_libdir}/libkime_engine.so
%{_libdir}/gtk-3.0/3.0.0/immodules/im-kime.so
%{_libdir}/gtk-4.0/4.0.0/immodules/libim-kime.so
%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

%{_includedir}/kime_engine.h
%{_includedir}/kime_engine.hpp

/etc/xdg/autostart/kime.desktop
%{{_datadir}}/applications/kime.desktop
%{_datadir}/icons/hicolor/64x64/apps/*
