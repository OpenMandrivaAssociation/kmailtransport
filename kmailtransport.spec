%define major 5
%define libname %mklibname KF5MailTransport %{major}
%define devname %mklibname KF5MailTransport -d

Name: kmailtransport
Version:	23.08.5
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	2
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for mail transport
URL: https://kde.org/
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
BuildRequires: cmake(KPim5SMTP)
BuildRequires: cmake(KPim5GAPI)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: boost-devel
BuildRequires: sasl-devel
Requires: akonadi-contacts
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
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
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/kmailtransport.categories
%{_datadir}/qlogging-categories5/kmailtransport.renamecategories
%{_libdir}/qt5/plugins/pim5/mailtransport
%{_datadir}/config.kcfg/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{qch,tags}
