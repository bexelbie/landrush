# Generated from landrush-1.0.0.gem by gem2rpm -*- rpm-spec -*-
# Now maintained manually
%global gem_name landrush

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: a vagrant plugin providing consistent DNS visible on host and guests
Group: Development/Languages
License: MIT
URL: https://github.com/vagrant-landrush/landrush
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires(posttrans): vagrant
Requires(preun): vagrant
Requires: vagrant
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
#BuildRequires: rubygems-eventmachine >= 1.0.9.1
BuildRequires: ruby
BuildRequires: vagrant
BuildArch: noarch
Provides: vagrant(%{gem_name}) = %{version}

%description
Forget about IPs in Vagrant - Automated DNS for your VMs
This Vagrant plugin spins up a lightweight DNS server and makes it visible
to your guests and your host, so that you can easily access all your
machines without having to fiddle with IP addresses.
DNS records are automatically added and removed as machines are brought up
and down, and you can configure static entries to be returned from the
server as well. See the README for more documentation.


%package doc
Summary: Documentation for %{name}
Group: Documentation
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




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.config
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/NOTES.md
%{gem_instdir}/features
%{gem_instdir}/issues
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/examples
%{gem_instdir}/landrush.gemspec
%{gem_instdir}/test

%changelog
* Mon Jun 13 2016 vagrant - 1.0.0-1
- Initial package
