#!/usr/bin/python3
"""
Fabric script that distributes archive to your web servers using function do_deploy
"""
from fabric.api import env, put, run
from os.path import exists
import os
from datetime import datetime

# Define the environment (web servers)
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # Set the username for SSH

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and deploys the new version.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        (bool): True if successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/<archive filename without extension>
        filename = os.path.basename(archive_path)
        folder_name = filename.split('.')[0]
        release_path = '/data/web_static/releases/{}'.format(folder_name)

        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, release_path))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Move contents to the appropriate folder
        run('mv {}/web_static/* {}'.format(release_path, release_path))

        # Remove unnecessary folder
        run('rm -rf {}/web_static'.format(release_path))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    # Example command to deploy
    archive_path = 'versions/web_static_20170315003959.tgz'
    result = do_deploy(archive_path)
    if result:
        print("Deployment successful!")
    else:
        print("Deployment failed.")
