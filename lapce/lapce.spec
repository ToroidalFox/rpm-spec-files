Name: lapce
Version: 0.4.0
Release: 1
License: Apache-2.0
Summary: Blazingly fast code editor that supports lsp and wasi plugins.
Url: https://github.com/lapce/lapce
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: clang
BuildRequires: cargo
BuildRequires: pkg-config
BuildRequires: openssl-devel
BuildRequires: perl
# `perl` includes `perl-lib`, `perl-FindBin`, `perl-IPC-Cmd`, `perl-File-Compare`, `perl-File-Copy` as dependency.
BuildRequires: mold
# mold for linker speed

%description
Lapce (IPA: /læps/) is written in pure Rust with a UI in Floem. It is designed with Rope Science from the Xi-Editor which makes for lightning-fast computation, and leverages Wgpu for rendering.

%prep
%autosetup

%build
RUSTFLAGS="-C linker=clang -C link-arg=-fuse-ld=mold" cargo build --profile release-lto

%install
install -Dm755 target/release-lto/%{name} -t %{buildroot}%{_bindir}
install -Dm755 target/release-lto/%{name}-proxy -t %{buildroot}%{_bindir}
install -Dm644 extra/linux/dev.lapce.lapce.desktop -t %{buildroot}%{_datadir}/applications
install -Dm644 extra/linux/dev.lapce.lapce.metainfo.xml -t %{buildroot}%{_datadir}/metainfo
install -Dm644 extra/images/logo.png %{buildroot}%{_datadir}/pixmaps/dev.lapce.lapce.png

%files
%license LICENSE*
%doc README.md
%doc CHANGELOG.md

%{_bindir}/%{name}
%{_bindir}/%{name}-proxy

%{_datadir}/applications
%{_datadir}/metainfo
%{_datadir}/pixmaps/dev.lapce.lapce.png
