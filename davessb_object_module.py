#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#only top checks are not infos
#negative checks call positive with 'nots', don't redo checks

import os

import davessb_common_module as dcm

#object existance check, normally not called directly
def _exists(obj):
    if os.path.exists(obj):
        _bool=' '
        msg="object does" + _bool + "exist: " + obj
        dcm._info(msg)
        return True
    else:
        _bool=' not '
        msg="object does" + _bool + "exist: " + obj
        dcm._info(msg)
        return False

#object type check, normally not called directly
def _isdir(obj):
    if os.path.isdir(obj):
        _bool=' '
        msg="object is" + _bool + "a dir: " + obj
        dcm._info(msg)
        return True
    else:
        _bool=' not '
        msg="object is" + _bool + "a dir: " + obj
        dcm._info(msg)
        return False

#object type check, normally not called directly
def _isfile(obj):
    if os.path.isfile(obj):
        _bool=' '
        msg="object is" + _bool + "a file: " + obj
        dcm._info(msg)
        return True
    else:
        _bool=' not '
        msg="object is" + _bool + "a file: " + obj
        dcm._info(msg)
        return False

#todo, call below and test existence or lack of it
#def _dir_exists(obj):
#def _file_exists

#object user owner checks
def _uid_owns(obj):
    if os.stat(obj).st_uid == os.getuid():
        _bool=' '
        msg="object is" + _bool + "owned by uid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool=' not '
        msg="object is" + _bool + "owned by uid: " + obj
        dcm._info(msg)
        return False

#object group owner checks
def _gid_owns(obj):
    if os.stat(obj).st_gid == os.getgid():
        _bool=' '
        msg="object is" + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool=' not '
        msg="object is" + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return False

#object user and group owner checks
def _id_owns(obj):
    if _uid_owns(obj) and _gid_owns(obj):
        _bool=' '
        _junct=' and '
        msg="object is" + _bool + "owned by uid" + _junct + "gid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool=' not '
        _junct=' or '
        msg="object is" + _bool + "owned by uid" + _junct + "gid: " + obj
        dcm._info(msg)
        return False

#
# os.getegid
# 
