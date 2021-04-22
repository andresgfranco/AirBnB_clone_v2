#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_Static folder"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Function that creates
    a .tgz"""

    filename = "versions/web_static_{}.tgz"
    filename = filename.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(filename))
    if create.succeeded:
        return filename
    else:
        return None

if __name__ == "__main__":
    do_pack()
