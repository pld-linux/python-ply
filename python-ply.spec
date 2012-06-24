%include	/usr/lib/rpm/macros.python

%define		module	ply

Summary:	Python Lex-Yacc
Summary(pl):	Python IRC library
Name:		python-%{module}
Version:	1.3.1
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://systems.cs.uchicago.edu/ply/ply-%{version}.tar.gz
# Source0-md5:	eeb11347ef861d3ec9469f072beeaeb1
URL:		http://systems.cs.uchicago.edu/ply/
BuildRequires:	rpm-pythonprov >= 4.0.2-50
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

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


%description -l pl
PLY to kolejna implementacja lex i yacc dla Pythona. Mimo i� istnieje
kilka innych narz�dzi parsuj�cych dla Pythona to istnieje kilka
powod�w dla kt�rych powiniene� zainteresowa� si� PLY:
- U�ywa parsowania-LR, kt�re jest racjonalnie wydajne i do�� dobre dla
  wi�kszych gramatyk.
- PLY dostarcza wi�kszo�� mo�liwo�ci standardowego lex/yacc w��czaj�c
  w to wsparcie dla pustych produkcji, regu� poprzedzania,
  rekompensowania b��d�w oraz wsparcia dla dwuznacznych gramatyk.
- PLY jest niezwykle ��twy w u�yciu oraz dostarcza szerokiej kontroli
  b��d�w.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

install *.py $RPM_BUILD_ROOT%{py_sitedir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO doc/*.html
%{py_sitedir}/*.py[co]
