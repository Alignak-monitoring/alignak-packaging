%global alignak_user alignak
%global alignak_group alignak

Summary:        Python Monitoring tool
Name:           alignak
Version:        0.2
Release:        1
URL:            https://github.com/Alignak-monitoring/alignak 
Source0:        %{name}-%{version}.tar.gz
License:        AGPLv3

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

Group:          Application/System


%description
Alignak is a new monitoring tool written in Python.
The main goal of Alignak is to allow users to have a fully flexible
architecture for their monitoring system that can easily scale to large
environments.
Alignak has several extensions to enrich its standard features:
 - a full REST backend that allows to store the monitoring configuration and the live state
 - a Web User interface to view and edit the monitored objects
 - modules to extend the basic monitoring features: external commands, logs, ...
 - checks packages to easily set-up new monitoring objects

%package all
Summary: Alignak Common files
Group:          Application/System
Requires:       python >= 2.6
Requires:       python-cherrypy
Requires:       python-requests >= 2.7.0
Requires:       python-termcolor
Requires:       python-setproctitle
Requires:       numpy
Requires:       pyOpenSSL >= 0.15
#Requires:       python-ujson


%description all
Common files for alignak monitoring



%prep
%setup -qn %{name}

# Apply all patches
# TODO check patch from shinken packaging
#for patch_file in $(cat debian/patches/series | grep -v "^#")
#do
#%{__patch} -p1 < debian/patches/$patch_file
#done


%build
# Does not work on centos7
#%{py_build}
 
%install

# See if we want usr/bin or usr/sbin for bin : --install-scripts=%{_sbindir}
%{__python} setup.py install -O1 --root=%{buildroot} --install-lib=%{python_sitelib}

install -d -m0755  %{buildroot}%{_sysconfdir}/%{name}/
rm -rf %{buildroot}%{_sysconfdir}/%{name}/*

# Remove generated conf
rm -rf %{buildroot}/usr/etc/%{name}/*
rm -rf %{buildroot}/usr/etc/default/%{name}

# Copy original file but remove sample
cp -r %{_builddir}/%{name}/etc/* %{buildroot}%{_sysconfdir}/%{name}
rm -rf %{buildroot}%{_sysconfdir}/%{name}/sample
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/modules

# change exec of python bin
chmod +x %{buildroot}/%{python_sitelib}/%{name}/bin/alignak*.py

# systemd part
install -d -m0755 %{buildroot}%{_unitdir}
mv %{_builddir}/%{name}/systemd/* %{buildroot}%{_unitdir}/
rm -rf %{buildroot}/usr/etc/init.d/%{name}*

# log
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}/archives

# run
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}

# Module, for new style module setup (namespace will do the job)
install -d -m0755 %{buildroot}/usr/share/pyshared/%{name}

%clean
rm -rf %{buildroot}

%files all
# Alignak python lib
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}*.egg-info


# Module, for new style module setup (namespace will do the job)
/usr/share/pyshared/%{name}

# Log and run dir 
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/log/%{name}
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/run/%{name}

# Basic config
%config(noreplace) %{_sysconfdir}/%{name}/*

# Daemon python binaries
/%{_bindir}/%{name}-*

# Systemd part
%{_unitdir}/%{name}*


%post
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%preun
/bin/systemctl --no-reload disable %{name}-arbiter.service > /dev/null 2>&1 || :
/bin/systemctl --no-reload disable %{name}-scheduler.service > /dev/null 2>&1 || :
/bin/systemctl --no-reload disable %{name}-poller.service > /dev/null 2>&1 || :
/bin/systemctl --no-reload disable %{name}-receiver.service > /dev/null 2>&1 || :
/bin/systemctl --no-reload disable %{name}-broker.service > /dev/null 2>&1 || :
/bin/systemctl --no-reload disable %{name}-reactionner.service > /dev/null 2>&1 || :
/bin/systemctl stop %{name}-arbiter.service > /dev/null 2>&1 || :
/bin/systemctl stop %{name}-scheduler.service > /dev/null 2>&1 || :
/bin/systemctl stop %{name}-poller.service > /dev/null 2>&1 || :
/bin/systemctl stop %{name}-receiver.service > /dev/null 2>&1 || :
/bin/systemctl stop %{name}-broker.service > /dev/null 2>&1 || :
/bin/systemctl stop %{name}-reactionner.service > /dev/null 2>&1 || :


%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%changelog
* Sun Jan 31 2016 Sebastien Coavoux <alignak@pyseb.cx> - 0.2-1
- Update version
* Sun Sep 20 2015 Sebastien Coavoux <alignak@pyseb.cx> - 0.1-1
- Initial package
