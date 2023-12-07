#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        (str): Archive path if successful, None otherwise.
    """
    # Create the folder versions if it doesn't exist
    local("mkdir -p versions")

    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Set the archive path
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Create the .tgz archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Check if the archive was created successfully
    if result.succeeded:
        return archive_path
    else:
        return None

if __name__ == "__main__":
    # Execute the do_pack function when the script is run
    archive_path = do_pack()
    if archive_path:
        print("web_static packed: {} -> {}Bytes\nDone.".format(archive_path, os.path.getsize(archive_path)))
    else:
        print("Packaging failed.")
