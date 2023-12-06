#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

# Install Nginx if not installed
sudo apt-get -y update
sudo apt-get -y install nginx

#config firewall
sudo ufw allow 'Nginx HTTP'

#create folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# test string
echo "<h1>Welcome to www.beta-scribbles.tech</h1>" > /data/web_static/releases/test/index.html

#prevent overwrite
if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;

#--create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data

# Update Nginx configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

#restart NGINX
sudo service nginx restart
