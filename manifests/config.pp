class dnsmasq::config {

   $ip      = $dnsmasq::params::default_ip
   $domains = $dnsmasq::parmas::default_domains

   $secondary_dns = $dnsmasq::params::default_sec_dns

   file { '/etc/dnsmasq.conf':
    ensure  => present,
    require => Package['dnsmasq'],
    owner   => 'root',
    group   => 'root',
    mode    => 0644,
    content => template("dnsmasq/dnsmasq.conf.erb"),
   }

   file { '/etc/dnsmasq.conf':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => 0644,
    content => template("dnsmasq/resolv.conf.erb"),
   }

}
