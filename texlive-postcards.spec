Name:		texlive-postcards
Version:	21641
Release:	2
Summary:	Facilitates mass-mailing of postcards (junkmail)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/postcards
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postcards.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postcards.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A modification of the standard LaTeX letter class which prints
multiple, pre-stamped, 5.5" by 3.5" postcards (a US standard
size) via the envlab and mailing packages. An address database
is employed to address the front side of each postcard and a
message is printed on the back side of all. An illustrative
example is provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/postcards/postcards.cls
%doc %{_texmfdistdir}/doc/latex/postcards/README
%doc %{_texmfdistdir}/doc/latex/postcards/datasmp.txt
%doc %{_texmfdistdir}/doc/latex/postcards/pcardsmp.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
