Name:          c-rest-engine
Summary:       minimal http(s) server library
Version:       1.0.5
Release:       2%{?dist}
Group:         Applications/System
Vendor:        VMware, Inc.
License:       Apache 2.0
URL:           http://www.github.com/vmware/c-rest-engine
Requires:      openssl >= 1.0.1
BuildRequires: coreutils >= 8.22
BuildRequires: openssl-devel >= 1.0.1
Source0:       %{name}-%{version}.tar.gz
%define sha1   c-rest-engine=f846acf51e5d8b31d73d78c3d55c14e887208064
Patch0:        c-rest-engine-aarch64.patch

%description
c-rest-engine is a minimal embedded http(s) server written in C.
Its primary intent is to enable REST(Representational State Transfer)
API support for C daemons.

%package devel
Summary: c-rest-engine dev files
Requires:  openssl-devel >= 1.0.1
Requires:  %{name} = %{version}-%{release}

%description devel
development libs and header files for c-rest-engine

%prep
%setup -q
%patch0 -p1

%build
cd build
autoreconf -mif ..
../configure \
    --host=%{_host} --build=%{_build} \
    --prefix=%{_prefix} \
    --with-ssl=/usr \
    --enable-debug=%{_enable_debug} \
    --disable-static

make

%install

[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
cd build && make install DESTDIR=$RPM_BUILD_ROOT
find %{buildroot} -name '*.la' -delete

%post -p  /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%exclude %{_sbindir}/vmrestd

%files devel
%{_includedir}/vmrest.h
%{_libdir}/*.so

# %doc ChangeLog README COPYING

%changelog
*  Tue Nov 14 2017 Alexey Makhalov <amakhalov@vmware.com> 1.0.5-2
-  Aarch64 support
*  Thu Nov 02 2017 Kumar Kaushik <kaushikk@vmware.com> 1.0.5-1
-  Adding version, 1.0.5, get peer info API.
*  Mon Sep 18 2017 Alexey Makhalov <amakhalov@vmware.com> 1.0.4-3
-  Remove coreutils runtime dependency.
*  Tue Sep 12 2017 Kumar Kaushik <kaushikk@vmware.com> 1.0.4-2
-  Making default log level as ERROR.
*  Mon Sep 11 2017 Kumar Kaushik <kaushikk@vmware.com> 1.0.4-1
-  Updating to version 1.0.4.
*  Tue Aug 22 2017 Kumar Kaushik <kaushikk@vmware.com> 1.0.3-2
-  Upstream version 1.0.4 patch for 1.0.3.
*  Fri Jul 21 2017 Kumar Kaushik <kaushikk@vmware.com> 1.0.3-1
-  Updating version to 1.0.3, API for setting SSL info.
*  Tue Jun 20 2017 Kumar Kaushik <kaushikk@vmware.com> 1.0.2-1
-  Updating version to 1.0.2
*  Thu May 18 2017 Kumar Kaushik <kaushikk@vmware.com> 1.0.1-1
-  Updating version to 1.0.1
*  Thu May 04 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.0-1
-  Initial build.  First version
