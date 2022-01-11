# Manifiest that configures with puppet

exec { 'update':
  command => 'sudo apt-get -y update',
  path    => ['/usr/bin'],
  returns => [0,1]
}
