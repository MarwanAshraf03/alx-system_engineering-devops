# This Puppet manifest creates the /var/www/html/index.html file with "hello world" as its content.

file { '/var/www/html/index.html':
  ensure  => file,
  content => "hello world\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
