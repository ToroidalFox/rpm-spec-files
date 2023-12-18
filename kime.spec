%global srcname copr-tito-quickdoc
Name: kime
Version: 3.0.2
Release: 1
License: GPLv3
Summary: Korean IME
Url: https://github.com/Riey/kime
Source0: https://github.com/Riey/kime/archive/refs/tags/v3.0.2.tar.gz

BuildArch: noarch
BuildRequires: cmake clang-libs cargo pkgconf-pkg-config
# requirements verified: cmake cargo pkgconf-pkg-config clang-devel fontconfig-devel dbus-devel

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
