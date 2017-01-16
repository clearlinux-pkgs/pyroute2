#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyroute2
Version  : 0.4.4
Release  : 16
URL      : http://pypi.debian.net/pyroute2/pyroute2-0.4.4.tar.gz
Source0  : http://pypi.debian.net/pyroute2/pyroute2-0.4.4.tar.gz
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
%setup -q -n pyroute2-0.4.4

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484565598
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484565598
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
