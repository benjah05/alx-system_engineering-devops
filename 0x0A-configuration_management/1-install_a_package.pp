# Install Python 3.8 using the system package manager
package { 'python3.8':
  ensure => present,
}

# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3.8'],
}

# Install Werkzeug version compatible with Flask
package { 'Werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
  require  => Package['Flask'],
}

