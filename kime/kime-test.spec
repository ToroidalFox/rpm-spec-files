
Name: kime-test
Version: 3.0.2^git_675_f82ce41
Release: 1
License: GPLv3
Summary: Korean IME
Url: https://github.com/Riey/kime
Source0: %{url}/archive/f82ce41.tar.gz

BuildRequires: cmake
BuildRequires: (clang-devel < 18 or clang17-devel)
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

Requires: (google-noto-sans-cjk-vf-fonts or google-noto-sans-cjk-fonts)
Requires: im-chooser

Conflicts: kime
Conflicts: kime-git

%define kime_out build/out
%define kime_imsettings_conf kime-imsettings.conf

%description
kime is a fast, lightweight, reliable and highly customizable input engine for Korean input.

%prep
%autosetup -n kime-f82ce419f697d4f836e79bf6c3de074f35f96f23

%build
scripts/build.sh -ar

cat > %{kime_out}/%{kime_imsettings_conf} << EOF
SHORT_DESC="kime"
XIM=kime
XIM_PROGRAM=%{_bindir}/kime-xim
GTK_IM_MODULE=kime
QT_IM_MODULE=kime
AUXILIARY_PROGRAM=%{_bindir}/kime-indicator
EOF

%install
install -Dm755 %{kime_out}/kime -t %{buildroot}%{_bindir}
install -Dm755 %{kime_out}/kime-xdg-autostart -t %{buildroot}%{_bindir}
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
install -Dm644 %{kime_out}/%{kime_imsettings_conf} %{buildroot}%{_sysconfdir}/X11/xinit/xinput.d/kime.conf
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
%{_bindir}/kime-xdg-autostart
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

%{_sysconfdir}/X11/xinit/xinput.d/kime.conf
%{_datadir}/applications/kime.desktop
%{_datadir}/icons/hicolor/64x64/apps/*
