%define oname berusky

Name:		%{oname}-data
Version:	1.7
Release:	1
Summary:	Game data files for Berusky
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://www.anakreon.cz/
Source0:	http://anakreon.cz/download/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
A datafile for Berusky. Berusky is a 2D logic game based on an ancient
puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic
items such as explosives, stones, special gates and so on.
In addition, up to five bugs can cooperate and be controlled by the player.

This package contains a data for the game, i.e. files with graphics, levels,
game rules and configuration.


%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_gamesdatadir}/%{oname}

cp -p -R GameData %{buildroot}%{_gamesdatadir}/%{oname}
cp -p -R Graphics %{buildroot}%{_gamesdatadir}/%{oname}
cp -p -R Levels   %{buildroot}%{_gamesdatadir}/%{oname}

# berusky.ini is installed from the berusky package

%clean
%__rm -rf %{buildroot}

%files
%doc README COPYING
%{_gamesdatadir}/%{oname}/*



%changelog
* Tue May 01 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4-1
+ Revision: 794784
- imported package berusky-data


* Tue May 01 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4-1mdv2010.2
- Import from Mageia
- New version 1.4

* Tue Jan 31 2012 kamil <kamil> 1.0-11.mga2
+ Revision: 203632
- don't own berusky-data_directory
- don't install berusky.ini from this package, it's in berusky

* Mon Jan 30 2012 kamil <kamil> 1.0-10.mga2
+ Revision: 203341
- adapt .spec for Mageia
- imported package berusky-data


* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 19 2009 Martin Stransky <stransky@redhat.com> 1.0-7
- fixed licence & #473628

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-4
- fix license tag

* Tue May 8 2007 Martin Stransky <stransky@redhat.com> 1.0-3
- added build section

* Mon Apr 23 2007 Martin Stransky <stransky@redhat.com> 1.0-2
- fixes from #237416

* Fri Apr 20 2007 Martin Stransky <stransky@redhat.com> 1.0-1
- initial build

