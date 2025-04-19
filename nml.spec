#
# Conditional build:
%bcond_without	tests	# regression tests

Summary:	Convert meta-language to openttd's grf and/or nfo files
Summary(pl.UTF-8):	Konwersja meta-języka do plików grf i/lub nfo dla openttd
Name:		nml
Version:	0.7.6
Release:	4
License:	GPL v2
Group:		Applications
Source0:	https://github.com/OpenTTD/nml/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fd26c9d416f3ceaa481fa293c190520b
URL:		https://dev.openttdcoop.org/projects/nml
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-pillow >= 3.4
BuildRequires:	python3-ply
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to convert a meta-language to grf and/or nfo files, making
newgrf coding easier.

%description -l pl.UTF_8
Narzędzie do konwersji meta-języka do plików grf i/lub nfo, dzięki
czemu kodowanie newgrf staje się prostsze.

%prep
%setup -q

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__make} -C regression -j1
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -D docs/nmlc.1 $RPM_BUILD_ROOT%{_mandir}/man1/nmlc.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md docs/changelog.txt docs/index.html
%attr(755,root,root) %{_bindir}/nmlc
%{_mandir}/man1/nmlc.1*
%attr(755,root,root) %{py3_sitedir}/nml_lz77.cpython-*.so
%{py3_sitedir}/nml
%{py3_sitedir}/nml-%{version}-py*.egg-info
