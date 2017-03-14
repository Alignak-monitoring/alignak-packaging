%global alignak_user alignak
%global alignak_group alignak

Summary:        Python Rest API for Alignak Monitoring tool
Name:           alignak-backend
Version:        0.1
Release:        1
URL:            https://github.com/Alignak-monitoring-contrib/alignak-backend 
Source0:        %{name}-%{version}.tar.gz
License:        AGPLv3

BuildRequires:  python-devel
BuildRequires:  python-setuptools

Group:          Application/System


%description
Alignak Backend is a REST Api based on Python Eve framework

%package 
Summary: Alignak REST Backend
Group:          Application/System
Requires:       python >= 2.6
Requires:       python-docopt
Requires:       python-jsonschema
Requires:       python2-future
Requires:       python2-statsd
Requires:       uwsgi-plugin-python
Requires:       uwsgi


%prep
cd %{vendor}
pip install .
%setup -qn %{name}

 
%install

%{__python} setup.py install -O1 --root=%{buildroot} --install-lib=%{python_sitelib}

install -d -m0755  %{buildroot}%{_sysconfdir}/%{name}/
rm -rf %{buildroot}%{_sysconfdir}/%{name}/*

# Remove generated conf
#rm -rf %{buildroot}/usr/etc/%{name}/*
#rm -rf %{buildroot}/usr/etc/default/%{name}

# Copy original file but remove sample
cp -r %{_builddir}/%{name}/etc/* %{buildroot}%{_sysconfdir}/%{name}
#rm -rf %{buildroot}%{_sysconfdir}/%{name}/sample

# change exec of python bin
#chmod +x %{buildroot}/%{python_sitelib}/%{name}/bin/alignak*.py

# systemd part
install -d -m0755 %{buildroot}%{_unitdir}
mv %{_builddir}/%{name}/systemd/* %{buildroot}%{_unitdir}/

# log
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}/archives

# run
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}


%clean
rm -rf %{buildroot}

%files all
# Alignak Backend python lib
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}*.egg-info
# Deps



# Log and run dir 
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/log/%{name}
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/run/%{name}

# Basic config
%config(noreplace) %{_sysconfdir}/%{name}/*

# Daemon python binaries
/%{_bindir}/%{name}

# Systemd part
%{_unitdir}/%{name}


%post
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%preun
/bin/systemctl --no-reload disable %{name}.service > /dev/null 2>&1 || :
/bin/systemctl stop %{name}.service > /dev/null 2>&1 || :


%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%changelog
* Fri Mar 03 2017 Sebastien Coavoux <alignak@pyseb.cx> - 0.1-1
- Initial package
