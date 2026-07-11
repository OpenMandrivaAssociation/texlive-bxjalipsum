%global tl_name bxjalipsum
%global tl_revision 79277

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0b
Release:	%{tl_revision}.1
Summary:	Dummy text in Japanese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/BX/bxjalipsum
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjalipsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjalipsum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables users to print some Japanese text that can be used
as dummy text. It is a Japanese counterpart of the lipsum package. Since
there is no well-known nonsense text like Lipsum in the Japanese
language, the package uses some real text in public domain.

