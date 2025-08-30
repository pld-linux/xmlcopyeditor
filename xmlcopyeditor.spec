Summary:	Fast, free, validating XML editor
Summary(pl.UTF-8):	Szybkim, wolnodostępnym, walidującym edytorem XML
Name:		xmlcopyeditor
Version:	1.3.1.0
Release:	4
License:	GPL v2
Group:		Applications/Text
Source0:	https://downloads.sourceforge.net/xml-copy-editor/%{name}-%{version}.tar.gz
# Source0-md5:	3e515b07a9f3c3c73f03c43cbb8719cd
Patch0:		%{name}-types.patch
URL:		https://sourceforge.net/projects/xml-copy-editor/
BuildRequires:	boost-devel
BuildRequires:	enchant2-devel >= 2
BuildRequires:	expat-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	pcre2-8-devel
BuildRequires:	wxGTK3-unicode-devel >= 2.8.0
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML Copy Editor is a fast, free, validating XML editor

%description -l pl.UTF-8
XML Copy Editor jest szybkim, wolnodostępnym, walidującym edytorem
XML.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	--with-wx-config=%{_bindir}/wx-gtk3-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{uk_UA,uk}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/xmlcopyeditor
%{_datadir}/%{name}
%{_desktopdir}/xmlcopyeditor.desktop
%{_pixmapsdir}/xmlcopyeditor.png
%{_datadir}/metainfo/xmlcopyeditor.appdata.xml
%{_mandir}/man1/xmlcopyeditor.1*
