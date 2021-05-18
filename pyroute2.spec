#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyroute2
Version  : 0.6.1
Release  : 52
URL      : https://files.pythonhosted.org/packages/ef/84/2cb5108af53c8da3d1c4e2335c8a28c30d1a1e984fc5463e0e16531d2236/pyroute2-0.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/84/2cb5108af53c8da3d1c4e2335c8a28c30d1a1e984fc5463e0e16531d2236/pyroute2-0.6.1.tar.gz
Summary  : Python Netlink library
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+
Requires: pyroute2-license = %{version}-%{release}
Requires: pyroute2-python = %{version}-%{release}
Requires: pyroute2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Pyroute2
        ========
        
        Pyroute2 is a pure Python **netlink** library. The core requires only Python
        stdlib, no 3rd party libraries. The library was started as an RTNL protocol
        implementation, so the name is **pyroute2**, but now it supports many netlink

%package license
Summary: license components for the pyroute2 package.
Group: Default

%description license
license components for the pyroute2 package.


%package python
Summary: python components for the pyroute2 package.
Group: Default
Requires: pyroute2-python3 = %{version}-%{release}

%description python
python components for the pyroute2 package.


%package python3
Summary: python3 components for the pyroute2 package.
Group: Default
Requires: python3-core
Provides: pypi(pyroute2)
Requires: pypi(pyroute2.core)
Requires: pypi(pyroute2.ethtool)
Requires: pypi(pyroute2.ipdb)
Requires: pypi(pyroute2.ipset)
Requires: pypi(pyroute2.ndb)
Requires: pypi(pyroute2.nftables)
Requires: pypi(pyroute2.nslink)

%description python3
python3 components for the pyroute2 package.


%prep
%setup -q -n pyroute2-0.6.1
cd %{_builddir}/pyroute2-0.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621358273
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyroute2
cp %{_builddir}/pyroute2-0.6.1/LICENSE.Apache.v2 %{buildroot}/usr/share/package-licenses/pyroute2/cd9bad64b174708395f795bb92f7b4be7d996e8f
cp %{_builddir}/pyroute2-0.6.1/LICENSE.GPL.v2 %{buildroot}/usr/share/package-licenses/pyroute2/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
rm -rf %{buildroot}/usr/lib/python3*/site-packages/tests
## install_append end

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyroute2/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/pyroute2/cd9bad64b174708395f795bb92f7b4be7d996e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
