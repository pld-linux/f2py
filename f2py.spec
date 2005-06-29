%define	module	f2py2e
Summary:	Fortran to Python interface generator
Summary(pl):	Oprogramowanie do robienia kopii zapasowych
Name:		f2py
Version:	2.45.241_1926
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://cens.ioc.ee/projects/f2py2e/2.x/F2PY-%{version}.tar.gz
# Source0-md5:	8aedac9cad32afdcddcfb026b6393ece
URL:		http://cens.ioc.ee/projects/f2py2e/
%pyrequires_eq  python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortran to Python interface generator.

%prep
%setup -q -n F2PY-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}