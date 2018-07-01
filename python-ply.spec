#
# Conditional build:
%bcond_without  tests   # do not perform "make test"
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module
#
%define		module	ply
Summary:	Python 2 Lex-Yacc
Summary(pl.UTF-8):	lex i yacc dla Pythona 2
Name:		python-%{module}
Version:	3.10
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	http://www.dabeaz.com/ply/ply-%{version}.tar.gz
# Source0-md5:	1d63c166ab250bab87d8dcc42dcca70e
URL:		http://www.dabeaz.com/ply/
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python3}
BuildRequires:	python >= 2.2.1
%if %{with tests}
BuildRequires:	python-setuptools
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
%if %{with tests}
BuildRequires:	python3-setuptools
%endif
%endif
Requires:	python-modules
Obsoletes:	ply
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLY is yet another implementation of lex and yacc for Python. Although
several other parsing tools are available for Python, there are
several reasons why you might want to take a look at PLY:
- It uses LR-parsing which is reasonably efficient and well suited for
  larger grammars.
- PLY provides most of the standard lex/yacc features including
  support for empty productions, precedence rules, error recovery, and
  support for ambiguous grammars.
- PLY is extremely easy to use and provides very extensive error
  checking.

%description -l pl.UTF-8
PLY to kolejna implementacja narzędzi lex i yacc dla Pythona. Mimo iż
istnieje kilka innych analizatorów dla Pythona, to istnieje kilka
powodów, dla których można zainteresować się PLY:
- Używa on analizy LR, która jest w miarę wydajna i dość dobra dla
  większych gramatyk.
- Udostępnia większość możliwości standardowych lex/yacc, w tym
  obsługę pustych produkcji, reguł poprzedzania, rekompensowania błędów
  oraz obsługę niejednoznacznych gramatyk.
- Jest niezwykle łatwy w użyciu oraz zapewnia rozległą kontrolę
  błędów.

%package -n python3-%{module}
Summary:	Python 3 Lex-Yacc
Summary(pl.UTF-8):	lex i yacc dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
PLY is yet another implementation of lex and yacc for Python. Although
several other parsing tools are available for Python, there are
several reasons why you might want to take a look at PLY:
- It uses LR-parsing which is reasonably efficient and well suited for
  larger grammars.
- PLY provides most of the standard lex/yacc features including
  support for empty productions, precedence rules, error recovery, and
  support for ambiguous grammars.
- PLY is extremely easy to use and provides very extensive error
  checking.

%description -n python3-%{module} -l pl.UTF-8
PLY to kolejna implementacja narzędzi lex i yacc dla Pythona. Mimo iż
istnieje kilka innych analizatorów dla Pythona, to istnieje kilka
powodów, dla których można zainteresować się PLY:
- Używa on analizy LR, która jest w miarę wydajna i dość dobra dla
  większych gramatyk.
- Udostępnia większość możliwości standardowych lex/yacc, w tym
  obsługę pustych produkcji, reguł poprzedzania, rekompensowania błędów
  oraz obsługę niejednoznacznych gramatyk.
- Jest niezwykle łatwy w użyciu oraz zapewnia rozległą kontrolę
  błędów.

%package examples
Summary:	Python Lex-Yacc - examples
Summary(pl.UTF-8):	lex i yacc dla Pythona - przykłady
Group:		Development/Languages/Python

%description examples
Python Lex-Yacc - examples.

%description examples -l pl.UTF-8
lex i yacc dla Pythona - przykłady.

%prep
%setup -q -n %{module}-%{version}

%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with python2}
%py_install
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

cp -Rf example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README.md TODO doc/*.html
%dir %{py_sitescriptdir}/ply
%{py_sitescriptdir}/ply/*.py[co]
%if "%{py_ver}" >= "2.5"
%{py_sitescriptdir}/ply-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README.md TODO doc/*.html
%{py3_sitescriptdir}/ply
%{py3_sitescriptdir}/ply-%{version}-py*.egg-info
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
