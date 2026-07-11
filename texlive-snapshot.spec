%global tl_name snapshot
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.14
Release:	%{tl_revision}.1
Summary:	List the external dependencies of a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/snapshot
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/snapshot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/snapshot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/snapshot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The snapshot package helps the owner of a LaTeX document obtain a list
of the external dependencies of the document, in a form that can be
embedded at the top of the document. It provides a snapshot of the
current processing context of the document, insofar as it can be
determined from inside LaTeX. If a document contains such a dependency
list, then it becomes possible to arrange that the document be processed
always with the same versions of everything, in order to ensure the same
output. This could be useful for someone wanting to keep a LaTeX
document on hand and consistently reproduce an identical DVI file from
it, on the fly; or for someone wanting to shield a document during the
final stages of its production cycle from unexpected side effects of
routine upgrades to the TeX system.

