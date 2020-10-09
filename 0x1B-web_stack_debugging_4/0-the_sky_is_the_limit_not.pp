# Sky is the limit, let's bring that limit higher
exec { 'replace files per process':
  command => "sudo sed -i 's/worker_processes 4/worker_processes 2048/g' /etc/nginx/nginx.conf",
  path    =>   ['/bin', '/usr/bin'],
}
exec {'restart nginx service':
  command =>  'sudo service nginx restart',
  path    => '/usr/bin',
}
