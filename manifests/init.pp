class dnsmasq {
        package { 'dnsmasq':
            ensure => installed,
        }
        
        file { '/etc/dnsmasq.conf':
            ensure  => present,
            require => Package['dnsmasq'],
        }

        service { 'dnsmsq':
            ensure    => running,
            enabled   => true,
            subscribe => File['/etc/dnsmasq.conf'],
        }
