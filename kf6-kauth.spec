%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6Auth
%define devname %mklibname KF6Auth -d
#define git 20240217

Name: kf6-kauth
Version: 6.0.0
Release: %{?git:0.%{git}.}2
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kauth/-/archive/master/kauth-master.tar.bz2#/kauth-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{version}/kauth-%{version}.tar.xz
%endif
Summary: Execute actions as privileged user
URL: https://invent.kde.org/frameworks/kauth
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: polkit-qt6-1-devel
Requires: %{libname} = %{EVRD}

%description
Execute actions as privileged user

%package -n %{libname}
Summary: Execute actions as privileged user
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Execute actions as privileged user

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Execute actions as privileged user

%prep
%autosetup -p1 -n kauth-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kauth.*
%{_datadir}/dbus-1/system.d/org.kde.kf6auth.conf
%{_datadir}/kf6/kauth
%{_libdir}/libexec/kf6/kauth

%files -n %{devname}
%{_includedir}/KF6/KAuth
%{_includedir}/KF6/KAuthCore
%{_libdir}/cmake/KF6Auth
%{_qtdir}/doc/KF6Auth.*

%files -n %{libname}
%{_libdir}/libKF6AuthCore.so*
%{_qtdir}/plugins/kf6/kauth
