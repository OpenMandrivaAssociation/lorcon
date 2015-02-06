%define	name	lorcon
%define version	0.0.20060625
%define release	10
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
mkdir -p \
	%{buildroot}/%{_includedir} \
	%{buildroot}/%{_libdir}
%makeinstall LIB=%{buildroot}/%{_libdir}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liborcon-%{major}.*.so

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/liborcon.a
%{_libdir}/liborcon.so


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.20060625-8mdv2011.0
+ Revision: 620257
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.20060625-7mdv2010.0
+ Revision: 429868
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.0.20060625-6mdv2009.0
+ Revision: 240258
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.0.20060625-5mdv2009.0
+ Revision: 239717
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Stefan van der Eijk <stefan@mandriva.org>
    - Import lorcon



* Mon Jun 26 2006 Pascal Terjan <pterjan@mandriva.org> 0.0.20060625-3mdv2007.0
- fix build on x86_64

* Sun Jun 25 2006 Stefan van der Eijk <stefan@eijk.nu> 0.0.20060625-2
- add %%post & %%postun

* Sun Jun 25 2006 Stefan van der Eijk <stefan@eijk.nu> 0.0.20060625-1
- initial package
