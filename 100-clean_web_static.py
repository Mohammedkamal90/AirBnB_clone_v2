#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives using the function do_clean.
"""
from fabric.api import env, local, run
from datetime import datetime
from os.path import exists

# Define the environment (web servers)
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # Set the username for SSH

def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep. Default is 0.

    Returns:
        None
    """
    number = int(number)

    # Get the list of archives in the versions folder
    local_archives = local("ls -1tr versions", capture=True).split("\n")

    # Keep only the most recent 'number' archives
    archives_to_keep = local_archives[-number:]
    archives_to_delete = local_archives[:-number]

    # Delete unnecessary archives in the versions folder
    for archive in archives_to_delete:
        local("rm -f versions/{}".format(archive))

    # Get the list of archives in the /data/web_static/releases folder on the web servers
    remote_archives = run("ls -1tr /data/web_static/releases", capture=True).split("\n")

    # Keep only the most recent 'number' archives on the web servers
    remote_archives_to_keep = remote_archives[-number:]
    remote_archives_to_delete = remote_archives[:-number]

    # Delete unnecessary archives in the /data/web_static/releases folder on the web servers
    for archive in remote_archives_to_delete:
        run("rm -rf /data/web_static/releases/{}".format(archive))

if __name__ == "__main__":
    # Example command to clean archives, keeping the most recent 2
    do_clean(number=2)
