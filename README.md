##Dnsamasq Puppet Module
###Summary
This module contains a single class named dnsmasq. The class manages the package, configuration files and service of dnsmasq. It accepts three class parameters: domains, ip and external_dns. A script is also included that will check and see if the dnsmasq service is running and to make sure it is listening. This script should be run as root to work properly.
###Class Parameters
domains (array): An array of domain names that are inserted in dnsmasq.conf

ip: The ip address that the domains from the domains class paremeter will resolve to

external_dns: The external nameserver that will be inserted into resolv.conf. If it's set to "" or false an external or secondary nameserver will not be entered.
###Example Configuration
The following configuration of the dnsmasq class will have bob.com and alice.com resolve to 1.2.3.4. It will also use the nameserver 8.8.8.8 as an external, or secondary, nameserver.

```
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
```