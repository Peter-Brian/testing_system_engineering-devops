# Script that installs and configures nginx on a server

package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.html':
  content => 'Hellow World'
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://example.com/ permanent;'
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
