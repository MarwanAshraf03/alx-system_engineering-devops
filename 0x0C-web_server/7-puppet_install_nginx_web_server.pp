# Puppet code to install Flask version 2.1.0 using pip3
exec {command => ['/bin/apt-get', 'update; -y']}
exec {command => ['/bin/apt-get', 'install nginx; -y']}
exec {command => ['/bin/echo', 'Hello World! > /var/www/html/index.nginx-debian.html']}
exec {command => ['/bin/echo', 'http {
        include mime.types;

        server {
                listen 80;
                root /var/www/html/;
                index index.nginx-debian.html;
                location /redirect_me/ {
                    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
                }
        }
}
events {} > /etc/nginx/nginx.conf']}
exec {command => ['/bin/service', 'nginx restart']}
