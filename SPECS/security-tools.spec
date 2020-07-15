Name:           security-tools
Version:        1.0.0
Release:        4%{?dist}
Summary:        Generates 3 uuids for a pool secret
License:        GPLv3
URL:            https://github.com/xcp-ng/security-tools
Source0:        https://github.com/xcp-ng/security-tools/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        pool_secret_wrapper
Source2:        genptoken-cc.service

BuildRequires:  cmake3
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  openssl-libs
BuildRequires:  systemd
%systemd_requires

%description
Generates 3 uuids for a pool secret.

%prep
%autosetup -p1

%build
mkdir build && cd build
%cmake3 .. -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr
make

%install
cd build
make install
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/pool_secret_wrapper
install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/genptoken-cc.service

%post
%systemd_post genptoken-cc.service

%preun
%systemd_preun genptoken-cc.service

%postun
%systemd_postun genptoken-cc.service

%files
%doc LICENSE README.md
%{_bindir}/pool_secret
%{_bindir}/pool_secret_wrapper
%{_unitdir}/genptoken-cc.service

%changelog
* Wed Jul 15 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-4
- Add genptoken-cc.service, since xenserver-firstboot doesn't exist anymore

* Tue Jul 07 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-3
- Rebuild for XCP-ng 8.2

* Fri Dec 20 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-2
- Rebuild for XCP-ng 8.1

* Thu May 02 2019 Benjamin Reis <benjamin.reis@vates.fr> - 1.0.0-1
- Initial package
