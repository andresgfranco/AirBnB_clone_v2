#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_Static folder"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["34.74.115.197", "54.87.144.17"]


def do_pack():
    """Function that creates
    a .tgz file"""

    filename = "versions/web_static_{}.tgz"
    filename = filename.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(filename))
    if create.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """Function that distributes an archive to a server"""

    if not os.path.exists(archive_path):
        return False

    destdir = "/data/web_static/releases/"
    aux = archive_path.split('/')[1]
    filename = aux.split('.')[0]
    destfile = destdir + filename

    try:
        put(archive_path, "/tmp")
        run('mkdir -p {}'.format(destfile))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(filename, destfile))
        run('rm -f /tmp/{}.tgz'.format(filename))
        run('mv {}/web_static/* {}/'.format(destfile, destfile))
        run('rm -rf {}/web_static/*'.format(destfile))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(destfile))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ Function that call do_pack and do_deply for full deployment """
    filepath = do_pack()
    if filepath is None:
        return False
    value = do_deploy(filepath)
    return value

if __name__ == "__main__":
    do_pack()
