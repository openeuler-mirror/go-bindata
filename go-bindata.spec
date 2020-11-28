%global debug_package %{nil}
%global provider        github
%global provider_tld    com
%global project         go-bindata
%global repo            go-bindata
# https://github.com/go-bindata/go-bindata
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           go-bindata
Version:        3.1.3
Release:        1
Summary:        A small utility which generates Go code from any file
License:        MIT
URL:		    https://%{provider_prefix}
Source0:	    https://%{provider_prefix}/archive/%{name}-%{version}.tar.gz

BuildRequires:  golang

%description
%{summary}

This tool converts any file into managable Go source code. Useful for
embedding binary data into a go program. The file data is optionally gzip
compressed before being converted to a raw byte slice.

%prep
%autosetup -n %{name}-%{version} -p1

%build
mkdir -p src/github.com/go-bindata/
ln -s ../../../ src/github.com/go-bindata/go-bindata

export GOPATH=$(pwd):%{gopath}

# go build -o bin/go-bindata github.com/go-bindata/go-bindata/go-bindata
go build -o bin/go-bindata %{import_path}/go-bindata

%install
# install -d -p /root/rpmbuild/BUILDROOT/go-bindata-3.1.3-1.aarch64/usr/bin
install -d -p %{buildroot}%{_bindir}
# install -m 755 bin/go-bindata /root/rpmbuild/BUILDROOT/go-bindata-3.1.3-1.aarch64/usr/bin/go-bindata
install -m 755 bin/go-bindata %{buildroot}%{_bindir}/go-bindata

%files
%doc LICENSE README.md
%{_bindir}/go-bindata

%changelog
* Fri Jul 10 2020 openEuler Buildteam <buildteam@openeuler.org> - v1.7.0-1
- Package init
