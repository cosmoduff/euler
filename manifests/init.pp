# Class: dnsmasq
# 
# Install dnsmasq package
#
# Manage /etc/dnsmasq.conf adding domains listed in th domains var
#
# Manage /etc/resolv.conf setting loclhost as the first nameserver
# and add a second nameserver from the secondary_dns var
#
# Start and enable the dnsmasq service
#

class dnsmasq (
$domains = $dnsmasq::params::domains,
$ip = $dnsmasq::params::ip
)

{
  $external_dns = $dnsmasq::params::external_dns

  package { 'dnsmasq':
    ensure => installed,
  }

  file { '/etc/dnsmasq.conf':
    ensure  => present,
    require => Package['dnsmasq'],
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('dnsmasq/dnsmasq.conf.erb'),
  }

  file { '/etc/resolv.conf':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('dnsmasq/resolv.conf.erb'),
  }

    service { 'dnsmasq':
      ensure    => running,
      enable    => true,
      subscribe => File['/etc/dnsmasq.conf'],
    }

}
