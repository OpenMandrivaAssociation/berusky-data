%define oname berusky

Name:		%{oname}-data
Version:	1.4
Release:	%mkrel 1
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

