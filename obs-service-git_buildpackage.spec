#
# spec file for package obs-service-git_buildpackage
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           obs-service-git_buildpackage
Summary:        An OBS source service: Create Debian source package from GIT
License:        GPL-2.0+
Group:          Development/Tools/Building
Version:        1.1
Release:        0
Source:         %{name}-%{version}.tar.gz
Requires:       sed
Requires:       gawk
Requires:       git-buildpackage
Requires:       fakeroot
Requires:       devscripts
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

Very simply script to update the version in .spec or .dsc files according to
a given version or to the existing files.

%prep
%setup -q -n obs-service-git_buildpackage-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/obs/service
install -m 0755 git_buildpackage $RPM_BUILD_ROOT/usr/lib/obs/service
install -m 0644 git_buildpackage.service $RPM_BUILD_ROOT/usr/lib/obs/service

%files
%defattr(-,root,root)
%dir /usr/lib/obs
/usr/lib/obs/service

%changelog
