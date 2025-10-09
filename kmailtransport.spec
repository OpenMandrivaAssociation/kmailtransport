#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6MailTransport
%define devname %mklibname KPim6MailTransport -d

Name: kmailtransport
Version:	25.08.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kmailtransport/-/archive/%{gitbranch}/kmailtransport-%{gitbranchd}.tar.bz2#/kmailtransport-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kmailtransport-%{version}.tar.xz
%endif
Summary: KDE library for mail transport
URL: https://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KPim6SMTP)
BuildRequires: cmake(KPim6GAPI)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: boost-devel
BuildRequires: sasl-devel
Requires: akonadi-contacts
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
BuildSystem: cmake
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
%rename plasma6-kmailtransport

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

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kmailtransport.categories
%{_datadir}/qlogging-categories6/kmailtransport.renamecategories
%{_libdir}/qt6/plugins/pim6/mailtransport
%{_datadir}/config.kcfg/*

%files -n %{libname}
%{_libdir}/*.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
