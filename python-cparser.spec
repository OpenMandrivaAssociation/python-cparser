%define oname pycparser
%define module cparser

Summary:	C parser in Python
Name:		python-%{module}
Version:	2.18
Release:	3
License:	BSD
Group:		Development/Python
Url:		https://github.com/eliben/pycparser
Source0:	https://github.com/eliben/pycparser/archive/release_v%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python2-setuptools
BuildRequires:	python2dist(ply)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python3dist(ply)
Requires:	python3dist(ply)
BuildArch:	noarch

%description
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library. It parses C code into an AST and can serve
as a front-end for C compilers or analysis tools.

%files
%doc CHANGES LICENSE README.rst
%{py_puresitedir}/pycparser
%{py_puresitedir}/pycparser*.egg-info

#----------------------------------------------------------------------------

%package -n python2-%{module}
Summary:	C parser in Python 2
Group:		Development/Python
Requires:	python2dist(ply)

%description -n python2-%{module}
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library. It parses C code into an AST and can serve
as a front-end for C compilers or analysis tools.

%files -n python2-%{module}
%doc CHANGES LICENSE README.rst
%{py2_puresitedir}/pycparser
%{py2_puresitedir}/pycparser*.egg-info

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-release_v%{version}
perl -i -pe 's/\r\n/\n/gs' LICENSE

cp -a . %{py2dir}

%build
pushd %{py2dir}
%{__python2} setup.py build
popd

%{__python} setup.py build

%install
pushd %{py2dir}
%{__python2} setup.py install --root=%{buildroot} --install-purelib=%{py2_puresitedir}
popd

%{__python} setup.py install --root=%{buildroot} --install-purelib=%{py_puresitedir}
