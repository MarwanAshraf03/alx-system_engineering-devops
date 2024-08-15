# This Puppet manifest creates /var/www/html/index.html with the content from hi/hi.txt.

file { '/var/www/html/index.html':
  ensure  => file,
  content => file('./hi.txt'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
