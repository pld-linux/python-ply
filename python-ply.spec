%define		module	ply
Summary:	Python Lex-Yacc
Summary(pl.UTF-8):	lex i yacc dla Pythona
Name:		python-%{module}
Version:	3.4
Release:	4
License:	BSD
Group:		Libraries/Python
Source0:	http://www.dabeaz.com/ply/ply-%{version}.tar.gz
# Source0-md5:	ffdc95858819347bf92d7c2acc074894
URL:		http://www.dabeaz.com/ply/
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python
Obsoletes:	%{module}
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install \
	 --root $RPM_BUILD_ROOT \
	 --optimize=2
%py_postclean

cp -Rf example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README TODO doc/*.html
%dir %{py_sitescriptdir}/ply
%{py_sitescriptdir}/ply/*.py[co]
%if "%{py_ver}" >= "2.5"
%{py_sitescriptdir}/ply-%{version}-py*.egg-info
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
