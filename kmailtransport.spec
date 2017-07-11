%define major 5
%define libname %mklibname KF5MailTransport %{major}
%define devname %mklibname KF5MailTransport -d

Name: kmailtransport
Version: 17.04.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release: 1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for mail transport
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5AkonadiMime)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Test)
BuildRequires: boost-devel
BuildRequires: sasl-devel
Requires: akonadi-contacts
Conflicts: kdepimlibs4-core < 4.14.10-6
Conflicts: kio-smtp < 3:16.04.3-2
Obsoletes: kio-smtp < 3:16.04.3-2
Provides: kio-smtp = 3:16.04.3-2

%description
KDE library for mail transport.

%package -n %{libname}
Summary: KDE library for mail transport
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for mail transport.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libmailtransport5
%find_lang kio_smtp
cat *.lang >%{name}.lang

%files -f %{name}.lang
%doc %{_docdir}/HTML/en/kioslave5/smtp/index.*
%{_sysconfdir}/xdg/kmailtransport.categories
%{_sysconfdir}/xdg/kmailtransport.renamecategories
%{_libdir}/qt5/plugins/kf5/kio/smtp.so
%{_libdir}/qt5/plugins/kcm_mailtransport.so
%{_datadir}/config.kcfg/*
%{_datadir}/kservices5/kcm_mailtransport.desktop
%{_datadir}/kservices5/*.protocol
%lang(ca) %{_docdir}/HTML/ca/kioslave5/smtp
%lang(de) %{_docdir}/HTML/de/kioslave5/smtp
%lang(es) %{_docdir}/HTML/es/kioslave5/smtp
%lang(et) %{_docdir}/HTML/et/kioslave5/smtp
%lang(it) %{_docdir}/HTML/it/kioslave5/smtp
%lang(nl) %{_docdir}/HTML/nl/kioslave5/smtp
%lang(pt_BR) %{_docdir}/HTML/pt_BR/kioslave5/smtp
%lang(ru) %{_docdir}/HTML/ru/kioslave5/smtp
%lang(sr) %{_docdir}/HTML/sr/kioslave5/smtp
%lang(sv) %{_docdir}/HTML/sv/kioslave5/smtp
%lang(uk) %{_docdir}/HTML/uk/kioslave5/smtp

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
