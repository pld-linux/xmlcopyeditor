Summary:	Fast, free, validating XML editor
Summary(pl.UTF-8):	Szybkim, wolnodostępnym, walidującym edytorem XML
Name:		xmlcopyeditor
Version:	1.3.1.0
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/xml-copy-editor/%{name}-%{version}.tar.gz
# Source0-md5:	3e515b07a9f3c3c73f03c43cbb8719cd
URL:		https://sourceforge.net/projects/xml-copy-editor/
BuildRequires:	aspell-devel
BuildRequires:	boost-devel
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxslt-devel
BuildRequires:	pcre-devel
BuildRequires:	wxGTK3-unicode-devel
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML Copy Editor is a fast, free, validating XML editor

%description -l pl.UTF-8
XML Copy Editor jest szybkim, wolnodostępnym, walidującym edytorem
XML.

%prep
%setup -q

%build
%configure \
	--with-wx-config=%{_bindir}/wx-gtk3-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/metainfo/xmlcopyeditor.appdata.xml
%{_mandir}/man1/xmlcopyeditor.1*
