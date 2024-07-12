Name: sshs
Version: 4.4.1
Release: 1
License: MIT
Summary: TUI for SSH
Url: https://github.com/quantumsheep/sshs
Source0: %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo

Requires: openssh

%description

Terminal user interface for SSH. It uses `~/.ssh/config` to list and connect to hosts.

%prep
%autosetup

%build
cargo build --release

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%files
%license LICENSE*

%{_bindir}/%{name}
