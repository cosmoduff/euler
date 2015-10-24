##Dnsamasq Puppet Module
###Summary
This module contains a single class named dnsmasq. The class manages the package, configuration files and service of dnsmasq. It accepts three different class parameters.The first, domains, accepts an array of domains to be configured in the dnsmasq.conf file. The second class parameter, ip, sets the ip address to the domains in dnsmasq.conf. The third, external_dns, sets a external dns server in resolv.conf to lookup entries that are not found in dnsmasq. If the external_dns class parameter is set to "", or false, an external dns will not be used and only domains listed in dnsmasq.conf will be resolved.
###Example Configuration
The following configuration of the dnsmasq class will have bob.com and alice.com resolve to 1.2.3.4. It will also use the nameserver 8.8.8.8 as an external, or secondary, nameserver.

class dnsmasq {

  $domains = ['bob.com',
            'alice.com']

  $ip      =  1.2.3.4

  $external_dns = 8.8.8.8

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