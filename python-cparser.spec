%define oname pycparser
%define module cparser

Summary:	C parser in Python
Name:		python-%{module}
Version:	2.14
Release:	2
License:	BSD
Group:		Development/Python
Url:		https://github.com/eliben/pycparser
Source0:	http://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python2-setuptools

BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library. It parses C code into an AST and can serve
as a front-end for C compilers or analysis tools.

%files
%doc CHANGES LICENSE README.rst
%{py_puresitedir}/pycparser/*.py*
%{py_puresitedir}/pycparser/ply/*.py*
%{py_puresitedir}/pycparser*.egg-info
%{py_puresitedir}/pycparser/_c_ast.cfg

#----------------------------------------------------------------------------

%package -n python2-%{module}
Summary:	C parser in Python 2
Group:		Development/Python

%description -n python2-%{module}
pycparser is a complete parser of the C language, written in pure Python
using the PLY parsing library. It parses C code into an AST and can serve
as a front-end for C compilers or analysis tools.

%files -n python2-%{module}
%doc CHANGES LICENSE README.rst
%{py2_puresitedir}/pycparser/*.py*
%{py2_puresitedir}/pycparser/ply/*.py*
%{py2_puresitedir}/pycparser*.egg-info
%{py2_puresitedir}/pycparser/_c_ast.cfg

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
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
