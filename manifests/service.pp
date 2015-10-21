class dnsmasq::service {

    service { 'dnsmasq':
      ensure    => running,
      enable   => true,
      subscribe => File['/etc/dnsmasq.conf'],
    }

}
