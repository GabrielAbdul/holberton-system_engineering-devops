# set up your client SSH configuration file so that you can connect to a server without typing a password

file_line {'ssh_config':
    path  => '~/etc/ssh/ssh_config',
    match => '*Pass*Auth*yes'
    line  => '#   PasswordAuthentication no'
}

file_line {'ssh_config':
    path  => '~/etc/ssh/ssh_config',
    match => '*Id*F*_rsa'
    line  => '#   IdentityFile ~/.ssh/holberton'
}
