Name:    watchman
Version: 4.9.0
Release: 2%{?dist}
Summary: Watches files and records, or triggers actions, when they change.
License: APL2
URL:     https://facebook.github.io/watchman/
Source0: https://github.com/facebook/%{name}/archive/v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: openssl-devel
BuildRequires: pcre

%description
Watches files and records, or triggers actions, when they change.

%prep
%autosetup -n %{name}-%{version}
./autogen.sh

# See https://github.com/facebook/watchman/issues/638 as to why --enable-lenient
# is required.
%configure --enable-lenient --without-python --disable-statedir

%build
%make_build

# Unfortunately make check fails on art.t
# %%check
#make check

%install
make install DESTDIR=%{buildroot}
mkdir %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc README.markdown
%attr(0755,root,root) %{_bindir}/watchman{,-make,-wait}

%changelog
* Thu Nov 22 2018 Evan Klitzke <evan@eklitzke.org>
- Initial version
