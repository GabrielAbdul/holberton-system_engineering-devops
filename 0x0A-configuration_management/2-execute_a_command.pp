# Using Puppet, create a manifest that kills a process named killmenow
# Requirements: must use the exec PP resource, must use pkill

exec { 'killmenow':
    command  => 'pkill -f killmenow',
    path     => '/usr/bin'
}
