# Sky is the limit, let's bring that limit higher

exec { 'replace files per process':
  command => "sudo sed -i '/^ULIMIT/s/^/#/g' /etc/default/nginx",
  path    =>   ['/bin', '/usr/bin'],
}
exec {'restart nginx service':
  command =>  'sudo service nginx restart',
  path    => '/usr/bin',
}
