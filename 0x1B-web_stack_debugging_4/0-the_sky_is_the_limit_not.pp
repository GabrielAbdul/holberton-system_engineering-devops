# Sky is the limit, let's bring that limit higher
exec { 'replace files per process':
  command => "sudo sed -i 's/15/4096/g' /etc/default/nginx",
  path    =>   ['/bin', '/usr/bin'],
}
exec {'restart nginx service':
  command =>  'sudo service nginx restart',
  path    => '/usr/bin',
}
