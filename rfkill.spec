Name:           rfkill
Version:        0.4
Release:        9%{?dist}
Summary:        A tool for enabling and disabling wireless devices

Group:          System Environment/Base
License:        ISC
URL:            http://www.linuxwireless.org/en/users/Documentation/rfkill
Source0:        http://wireless.kernel.org/download/rfkill/rfkill-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
rfkill is a simple tool for accessing the Linux rfkill device interface,
which is used to enable and disable wireless networking devices, typically
WLAN, Bluetooth and mobile broadband.

%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT} PREFIX='' MANDIR=%{_mandir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/sbin/rfkill
%{_mandir}/man8/*
%doc COPYING README


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.4-9
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4-8
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 25 2010 John W. Linville <linville@redhat.com> 0.4-3
- Use correct email address in changelog entries -- oops...

* Mon Feb 25 2010 John W. Linville <linville@redhat.com> 0.4-2
- Correct license tag from BSD to ISC

* Mon Feb  8 2010 John W. Linville <linville@redhat.com> 0.4-1
- Update to version 0.4

* Tue Sep 29 2009 John W. Linville <linville@redhat.com> 0.3-3
- Install binary into /sbin to enable use during boot

* Tue Sep 15 2009 John W. Linville <linville@redhat.com> 0.3-2
- Change summary and description as suggested by Tomasz Torcz <zdzichu@irc.pl>

* Thu Sep  3 2009 John W. Linville <linville@redhat.com> 0.3-1
- Update to upstream version 0.3
- Use 'make install' and include man page in files section

* Tue Aug 25 2009 John W. Linville <linville@redhat.com> 0.1-1
- Initial import
