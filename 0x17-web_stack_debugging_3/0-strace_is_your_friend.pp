# Fixes bad `phpp` extensions in the Wordpress file `wp-settings.php` to `php`

exec {'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
