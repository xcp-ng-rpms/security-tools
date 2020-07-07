Name:           security-tools
Version:        1.0.0
Release:        3%{?dist}
Summary:        Generates 3 uuids for a pool secret
License:        GPLv3
URL:            https://github.com/xcp-ng/security-tools
Source0:        https://github.com/xcp-ng/security-tools/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  openssl-libs

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

%files
%doc LICENSE README.md
/usr/bin/pool_secret

%changelog
* Tue Jul 07 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-3
- Rebuild for XCP-ng 8.2

* Fri Dec 20 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-2
- Rebuild for XCP-ng 8.1

* Thu May 02 2019 Benjamin Reis <benjamin.reis@vates.fr> - 1.0.0-1
- Initial package
