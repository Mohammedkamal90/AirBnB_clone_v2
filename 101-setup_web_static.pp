# 101-setup_web_static.pp

# Ensure the web_static directory exists
file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  force   => true,
}

# Give ownership of the /data/ folder to the ubuntu user AND group
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80 default_server;
                server_name _;
                location /hbnb_static {
                    alias /data/web_static/current;
                }
                location /redirect_me {
                    rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
                }
                error_page 404 /404.html;
                location = /404.html {
                    root /usr/share/nginx/html;
                    internal;
                }
                add_header X-Served-By $HOSTNAME;
            }",
  notify  => Service['nginx'],
}

# Notify Nginx to restart
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
