# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/snapshot
# catalog-date 2006-12-14 00:03:18 +0100
# catalog-license lppl
# catalog-version 1.14
Name:		texlive-snapshot
Version:	1.14
Release:	12
Summary:	List the external dependencies of a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/snapshot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/snapshot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/snapshot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/snapshot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The snapshot package helps the owner of a LaTeX document obtain
a list of the external dependencies of the document, in a form
that can be embedded at the top of the document. It provides a
snapshot of the current processing context of the document,
insofar as it can be determined from inside LaTeX. If a
document contains such a dependency list, then it becomes
possible to arrange that the document be processed always with
the same versions of everything, in order to ensure the same
output. This could be useful for someone wanting to keep a
LaTeX document on hand and consistently reproduce an identical
DVI file from it, on the fly; or for someone wanting to shield
a document during the final stages of its production cycle from
unexpected side effects of routine upgrades to the TeX system.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/snapshot/snapshot.sty
%doc %{_texmfdistdir}/doc/latex/snapshot/snapshot.pdf
#- source
%doc %{_texmfdistdir}/source/latex/snapshot/snapshot.dtx
%doc %{_texmfdistdir}/source/latex/snapshot/snapshot.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.14-2
+ Revision: 756072
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.14-1
+ Revision: 719554
- texlive-snapshot
- texlive-snapshot
- texlive-snapshot
- texlive-snapshot

