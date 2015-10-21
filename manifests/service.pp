class dnsmasq::service {

    service { 'dnsmasq':
      ensure    => running,
      enabled   => true,
      subscribe => File['/etc/dnsmasq.conf'],
    }

}
