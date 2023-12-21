Name: kime
Version: 3.0.2
Release: 1
License: GPLv3
Summary: Korean IME
Url: https://github.com/Riey/kime
Source0: https://github.com/Riey/kime/archive/refs/tags/v%{version}.tar.gz

# NOTE: On 3.0.2, `kime.desktop` relies on `kime` executable to be in `/usr/bin` which is same as %%{_bindir} for now.
# NOTE: Currently(3.0.2.git.673.33603e0) `kime.desktop` relies on `kime-xdg-autostart` to be in `/usr/bin` which is same as %%{_bindir} for now. However, restructuring is needed if this changes in the future.

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
BuildRequires: cmake clang-devel cargo pkgconf-pkg-config gtk3-devel gtk4-devel qt5-qtbase-private-devel qt6-qtbase-private-devel dbus-devel libxcb-devel fontconfig-devel freetype-devel

%define kime_out build/out

%description

Kime is a fast, lightweight, and reliable input engine for Korean input.

%prep
%autosetup

%build
scripts/build.sh -ar

%install
install -Dm755 %{kime_out}/kime-check -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-indicator -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-candidate-window -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-xim -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-wayland -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime -t %{buildroot}%{_bindir}

install -Dm755 %{kime_out}/libkime_engine.so -t %{buildroot}%{_libdir}
install -Dm755 %{kime_out}/libkime-gtk3.so -t %{buildroot}%{_libdir}/gtk-3.0/3.0.0/immodules/libim-kime.so
install -Dm755 %{kime_out}/libkime-gtk4.so -t %{buildroot}%{_libdir}/gtk-4.0/4.0.0/immodules/libim-kime.so
install -Dm755 %{kime_out}/libkime-qt5.so -t %{buildroot}%{_libdir}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
install -Dm755 %{kime_out}/libkime-qt6.so -t %{buildroot}%{_libdir}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

install -Dm644 %{kime_out}/kime_engine.hpp -t %{buildroot}%{_includedir}
install -Dm644 %{kime_out}/kime_engine.h -t %{buildroot}%{_includedir}

# etc
install -Dm644 %{kime_out}/default_config.yaml -t %{buildroot}/etc/xdg/%{name}/config.yaml
# install -Dm755 %%{kime_out}/kime-xdg-autostart -t %%{buildroot}%%{_bindir} # reserved for next version
install -Dm644 %{kime_out}/kime.desktop -t %{buildroot}/etc/xdg/autostart/kime.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolors/64x64/apps
install -Dm644 %{kime_out}/icons/64x64/* -t %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
# install -Dm644 %%{kime_out}/icons/* %%{buildroot}%%{_datadir}/%%{name}/icons/ # reserved for next version

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

%{_libdir}/libkime_engine.so
%{_libdir}/gtk-3.0/3.0.0/immodules/libim-%{name}.so
%{_libdir}/gtk-4.0/4.0.0/immodules/libim-%{name}.so
%{_libdir}/qt5/plugins/platforminputcontexts/lib%{name}platforminputcontextplugin.so
%{_libdir}/qt6/plugins/platforminputcontexts/lib%{name}platforminputcontextplugin.so

%{_includedir}/kime_engine.hpp
%{_includedir}/kime_engine.h

/etc/xdg/%{name}/config.yaml
# %%{_bindir}/kime-xdg-autostart # reserved for next version
/etc/xdg/autostart/kime.desktop
%{_datadir}/icons/hicolor/64x64/apps/*
# %%{_datadir}/%%{name}/icons/* # reserved for next version

%changelog
* Thu Dec 21 2023 - 3.0.2
- Created with version 3.0.2
