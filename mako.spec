Summary:	A lightweight Wayland notification daemon
Name:		mako
Version:	1.10.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/emersion/mako/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6162235130fa4cb1ea4b01bc1f96f651
URL:		https://wayland.emersion.fr/mako/
BuildRequires:	bash-completion-devel >= 1:2.0
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc >= 1.9.7
BuildRequires:	systemd-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mako is a lightweight notification daemon for Wayland compositors that
support the layer-shell protocol.

%package -n bash-completion-mako
Summary:	bash-completion for mako
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-mako
This package provides bash-completion for mako.

%package -n zsh-completion-mako
Summary:	ZSH completion for mako
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-mako
ZSH completion for mako.

%prep
%setup -q

%build
%meson \
	-Dbash-completions=true \
	-Dzsh-completions=true
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/mako
%attr(755,root,root) %{_bindir}/makoctl
%{_datadir}/dbus-1/services/fr.emersion.mako.service
%{_mandir}/man1/mako.1*
%{_mandir}/man1/makoctl.1*
%{_mandir}/man5/mako.5*

%files -n bash-completion-mako
%defattr(644,root,root,755)
%{bash_compdir}/mako
%{bash_compdir}/makoctl

%files -n zsh-completion-mako
%defattr(644,root,root,755)
%{zsh_compdir}/_mako
%{zsh_compdir}/_makoctl
