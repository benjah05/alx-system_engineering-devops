#execute a command
exec { 'kill_a_process':
command => 'pkill -f "./killmenow"',
path    => ['/usr/bin', '/bin'],
}
