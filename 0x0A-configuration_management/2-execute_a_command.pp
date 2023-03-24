#Executing a bash command that kills with puppet

exec { 'kill process':
command  => '/usr/bin/pkill -f killmenow'
}
