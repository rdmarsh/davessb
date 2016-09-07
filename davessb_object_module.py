#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#negative checks call positive with 'nots', don't redo checks

import os

import davessb_common_module as dcm

#object existence check, normally not called directly
def _exists(obj):
    if os.path.exists(obj):
        _bool = ''
        msg = "object does " + _bool + "exist: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = "object does " + _bool + "exist: " + obj
        dcm._info(msg)
        return False

#object not existence check, normally not called directly
def _not_exists(obj):
    if not _exists(obj):
        _bool = 'not '
        msg = "object does " + _bool + "exist: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = "object does " + _bool + "exist: " + obj
        dcm._info(msg)
        return False

#object type check, normally not called directly
def _isdir(obj):
    if os.path.isdir(obj):
        _bool = ''
        msg = "object is " + _bool + "a dir: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = "object is " + _bool + "a dir: " + obj
        dcm._info(msg)
        return False

#object not type check, normally not called directly
def _not_isdir(obj):
    if not _isdir(obj):
        _bool = 'not '
        msg = "object is " + _bool + "a dir: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = "object is " + _bool + "a dir: " + obj
        dcm._info(msg)
        return False

#object type check, normally not called directly
def _isfile(obj):
    if os.path.isfile(obj):
        _bool = ''
        msg = "object is " + _bool + "a file: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = "object is " + _bool + "a file: " + obj
        dcm._info(msg)
        return False

#object type check, normally not called directly
def _not_isfile(obj):
    if not _isfile(obj):
        _bool = 'not '
        msg = "object is " + _bool + "a file: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = "object is " + _bool + "a file: " + obj
        dcm._info(msg)
        return False

#object user owner checks
def _uid_owns(obj):
    if os.stat(obj).st_uid == os.getuid():
        _bool = ''
        msg = "object is " + _bool + "owned by uid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = "object is " + _bool + "owned by uid: " + obj
        dcm._info(msg)
        return False

#object user not owner checks
def _not_uid_owns(obj):
    if not _uid_owns(obj):
        _bool = 'not '
        msg = "object is " + _bool + "owned by uid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = "object is " + _bool + "owned by uid: " + obj
        dcm._info(msg)
        return False

#object group owner checks
def _gid_owns(obj):
    if os.stat(obj).st_gid == os.getgid():
        _bool = ''
        msg = "object is " + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = "object is " + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return False

#object group not owner checks
def _not_gid_owns(obj):
    if not _gid_owns(obj):
        _bool = 'not '
        msg = "object is " + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = "object is " + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return False

#object user and group owner checks
def _id_owns(obj):
    if _uid_owns(obj) and _gid_owns(obj):
        _bool = ''
        _junct = 'and '
        msg = "object is " + _bool + "owned by uid " + _junct + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        _junct = 'or '
        msg = "object is " + _bool + "owned by uid " + _junct + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return False

#object user and group not owner checks
def _not_id_owns(obj):
    if not _uid_owns(obj) or not _gid_owns(obj):
        _bool = 'not '
        _junct = 'and '
        msg = "object is " + _bool + "owned by uid " + _junct + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        _junct = 'or '
        msg = "object is " + _bool + "owned by uid " + _junct + _bool + "owned by gid: " + obj
        dcm._info(msg)
        return False
 
