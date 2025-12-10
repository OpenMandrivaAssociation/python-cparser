%define oname pycparser
%define module cparser

Summary:	C parser in Python
Name:		python-%{module}
Version:	2.23
Release:	1
License:	BSD
Group:		Development/Python
Url:		https://github.com/eliben/pycparser
Source0:	https://github.com/eliben/pycparser/archive/refs/tags/release_v%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	python%{pyver}dist(ply)
BuildRequires:	dos2unix
Requires:	python%{pyver}dist(ply)
BuildArch:	noarch

%description
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library. It parses C code into an AST and can serve
as a front-end for C compilers or analysis tools.

%prep
%autosetup -n %{oname}-release_v%{version} -p1
dos2unix LICENSE

%build
%py_build

%install
%py_install -- --install-purelib=%{py_puresitedir}

%files
%doc CHANGES LICENSE README.rst
%{py_puresitedir}/pycparser
%{py_puresitedir}/pycparser*.egg-info
