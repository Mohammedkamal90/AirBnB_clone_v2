#!/usr/bin/env bash
# Install Nginx if not install
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx

# Create necessary folder
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared /data/web_static/current

# Create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/^location \/hbnb_static {/,$d' $nginx_config
sudo sh -c 'echo "location /hbnb_static {" >> '"$nginx_config"'
sudo sh -c 'echo "    alias /data/web_static/current/;" >> '"$nginx_config"'
sudo sh -c 'echo "    index index.html;" >> '"$nginx_config"'
sudo sh -c 'echo "}" >> '"$nginx_config"'

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0
