%global alignak_user alignak
%global alignak_group alignak

Summary:        Python Rest API for Alignak Monitoring tool
Name:           alignak-backend
Version:        0.1
Release:        1
URL:            https://github.com/Alignak-monitoring-contrib/alignak-backend 
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor
License:        AGPLv3

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pip

Group:          Application/System


%description
Alignak Backend is a REST Api based on Python Eve framework

Requires:       python >= 2.6
Requires:       python-docopt
Requires:       python-jsonschema
Requires:       python2-future
Requires:       python2-statsd
Requires:       uwsgi-plugin-python
Requires:       uwsgi
# This package is builded in this spec
Requires:       %{name}-dep


%package dep
Summary:        All-in-one alignak-backend non-packaged dependencies
Requires:       python >= 2.

%description dep
Ugly package to provide alignak-backend dependencies as their are not packaged yet

%prep
%autosetup -n %{name}

%install
cd %{SOURCE1}
pip install --root=%{buildroot} -I *
#Remove not compilable py2 file
rm -rf %{buildroot}%{python_sitelib}/apscheduler/executors/base_py3.py
rm -rf %{buildroot}%{python_sitelib}/jinja2/asyncfilters.py
rm -rf %{buildroot}%{python_sitelib}/jinja2/asyncsupport.py


cd -


%{__python} setup.py install -O1 --root=%{buildroot} --install-lib=%{python_sitelib}

install -d -m0755  %{buildroot}%{_sysconfdir}/%{name}/
rm -rf %{buildroot}%{_sysconfdir}/%{name}/*

# Remove generated conf
rm -rf %{buildroot}/usr/etc/%{name}/*

# Copy original file but remove sample
cp -r %{_builddir}/%{name}/etc/* %{buildroot}%{_sysconfdir}/%{name}

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

%files 
# Alignak Backend python lib
%{python_sitelib}/alignak_backend
%{python_sitelib}/alignak_backend*.egg-info

# Log and run dir 
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/log/%{name}
%attr(-,%{alignak_user} ,%{alignak_group}) %dir %{_localstatedir}/run/%{name}

# Basic config
%config(noreplace) %{_sysconfdir}/%{name}/*

# Daemon python binaries
/%{_bindir}/%{name}
/%{_bindir}/%{name}-uwsgi

# Systemd part
%{_unitdir}/%{name}.service


%post
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%preun
/bin/systemctl --no-reload disable %{name}.service > /dev/null 2>&1 || :
/bin/systemctl stop %{name}.service > /dev/null 2>&1 || :


%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :


%files dep
#/usr/lib
%{python_sitelib}/APScheduler-3.3.1.dist-info
%{python_sitelib}/Cerberus-0.9.2-py2.7.egg-info
%{python_sitelib}/Eve-0.7.2-py2.7.egg-info
%{python_sitelib}/Eve_Swagger-0.0.6-py2.7.egg-info
%{python_sitelib}/Events-0.2.2-py2.7.egg-info
%{python_sitelib}/Flask-0.12.dist-info
%{python_sitelib}/Flask_APScheduler-1.6.0-py2.7.egg-info
%{python_sitelib}/Flask_Bootstrap-3.3.7.1-py2.7.egg-info
%{python_sitelib}/Flask_PyMongo-0.4.1.dist-info
%{python_sitelib}/Jinja2-2.9.5.dist-info
%{python_sitelib}/MarkupSafe-0.23-py2.7.egg-info
%{python_sitelib}/Werkzeug-0.11.15.dist-info
%{python_sitelib}/_dummy_thread
%{python_sitelib}/_markupbase
%{python_sitelib}/_thread
%{python_sitelib}/appdirs-1.4.2.dist-info
%{python_sitelib}/appdirs.py
%{python_sitelib}/appdirs.pyc
%{python_sitelib}/appdirs.pyo
%{python_sitelib}/apscheduler
%{python_sitelib}/builtins
%{python_sitelib}/cerberus
%{python_sitelib}/click
%{python_sitelib}/click-6.7.dist-info
%{python_sitelib}/concurrent
%{python_sitelib}/copyreg
%{python_sitelib}/dateutil
%{python_sitelib}/dominate
%{python_sitelib}/dominate-2.3.1-py2.7.egg-info
%{python_sitelib}/easy_install.py
%{python_sitelib}/easy_install.pyc
%{python_sitelib}/easy_install.pyo
%{python_sitelib}/eve
%{python_sitelib}/eve_swagger
%{python_sitelib}/events
%{python_sitelib}/flask
%{python_sitelib}/flask_apscheduler
%{python_sitelib}/flask_bootstrap
%{python_sitelib}/flask_pymongo
%{python_sitelib}/funcsigs
%{python_sitelib}/funcsigs-1.0.2.dist-info
%{python_sitelib}/functools32
%{python_sitelib}/functools32-3.2.3_2-py2.7.egg-info
%{python_sitelib}/future
%{python_sitelib}/future-0.16.0-py2.7.egg-info
%{python_sitelib}/futures-3.0.5.dist-info
%{python_sitelib}/html
%{python_sitelib}/http
%{python_sitelib}/influxdb
%{python_sitelib}/influxdb-4.0.0.dist-info
%{python_sitelib}/itsdangerous-0.24-py2.7.egg-info
%{python_sitelib}/itsdangerous.py
%{python_sitelib}/itsdangerous.pyc
%{python_sitelib}/itsdangerous.pyo
%{python_sitelib}/jinja2
%{python_sitelib}/libfuturize
%{python_sitelib}/libpasteurize
%{python_sitelib}/markupsafe
%{python_sitelib}/packaging
%{python_sitelib}/packaging-16.8.dist-info
%{python_sitelib}/past
%{python_sitelib}/pkg_resources
%{python_sitelib}/pyparsing-2.2.0.dist-info
%{python_sitelib}/pyparsing.py
%{python_sitelib}/pyparsing.pyc
%{python_sitelib}/pyparsing.pyo
%{python_sitelib}/python_dateutil-2.4.2.dist-info
%{python_sitelib}/pytz
%{python_sitelib}/pytz-2016.10.dist-info
%{python_sitelib}/queue
%{python_sitelib}/reprlib
%{python_sitelib}/requests
%{python_sitelib}/requests-2.13.0.dist-info
%{python_sitelib}/setuptools
%{python_sitelib}/setuptools-34.3.1.dist-info
%{python_sitelib}/simplejson
%{python_sitelib}/simplejson-3.10.0-py2.7.egg-info
%{python_sitelib}/six-1.10.0.dist-info
%{python_sitelib}/six.py
%{python_sitelib}/six.pyc
%{python_sitelib}/six.pyo
%{python_sitelib}/socketserver
%{python_sitelib}/tests
%{python_sitelib}/tkinter
%{python_sitelib}/tzlocal
%{python_sitelib}/tzlocal-1.3-py2.7.egg-info
%{python_sitelib}/visitor
%{python_sitelib}/visitor-0.1.3-py2.7.egg-info
%{python_sitelib}/werkzeug
%{python_sitelib}/winreg
%{python_sitelib}/xmlrpc

#lib64
%{python_sitearch}/bson
%{python_sitearch}/gridfs
%{python_sitearch}/pymongo
%{python_sitearch}/pymongo-3.4.0.dist-info

#bin
/%{_bindir}/easy_install*
/%{_bindir}/flask
/%{_bindir}/futurize
/%{_bindir}/pasteurize



%changelog
* Fri Mar 03 2017 Sebastien Coavoux <alignak@pyseb.cx> - 0.1-1
- Initial package
