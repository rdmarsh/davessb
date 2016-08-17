#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#only top checks are not infos
#negative checks call positive with 'nots', don't redo checks

import os

class bcolors:
    FAIL = '\033[31m'
    PASS = '\033[32m'
    WARN = '\033[33m'
    INFO = '\033[34m'
    ENDC = '\033[0m'

#messages
def _fail(msg):
    print("💔  " + bcolors.FAIL + "[FAIL]" + bcolors.ENDC + ": " + msg)

def _pass(msg):
    print("💚  " + bcolors.PASS + "[PASS]" + bcolors.ENDC + ": " + msg)

def _warn(msg):
    print("💛  " + bcolors.WARN + "[WARN]" + bcolors.ENDC + ": " + msg)

def _info(msg):
    print("💙  " + bcolors.INFO + "[INFO]" + bcolors.ENDC + ": " + msg)

#object existance checks
def _exists(pathobj):
    if os.path.exists(pathobj):
        _bool=' '
        _info("object does" + _bool + "exist: " + pathobj)
        return True
    else:
        _bool=' not '
        _warn("object does" + _bool + "exist: " + pathobj)
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
            _warn("uid does" + _bool + "own object: " + pathobj)
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
            _warn("gid does " + _bool + " own object: " + pathobj)
            return False

#symbolic links (own module?)
