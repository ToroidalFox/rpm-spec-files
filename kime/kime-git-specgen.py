import requests as web
import json
import re

OUTPUT_NAME = "kime-git.spec"

REPO_API = "https://api.github.com/repos/Riey/kime"
REPO_TAGS = f"{REPO_API}/tags"
REPO_DEV_BRANCH = f"{REPO_API}/branches/develop"
REPO_DEV_LATEST_COMMIT = f"{REPO_API}/commits?sha=develop&per_page=1&page=1"

COMMIT_COUNT_REGEX = r'[?&]page=(\d+)[^;]*?>\s*;\s*rel\s*=\s*"last"'

repo_latest_tag = json.loads(web.get(REPO_TAGS).content)[0]["name"].strip()[1:]
repo_latest_commit = web.get(REPO_DEV_LATEST_COMMIT)
# header "Link" example of `repo_latest_commit`
# REPO_LATEST_COMMIT_LINK_HEADER_EXAMPLE = '<https://api.github.com/repositories/320661831/commits?sha=develop&per_page=1&page=2>; rel="next", <https://api.github.com/repositories/320661831/commits?sha=develop&per_page=1&page=675>; rel="last"'
repo_commit_count = re.search(
    COMMIT_COUNT_REGEX, repo_latest_commit.headers["Link"]
).group(1)  # type: ignore
repo_latest_commit_id = json.loads(repo_latest_commit.content)[0]["sha"][:7]


package_version = f"{repo_latest_tag}^git_{repo_commit_count}_{repo_latest_commit_id}"

package_spec = f"""
Name: kime-git
Version: {package_version}
Release: 1
License: GPLv3
Summary: Korean IME
Url: https://github.com/Riey/kime
Source0: %{{url}}/archive/{repo_latest_commit_id}.tar.gz

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

%define kime_out build/out

%description
kime is a fast, lightweight, reliable and highly customizable input engine for Korean input.

%prep
%autosetup

%build
scripts/build.sh -ar
cat > %{{kime_out}}/kime-test.desktop << EOF
[Desktop Entry]
Exec=/usr/bin/kime
Name=kime daemon
Name[ko]=kime 데몬
Comment=Start kime daemon
Type=Application
Terminal=false
NoDisplay=true
StartupNotify=false
X-DBUS-StartupType=Unique
X-GNOME-AutoRestart=false
X-GNOME-Autostart-Notify=false
X-KDE-StartupNotify=false
X-KDE-Wayland-VirtualKeyboard=true
Icon=kime-han-black
EOF

%install
install -Dm755 %{{kime_out}}/kime-check -t %{{buildroot}}%{{_bindir}}
install -Dm755 %{{kime_out}}/kime-indicator -t %{{buildroot}}%{{_bindir}}
install -Dm755 %{{kime_out}}/kime-candidate-window -t %{{buildroot}}%{{_bindir}}
install -Dm755 %{{kime_out}}/kime-xim -t %{{buildroot}}%{{_bindir}}
install -Dm755 %{{kime_out}}/kime-wayland -t %{{buildroot}}%{{_bindir}}
install -Dm755 %{{kime_out}}/kime -t %{{buildroot}}%{{_bindir}}

install -Dm755 %{{kime_out}}/libkime_engine.so -t %{{buildroot}}%{{_libdir}}
install -Dm755 %{{kime_out}}/libkime-gtk3.so %{{buildroot}}%{{_libdir}}/gtk-3.0/3.0.0/immodules/im-kime.so
install -Dm755 %{{kime_out}}/libkime-gtk4.so %{{buildroot}}%{{_libdir}}/gtk-4.0/4.0.0/immodules/libim-kime.so
install -Dm755 %{{kime_out}}/libkime-qt5.so %{{buildroot}}%{{_libdir}}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
install -Dm755 %{{kime_out}}/libkime-qt6.so %{{buildroot}}%{{_libdir}}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

install -Dm644 %{{kime_out}}/kime_engine.hpp -t %{{buildroot}}%{{_includedir}}
install -Dm644 %{{kime_out}}/kime_engine.h -t %{{buildroot}}%{{_includedir}}

# etc
#install -Dm755 %{{kime_out}}/kime.desktop -t /etc/xdg/autostart
install -Dm755 %{{kime_out}}/kime-test.desktop /etc/xdg/autostart/kime.desktop
# install -Dm755 %%{{kime_out}}/kime-xdg-autostart -t %%{{buildroot}}%%{{_bindir}} # reserved for next version
install -Dm644 %{{kime_out}}/default_config.yaml %{{buildroot}}/etc/xdg/%{{name}}/config.yaml
mkdir -p %{{buildroot}}%{{_datadir}}/icons/hicolors/64x64/apps
install -Dm644 %{{kime_out}}/icons/64x64/* -t %{{buildroot}}%{{_datadir}}/icons/hicolor/64x64/apps
# install -Dm644 %%{{kime_out}}/icons/* %%{{buildroot}}%%{{_datadir}}/%%{{name}}/icons/ # reserved for next version

%files
%license LICENSE*
%doc README.md
%doc NOTICE.md
%doc docs/CONFIGURATION.md
%doc docs/CHANGELOG.md

%{{_bindir}}/kime-check
%{{_bindir}}/kime-indicator
%{{_bindir}}/kime-candidate-window
%{{_bindir}}/kime-xim
%{{_bindir}}/kime-wayland
%{{_bindir}}/kime

%{{_libdir}}/libkime_engine.so
%{{_libdir}}/gtk-3.0/3.0.0/immodules/im-kime.so
%{{_libdir}}/gtk-4.0/4.0.0/immodules/libim-kime.so
%{{_libdir}}/qt5/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so
%{{_libdir}}/qt6/plugins/platforminputcontexts/libkimeplatforminputcontextplugin.so

%{{_includedir}}/kime_engine.hpp
%{{_includedir}}/kime_engine.h

# %%{{_bindir}}/kime-xdg-autostart # reserved for next version
/etc/xdg/%{{name}}/config.yaml
%{{_datadir}}/icons/hicolor/64x64/apps/*
# %%{{_datadir}}/%%{{name}}/icons/* # reserved for next version
"""

with open(file="kime-git.spec", mode="w") as spec_file:
    spec_file.write(package_spec)
