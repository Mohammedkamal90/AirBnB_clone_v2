#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers using function deploy.
"""
from fabric.api import env, local
from os.path import exists
from datetime import datetime

# Import do_pack and do_deploy functions
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

# Define the environment (web servers)
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # Set the username for SSH

def deploy():
    """
    Creates and distributes an archive to the web servers, deploying the new version.

    Returns:
        (bool): True if successful, False otherwise.
    """
    # Call do_pack and store the path of the created archive
    archive_path = do_pack()

    # Return False if no archive has been created
    if not archive_path:
        return False

    try:
        # Call do_deploy using the new path of the new archive
        return do_deploy(archive_path)
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    # Example command to deploy
    result = deploy()
    if result:
        print("Deployment successful!")
    else:
        print("Deployment failed.")
