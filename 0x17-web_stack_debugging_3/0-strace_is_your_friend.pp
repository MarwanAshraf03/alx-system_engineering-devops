# This Puppet manifest creates /var/www/html/index.html with the content from hi/hi.txt.

file { '/var/www/html/index.html':
  ensure  => file,
  source => 'file:///0x17-web_stack_debugging_3/hi.txt',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
