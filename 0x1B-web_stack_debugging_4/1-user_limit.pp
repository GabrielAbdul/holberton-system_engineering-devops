# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec {'allow more files to be open':
    command => "sed -i 's/nofile*/nofile 97816/g' /etc/security/limits.conf",
    path    => '/bin',
}
