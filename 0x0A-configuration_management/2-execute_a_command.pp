#Manifest that kills a process named killmenow

exec { 'kill_me_now':
  command  => 'pkill -x killmenow',
  provider => shell,
}
