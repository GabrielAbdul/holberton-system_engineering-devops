# set up your client SSH configuration file so that you can connect to a server without typing a password

file_line {'ssh_config':
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
	ensure => 'present',
}

file_line {'ssh_config_1':
    path    => '/etc/ssh/ssh_config',
	line    => 'IdentityFile ~/.ssh/holberton',
	ensure  => 'present',
}
