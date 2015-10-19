class dnsmasq {
        package { 'dnsmasq':
            ensure => installed,
        }
        
        file { '/etc/dnsmasq.conf':
            ensure  => present,
            require => Package['dnsmasq'],
            owner   => 'root',
            group   => 'root',
            mode    => 0644,
        }
        
        file { '/etc/resolv.conf':
            ensure  => present,
            require => File['/etc/dnsmasq.conf'],
            owner   => 'root',
            group   => 'root',
            mode    => 0644,
        }

        service { 'dnsmsq':
            ensure    => running,
            enabled   => true,
            subscribe => File['/etc/dnsmasq.conf'],
        }
