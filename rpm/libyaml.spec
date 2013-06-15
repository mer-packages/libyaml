Name:       libyaml
Summary:    YAML 1.1 parser and emitter written in C
Version:    0.1.4
Release:    1
Group:      System Environment/Libraries
License:    MIT
URL:        http://pyyaml.org/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  LibYAML is a YAML parser and
emitter written in C.


%package devel
Summary:    Development files for LibYAML applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use LibYAML.


%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{_libdir}/%{name}*.so.*

%files devel
%defattr(-,root,root,-)

%doc doc/html
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/yaml-0.1.pc
%{_includedir}/yaml.h

