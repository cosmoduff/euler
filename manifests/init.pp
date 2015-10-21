class dnsmasq {

  package { 'dnsmasq':
    ensure => installed,
  }

  include dnsmasq::params
  include dnsmasq::config
  include dnsmasq::service
        
}
