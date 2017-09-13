# Generated from syslog_protocol-0.9.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name syslog_protocol

Name: rubygem-%{gem_name}
Version: 0.9.2
Release: 1%{?dist}
Summary: Syslog protocol parser and generator
License: MIT 
URL: https://github.com/eric/syslog_protocol
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(bacon)
# BuildRequires: rubygem(bacon) >= 1.1.0
# BuildRequires: rubygem(bacon) < 1.2
#Requires: fluentd
Requires: bacon
BuildArch: noarch

%if 0%{?rhel} > 0
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Syslog protocol parser and generator.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# bacon -a
rake test
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_instdir}/syslog_protocol.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Wed Sep 13 2017 stran <steveqtran@gmail.com> - 0.9.2-1
- Initial package
