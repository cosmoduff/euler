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

class dnsmasq {

  $ip      =  1.2.3.4
  $domains = ['bob.com',
            'alice.com']

  $secondary_dns = 8.8.8.8

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
