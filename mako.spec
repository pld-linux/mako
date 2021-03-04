Summary:	A lightweight Wayland notification daemon
Name:		mako
Version:	1.4.1
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/emersion/mako/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1da0e274b25e61d0f8ce956270f3f737
URL:		https://wayland.emersion.fr/mako/
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja
BuildRequires:	pango-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	systemd-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mako is a lightweight notification daemon for Wayland compositors that
support the layer-shell protocol.

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
%meson build \
	-Dzsh-completions=true
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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

%files -n zsh-completion-mako
%defattr(644,root,root,755)
%{zsh_compdir}/_mako
%{zsh_compdir}/_makoctl
