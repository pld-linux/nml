Summary:	convert meta-languate to openttd's grf and/or nfo files
Name:		nml
Version:	0.2.1
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://bundles.openttdcoop.org/nml/releases/0.2.1/%{name}-%{version}.src.tar.gz
# Source0-md5:	a19adeaa584c1f9798d7d0da0f2ac316
URL:		https://dev.openttdcoop.org/projects/nml
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	python-ply
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to convert a meta-language to grf and/or nfo files, making
newgrf coding easier.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/nml
%{py_sitescriptdir}/nml-%{version}*.egg-info
