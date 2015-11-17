Name:    libxio
Version: 1.5
Release: 1%{?dist}
Summary: Accelio - The Open Source I/O, Message, and RPC Acceleration Library

Group:   System Environment/Libraries
License: GPLv2 or BSD
Url:     http://www.accelio.org/
Source:  http://github.com/accelio/accelio/archive/v%{version}.tar.gz

BuildRequires: autoconf, libtool
BuildRequires: numactl-devel, libaio-devel, libibverbs-devel, librdmacm-devel

%description
Accelio provides an easy-to-use, reliable, scalable,
and high performance data/message delivery middleware
that maximizes the efficiency of modern CPU and NIC hardware
and that reduces time-to-market of new scale-out applications.


%package devel
Summary: Development files for the libxio library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release} libibverbs-devel%{?_isa}

%description devel
Development files for the libxio library.


%prep
%setup -q -n accelio-%{version}

%build
autoreconf -svfi
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# remove unpackaged files from the buildroot
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%{_bindir}/*
%{_libdir}/libxio.so*
%{_libdir}/libraio.so*
%doc AUTHORS COPYING README

%files devel
%{_includedir}/*


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
* Tue Nov 17 2015 Mikhail Ushanov <gm.mephisto@gmail.com> 1.5-1
- Initial spec file
