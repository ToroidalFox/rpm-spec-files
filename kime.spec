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
BuildRequires: cmake clang-devel cargo gtk3-devel pkgconf-pkg-config fontconfig-devel dbus-devel
# requirements:
#     cmake
#     clang-devel
#     cargo
#     gtk3-devel
# indirect requirements:
#     pkgconf-pkg-config is dependency of gtk3-devel
#     fontconfig-devel is dependency of gtk3-devel
#     dbus-devel is dependency of gtk3-devel
# unchecked requirements:
#     libxcb-devel is may required and is dependency of gtk3-devel

%define kime_conf_dir /etc/xdg/%{name}
%define kime_inc_dir %{_includedir}
%define kime_lib_dir %{_libdir}
%define kime_gtk2_dir %{_libdir}/gtk-2.0/2.10.0/immodules
%define kime_gtk3_dir %{_libdir}/gtk-3.0/3.0.0/immodules
%define kime_qt5_dir %{_libdir}/qt5/plugins/platforminputcontexts
%define kime_icons_dir %{_datadir}/%{name}/icons
%define kime_build_dir build/out

%description

Kime is Korean input method

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup
%build
scripts/build.sh -ar
%py3_build
%install
install -Dm755 build/out/kime-*
install -Dm644 build/out/kime_engine.hpp ${_includedir}
install -Dm644 build/out/kime_engine.h ${_includedir}
install -Dm644 build/out/default_config.yaml
install -Dm644 build/out/icons/* %{_datadir}/%{name}/icons
install -Dm644 build/out/LICENSE 

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{_bindir}/
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
