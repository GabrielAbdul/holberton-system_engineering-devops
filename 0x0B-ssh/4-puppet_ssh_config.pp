# set up your client SSH configuration file so that you can connect to a server without typing a password

file_line {'ssh_config':
    path   => '/etc/ssh/ssh_config',
    line   => 'passwordAuthentication no',
	ensure => 'present',
}

file_line {'ssh_config_1':
    path    => '/etc/ssh/ssh_config',
    match   => 'IdentityFile ~/.ssh/id_rsa',
	line    => 'IdentityFile ~/.ssh/holberton',
	enable => 'present',
}
