Name:		texlive-bxjalipsum
Version:	43369
Release:	1
Summary:	Dummy text in Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxjalipsum
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjalipsum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjalipsum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables users to print some Japanese text that can
be used as dummy text. It is a Japanese counterpart of the
lipsum package. Since there is no well-known nonsense text like
Lipsum in the Japanese language, the package uses some real
text in public domain.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxjalipsum
%doc %{_texmfdistdir}/doc/latex/bxjalipsum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
