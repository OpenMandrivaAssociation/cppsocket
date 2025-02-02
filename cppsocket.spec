%define	name		cppsocket
%define	version		0.8.4
%define	release		 %mkrel 6
%define	lib_name_orig	lib%{name}
%define	lib_major	0
%define	lib_name	%mklibname %{name} %{lib_major}
%define	lib_name_devel	%mklibname %{name} -d

Name:		%{name}
Summary:	A small and easy to use C++ library for programming with TCP and UDP sockets
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.bz2
Patch0:		cppsocket-0.8.4-gcc3_4.patch
Patch1:		cppsocket-0.8.4-gcc43-fix.patch
URL:		https://www.sourceforge.net/projects/cppsocket
#BuildRequires:	

%description
CPPSocket is a small Classlibrary for C++ that supports a easy usage of
socket-programming for networking-software.
It provides a simple object-oriented interface to the classic C Library
calls. Additionally it provides a simplified abstraction for creating
clients and servers.

With CPPSocket supports the following network protocols:
- TCP (transmission control protocol; needs an established connection
  from one host to another)
- UDP (user datagram protocol; packets can be sent without an established
  connection)
- IPv4 (internet protocol version 4; uses 32-bit network addresses)

These protocols are what may also be called TCP/IP.

The library provides two layers of abstraction:
- Low-Level
  This is a simple oo interface of the classic socket calls.
  But it provides some (optional) abstractions for addressing and buffering.
  Useful for more experienced programmers, that have already worked with
  classic sockets.

- High-Level
  This provides somewhat more abstraction and ignores some functionality of
  the full blown sockets.
  But nevertheless it is quite useful and makes programming of networking
  software very easy.
  So it's intended to be used by novice programmers or those who don't want
  the maximum complexity/flexibility but an easy to use network-interface.
		
%package -n %{lib_name}
Summary: Main library for %{name}
Group: System/Libraries
Provides: %{lib_name_orig} = %{version}-%{release} %{name} = %{version}-%{release}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{lib_name_devel}
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{lib_name} = %{version} libexpat-devel
Provides: %{lib_name_orig}-devel = %{version}-%{release} %{name}-devel = %{version}-%{release}
Obsoletes: %{lib_name}-devel

%description -n %{lib_name_devel}
This package contains the headers that programmers will need to develop
applications which will use %{name}, a C++ library for programming with
TCP and UDP sockets.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .gcc3_4
%patch1 -p0

%build
%configure2_5x	--enable-final \
		--with-gnu-ld \
		--disable-static \
		--with-pic
		
%make

%install
%makeinstall_std


%files -n %{lib_name}
%doc AUTHORS ChangeLog
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name_devel}
%doc README TODO
%{_includedir}/%{name}
%{_libdir}/*.so
