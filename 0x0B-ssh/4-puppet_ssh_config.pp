file_line {'ssh_config':
    path  => '~/etc/ssh/ssh_config',
    match => '*Pass*Auth*yes'
    line  => '#   PasswordAuthentication no'
}

file_line {'ssh_config':
    path  => '~/etc/ssh/ssh_config',
    match => '*Id*F*_rsa'
    line  => '#   IdentityFile ~\/.ssh/holberton'
}
