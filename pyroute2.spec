#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyroute2
Version  : 0.3.18
Release  : 6
URL      : https://pypi.python.org/packages/source/p/pyroute2/pyroute2-0.3.18.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyroute2/pyroute2-0.3.18.tar.gz
Summary  : Python Netlink library
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+
Requires: pyroute2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Pyroute2 package is dual licensed since 0.3.6, emerging two licenses:
* GPL v2+
* Apache v2

%package python
Summary: python components for the pyroute2 package.
Group: Default

%description python
python components for the pyroute2 package.


%prep
%setup -q -n pyroute2-0.3.18

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
