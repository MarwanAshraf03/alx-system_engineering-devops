file { '/var/www/html/index.html':
  ensure  => file,
  content => 'hello world',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
