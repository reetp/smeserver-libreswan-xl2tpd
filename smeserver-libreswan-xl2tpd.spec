%define name smeserver-libreswan-xl2tpd
%define version 0.5
%define release 8
Summary: Plugin to enable LT2P/IPSEC connections
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU GPL version 2
URL: https://www.libreswan.org/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
Patch1: smeserver-libreswan-xl2tpd-private-access.patch
Patch2: smeserver-libreswan-xl2tpd-update-variables.patch
Patch3: smeserver-libreswan-xl2tpd-cleanup-obsoletes.patch
Patch4: smeserver-libreswan-xl2tpd-update-status-default
Patch5: smeserver-libreswan-xl2tpd-update-ip-up-local.patch
Patch6: smeserver-libreswan-xl2tpd-update-createlinks.patch

BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 9.2
Requires:  libreswan >= 3.29
Requires:  smeserver-libreswan >= 0.5
Requires:  xl2tpd >= 1.3.15
AutoReqProv: no

%description
xl2tpd is an implementation of the Layer 2 Tunnelling Protocol (RFC 2661). L2TP allows you to tunnel PPP over UDP

%changelog
* Tue Feb 14 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-8.sme
- Update for xl2tpd 1.3.15
- Update createlinks to regenerate masq on connection
- Modify Nat/non Nat sections
- remove rightsubnet as normal configuration item
- set IKE v1 only and other updates to ipsec.conf
- update file layouts to match samples
- load pppol2tp on startup if xl2tpd is enabled
- Bump requires to newer xl2tpd

* Thu Jan 30 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-7
- Update ip-up.local to add debug and enhance setting
- update ipsec.conf to for NAT/noNAT
- add $mtu key - defaults to 1400

* Tue Sep 03 2019 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-6
- Add ipsec connection status key (disabled as default)
- Update Libreswan depends
- Add ikev2 permit to allow ike v1

* Thu Jun 21 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-5
- Fix obsolete forecencaps
- Update required Libreswan version

* Thu Nov 30 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-4
 - template cleanup pending - not yet committed to CVS but in git

* Wed Nov 29 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-3
- remove unneeded default right subnet setting to clear error
- added variables for leftsourceip and leftsubnet if required

* Wed Nov 29 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-2
- add xl2tpd access private as default

* Fri Nov 24 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-1
- First import to contribs

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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
