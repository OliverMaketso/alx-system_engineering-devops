# Using Puppet, install Flask version 2.1.0 using pip3

package { 'python3-pip':
ensure   => installed,
}
