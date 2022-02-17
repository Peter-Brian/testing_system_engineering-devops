# fix config file

exec { 'fix php code 500':
  command  => 'sed -i s/phpp/php/g /var/www/wp-settings.php',
  provider => shell,
}
