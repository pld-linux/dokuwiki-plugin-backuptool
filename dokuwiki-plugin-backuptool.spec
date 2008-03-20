%define		_plugin		backuptool
Summary:	DokuWiki Backup Tool Plugin
Summary(pl.UTF-8):	Wtyczka Backup Tool dla DokuWiki
Name:		dokuwiki-plugin-%{_plugin}
Version:	20070405
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://tatewake.com/wiki/_media/projects:backuptool-04052007.zip
# Source0-md5:	b2c33a5243b7d46705e4720012f05f34
Source1:	dokuwiki-find-lang.sh
URL:		http://tatewake.com/wiki/projects:backuptool_for_dokuwiki
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{_plugin}

%description
This is a plugin for DokuWiki which enables you to backup the most
important parts of your site; this includes all of your pages, all old
revisions, meta data, subscriptions, media files (your downloads), as
well as your plugins and templates.

This is in case, for some odd reason, your host accidentally loses all
your files; its happened to me personally twice, on two different
hosts since I began using DokuWiki– and backing up manually can be
quite a nightmare.

%description -l pl.UTF-8
Jest to plugin dla DokuWiki, który pozwala na archiwizacje
najważniejszych danych ze strony.

%prep
%setup -q -n backup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_plugindir}
%{_plugindir}/*.php
