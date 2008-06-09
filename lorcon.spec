%define	name	lorcon
%define version	0.0.20060625
%define	release	%mkrel 3
%define major	1
%define libname	%mklibname %{name} %{major}

Summary:	A generic library for injecting 802.11 frames
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		http://802.11ninja.net/
Source:		http://802.11ninja.net/code/%{name}-current.tar.bz2
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Lorcon is a generic library for injecting 802.11 frames, capable of injection
via multiple driver frameworks, with out forcing modification of the
application code.

%package -n %{libname}
Summary: Main library for %{name}
Group: System/Libraries
Provides: lib%{name} = %{version}-%{release}
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{libname}-devel
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel  = %{version}-%{release}
Requires: %{libname} = %{version}

%description -n %{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n %{name}

%build
%make

%install
rm -rf %{buildroot}
mkdir -p \
	$RPM_BUILD_ROOT/%{_includedir} \
	$RPM_BUILD_ROOT/%{_libdir}
%makeinstall LIB=$RPM_BUILD_ROOT/%{_libdir}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liborcon-%{major}.*.so

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/liborcon.a
%{_libdir}/liborcon.la
%{_libdir}/liborcon.so
