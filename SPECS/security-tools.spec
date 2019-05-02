Name:           security-tools
Version:        1.0.0
Release:        1%{?dist}
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
* Thu May 02 2019 Benjamin Reis <benjamin.reis@vates.fr> - 1.0.0-1
- Initial package
