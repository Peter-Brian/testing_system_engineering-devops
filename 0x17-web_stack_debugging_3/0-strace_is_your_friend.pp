# fix config file

exec { 'fix phpp':
  environment => ['DIR=/var/www/wp-settings.php',
                  'FIX=phpp',
                  'NEW=php'],
  command     => 'sudo sed -i s/$FIX/$NEW/g $DIR',
  path        => ['/bin', '/usr/bin']
}
