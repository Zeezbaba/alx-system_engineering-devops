# Fixing a phpp extension to php in a file on a server

$corrupt_file = '/var/www/html/wp-settings.php'

#replacing line containing "phpp" with "php"

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' ${corrupt_file}",
  path    => ['/bin','/usr/bin']
}
