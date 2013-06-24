%define pkgname systemu
Summary:	Universal capture of stdout and stderr and handling of child process pid
Name:		ruby-%{pkgname}
Version:	2.5.2
Release:	2
License:	BSD or Ruby
Group:		Development/Libraries
URL:		https://github.com/ahoward/systemu
Source0:	http://production.cf.rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	7ac461f71ebf29b68f286fe34730c2f2
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Universal capture of stdout and stderr and handling of child process
pid.

%prep
%setup -q

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.erb
%{ruby_vendorlibdir}/systemu.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
