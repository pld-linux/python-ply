
%define		module	ply

Summary:	Python Lex-Yacc
Summary(pl.UTF-8):   lex i yacc dla Pythona
Name:		python-%{module}
Version:	1.7
Release:	0.2
License:	LGPL
Group:		Libraries/Python
Source0:	http://www.dabeaz.com/ply/ply-%{version}.tar.gz
# Source0-md5:	95e1cc90132f7e9b7fe0877c922dd0b2
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
PLY to kolejna implementacja lex i yacc dla Pythona. Mimo iż istnieje
kilka innych narzędzi parsujących dla Pythona to istnieje kilka
powodów dla których powinieneś zainteresować się PLY:
- Używa parsowania-LR, które jest racjonalnie wydajne i dość dobre dla
  większych gramatyk.
- PLY dostarcza większość możliwości standardowego lex/yacc włączając
  w to wsparcie dla pustych produkcji, reguł poprzedzania,
  rekompensowania błędów oraz wsparcia dla dwuznacznych gramatyk.
- PLY jest niezwykle łatwy w użyciu oraz dostarcza szerokiej kontroli
  błędów.

%package examples
Summary:	Python Lex-Yacc - examples
Summary(pl.UTF-8):   lex i yacc dla Pythona - przykłady
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

%__python setup.py install --root $RPM_BUILD_ROOT --optimize 1
%py_postclean

cp -Rf example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO doc/*.html
%{py_sitescriptdir}/*.py[co]

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
