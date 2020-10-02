# script that corrects filename
file_line {'debug':
    path  => '/var/www/html/wp-settings.php',
    line  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
    match => 'wp-config-locale.phpp',
}
