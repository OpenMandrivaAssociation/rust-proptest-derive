# Generated by rust2rpm 9
# * compiletest_rs is not packaged
%bcond_with check
%global debug_package %{nil}

%global crate proptest-derive

Name:           rust-%{crate}
Version:        0.1.2
Release:        3%{?dist}
Summary:        Custom-derive for the Arbitrary trait of proptest

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/proptest-derive
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(proc-macro2/default) >= 0.4.0 with crate(proc-macro2/default) < 0.5.0)
BuildRequires:  (crate(quote/default) >= 0.6.0 with crate(quote/default) < 0.7.0)
BuildRequires:  (crate(syn/default) >= 0.15.17 with crate(syn/default) < 0.16.0)
BuildRequires:  (crate(syn/extra-traits) >= 0.15.17 with crate(syn/extra-traits) < 0.16.0)
BuildRequires:  (crate(syn/full) >= 0.15.17 with crate(syn/full) < 0.16.0)
BuildRequires:  (crate(syn/visit) >= 0.15.17 with crate(syn/visit) < 0.16.0)
%if %{with check}
BuildRequires:  (crate(compiletest_rs/default) >= 0.3.19 with crate(compiletest_rs/default) < 0.4.0)
BuildRequires:  (crate(compiletest_rs/stable) >= 0.3.19 with crate(compiletest_rs/stable) < 0.4.0)
BuildRequires:  (crate(compiletest_rs/tmp) >= 0.3.19 with crate(compiletest_rs/tmp) < 0.4.0)
BuildRequires:  (crate(criterion/default) >= 0.2.0 with crate(criterion/default) < 0.3.0)
BuildRequires:  (crate(proptest/default) >= 0.9.4 with crate(proptest/default) < 0.10.0)
%endif
%endif

%global _description %{expand:
Custom-derive for the Arbitrary trait of proptest.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 17:58:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Initial package
