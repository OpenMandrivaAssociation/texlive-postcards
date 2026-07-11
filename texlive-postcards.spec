%global tl_name postcards
%global tl_revision 75878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Facilitates mass-mailing of postcards (junkmail)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/postcards
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/postcards.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/postcards.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A modification of the standard LaTeX letter class which prints multiple,
pre-stamped, 5.5'' by 3.5'' postcards (a US standard size) via the
envlab and mailing packages. An address database is employed to address
the front side of each postcard and a message is printed on the back
side of all. An illustrative example is provided.

