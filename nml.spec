Summary:	convert meta-languate to openttd's grf and/or nfo files
Name:		nml
Version:	0.7.6
Release:	2
License:	GPL v2
Group:		Applications
Source0:	https://github.com/OpenTTD/nml/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fd26c9d416f3ceaa481fa293c190520b
URL:		https://dev.openttdcoop.org/projects/nml
BuildRequires:	python3-pillow
BuildRequires:	python3-ply
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	python3-pillow
Requires:	python3-ply
Requires:	python3-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to convert a meta-language to grf and/or nfo files, making
newgrf coding easier.

%prep
%setup -q

%build
%{__make} -j1
%{__make} -j1 extensions

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} setup.py install \
	--skip-build \
	--optimize=2 \
	--prefix=%{_prefix} \
	--root=$RPM_BUILD_ROOT
install -D docs/nmlc.1 $RPM_BUILD_ROOT%{_mandir}/man1/nmlc.1

# The actual python code is not being installed?!?
install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}/nml
cp -rp nml/* $RPM_BUILD_ROOT%{py3_sitescriptdir}/nml/

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmlc
%doc docs/*.txt
%{_mandir}/man1/nmlc.1*
%{py3_sitedir}/*
%{py3_sitescriptdir}/%{name}/
