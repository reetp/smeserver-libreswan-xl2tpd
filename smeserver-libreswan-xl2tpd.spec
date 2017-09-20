%define name smeserver-libreswan-xl2tpd
%define version 0.2
%define release 4
Summary: Plugin to enable LT2P/IPSEC connections
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU GPL version 2
URL: http://libreswan.org/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 9.2
Requires:  libreswan >= 3.16
Requires:  smeserver-libreswan >= 0.5
Requires:  xl2tpd >= 1.3.8
AutoReqProv: no

%description
xl2tpd is an implementation of the Layer 2 Tunnelling Protocol (RFC 2661). L2TP allows you to tunnel PPP over UDP

%changelog
* Wed Sep 20 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-4
- Fix typo error in ipsec.secrets

* Wed Sep 20 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-3
- Modified client authent to work with existing VPN Client Access via Server Manager

* Mon Jul 31 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-2
- Modify rightsubnet

* Wed Jun 14 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-1
- New v 0.2 release

* Wed Jun 14 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-15
- template masq fragment

* Mon Jun 12 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-14
- Big reformat of code to disable templates when items are disabled
- Remove service link in spec as xl2tpd will need starting via ipsec-update

* Fri Jun 09 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-13
- add options to /etc/ppp/options.xl2tpd

* Thu Jun 08 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-12
- Fix more templates

+* Wed Jun 07 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-11
+- Fix various templates

* Thu Jun 1 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-10
- Update notes
- Note SME bugs: 8890,8891,8897
- Fix mistakes in createlinks file
- Add event link

* Wed Nov 18 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-9
- Add UDP DB variable and modify masq temnplate

* Mon Jun 29 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-8
- Remove Incorrect template file from /etc/ip-up.local

* Wed Apr 08 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-6
- Add ip-up.local template - variosu other mods

* Tue Mar 24 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-5
- Few more mods to syntax - this appears to work

* Thu Mar 19 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-4
- Escape quotes in template
- Remove comments from db

* Thu Mar 5 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-3
- Amend firewall fragment

* Tue Mar 3 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-2
- More of code tidying

* Fri Feb 15 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-1
- initial release

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist


%clean
cd ..
rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre
%preun
%post
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q

%postun
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q
