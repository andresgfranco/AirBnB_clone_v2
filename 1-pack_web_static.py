#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_Static folder"""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """Function that creates
    a .tgz"""

    name = "./versions/webs_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None

if __name__ == "__main__":
    do_pack()
