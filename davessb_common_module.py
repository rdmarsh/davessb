#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#only top checks are not infos
#negative checks call positive with 'nots', don't redo checks

import os

#messages
def _pass(msg):
    print("💚  [PASS]: " + msg)

def _fail(msg):
    print("💔  [FAIL]: " + msg)

def _info(msg):
    print("💛  [INFO]: " + msg)

#object existance checks
def _exists(pathobj):
    if os.path.exists(pathobj):
        _bool=' '
        _info("object does" + _bool + "exist: " + pathobj)
        return True
    else:
        _bool=' not '
        _info("object does" + _bool + "exist: " + pathobj)
        return False

#object user owner checks
def _uid_owns(pathobj):
    if _exists(pathobj):
        if os.stat(pathobj).st_uid == os.getuid():
            _bool=' '
            _info("uid does" + _bool + "own object: " + pathobj)
            return True
        else:
            _bool=' not '
            _info("uid does" + _bool + "own object: " + pathobj)
            return False

#object group owner checks
def _gid_owns(pathobj):
    if _exists(pathobj):
        if os.stat(pathobj).st_gid == os.getgid():
            _bool=' '
            _info("gid does" + _bool + "own object: " + pathobj)
            return True
        else:
            _bool=' not '
            _info("gid does " + _bool + " own object: " + pathobj)
            return False

