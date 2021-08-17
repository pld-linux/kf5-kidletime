%define		kdeframever	5.85
%define		qtver		5.9.0
%define		kfname		kidletime

Summary:	Reporting of idle time of user and system
Name:		kf5-%{kfname}
Version:	5.85.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	58a3e469ac54cb78469b27f216c87c0a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KIdleTime is a singleton reporting information on idle time. It is
useful not only for finding out about the current idle time of the PC,
but also for getting notified upon idle time events, such as custom
timeouts, or user activity.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/qlogging-categories5/kidletime.categories
%ghost %{_libdir}/libKF5IdleTime.so.5
%attr(755,root,root) %{_libdir}/libKF5IdleTime.so.*.*
%dir %{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin0.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin1.so
%{_datadir}/qlogging-categories5/kidletime.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KIdleTime
%{_includedir}/KF5/kidletime_version.h
%{_libdir}/cmake/KF5IdleTime
%{_libdir}/libKF5IdleTime.so
%{qt5dir}/mkspecs/modules/qt_KIdleTime.pri
