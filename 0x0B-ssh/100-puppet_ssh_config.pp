class { 'ssh':
	options => {
		'User' => 'ubuntu',
		'Hostname' => '54.172.106.250',
		'HostKey' => '~/.ssh/school'
	}
}
