# revision 21641
# category Package
# catalog-ctan /macros/latex/contrib/postcards
# catalog-date 2009-01-23 15:11:09 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-postcards
Version:	20090123
Release:	1
Summary:	Facilitates mass-mailing of postcards (junkmail)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/postcards
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postcards.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/postcards.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A modification of the standard LaTeX letter class which prints
multiple, pre-stamped, 5.5" by 3.5" postcards (a US standard
size) via the envlab and mailing packages. An address database
is employed to address the front side of each postcard and a
message is printed on the back side of all. An illustrative
example is provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/postcards/postcards.cls
%doc %{_texmfdistdir}/doc/latex/postcards/README
%doc %{_texmfdistdir}/doc/latex/postcards/datasmp.txt
%doc %{_texmfdistdir}/doc/latex/postcards/pcardsmp.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
