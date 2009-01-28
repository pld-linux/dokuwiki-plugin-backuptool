%define		_plugin		backuptool
Summary:	DokuWiki Backup Tool Plugin
Summary(pl.UTF-8):	Wtyczka Backup Tool dla DokuWiki
Name:		dokuwiki-plugin-%{_plugin}
Version:	20080824
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://tatewake.com/wiki/_media/projects:backuptool-%{version}.tar.gz
# Source0-md5:	f98defc3c5f3613750868edc1c297f0e
Source1:	dokuwiki-find-lang.sh
URL:		http://tatewake.com/wiki/projects:backuptool_for_dokuwiki
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{_plugin}

%description
This is a plugin for DokuWiki which enables you to backup the most
important parts of your site; this includes all of your pages, all old
revisions, meta data, subscriptions, media files (your downloads), as
well as your plugins and templates.

This is in case, for some odd reason, your host accidentally loses all
your files.

%description -l pl.UTF-8
Jest to plugin dla DokuWiki, który pozwala na archiwizacje
najważniejszych danych ze strony.

%prep
%setup -q -n backup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
