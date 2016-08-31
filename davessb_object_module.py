#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#only top checks are not infos
#negative checks call positive with 'nots', don't redo checks

import os

import davessb_common_module as dcm

#object existance check, normally not called directly
def _exists(pathobj):
    if os.path.exists(pathobj):
        _bool=' '
        dcm._info("object does" + _bool + "exist: " + pathobj)
        return True
    else:
        _bool=' not '
        dcm._info("object does" + _bool + "exist: " + pathobj)
        return False

#object type check, normally not called directly
def _isdir(pathobj):
    if os.path.isdir(pathobj):
        _bool=' '
        dcm._info("object is" + _bool + "a dir: " + pathobj)
        return True
    else:
        _bool=' not '
        dcm._info("object is" + _bool + "a dir: " + pathobj)
        return False

#object type check, normally not called directly
def _isfile(pathobj):
    if os.path.isfile(pathobj):
        _bool=' '
        dcm._info("object is" + _bool + "a file: " + pathobj)
        return True
    else:
        _bool=' not '
        dcm._info("object is" + _bool + "a file: " + pathobj)
        return False

#object type check, normally not called directly
def _islink(pathobj):
    if os.path.islink(pathobj):
        _bool=' '
        dcm._info("object is" + _bool + "a link: " + pathobj)
        return True
    else:
        _bool=' not '
        dcm._info("object is" + _bool + "a link: " + pathobj)
        return False

#todo, call below and test existence or lack of it
#def _dir_exists(pathobj):
#def _file_exists
#def _link_exists


#object user owner checks
def _uid_owns(pathobj):
    if _exists(pathobj):
        if os.stat(pathobj).st_uid == os.getuid():
            _bool=' '
            dcm._info("uid does" + _bool + "own object: " + pathobj)
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
            dcm._info("gid does" + _bool + "own object: " + pathobj)
            return True
        else:
            _bool=' not '
            _warn("gid does " + _bool + " own object: " + pathobj)
            return False

#
# os.getegid
# 
