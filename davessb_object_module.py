#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#negative checks call positive with 'nots', don't redo checks

# object-
#dir-does-
#test-yesno-object


import os
import davessb_common_module as dcm


#object existence check, normally not called directly
def _exists(obj):

    _objadj = 'object does '
    _objvrb = 'exist '
    _objsep = ': '

    if os.path.exists(obj):
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object not existence check, normally not called directly
def _not_exists(obj):

    _objadj = 'object does '
    _objvrb = 'exist '
    _objsep = ': '

    if not _exists(obj):
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object type check, normally not called directly
def _isdir(obj):

    _objadj = 'object is '
    _objvrb = 'a dir '
    _objsep = ': '

    if os.path.isdir(obj):
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object not type check, normally not called directly
def _not_isdir(obj):

    _objadj = 'object is '
    _objvrb = 'a dir '
    _objsep = ': '

    if not _isdir(obj):
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object type check, normally not called directly
def _isfile(obj):

    _objadj = 'object is '
    _objvrb = 'a file '
    _objsep = ': '

    if os.path.isfile(obj):
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object type check, normally not called directly
def _not_isfile(obj):

    _objadj = 'object is '
    _objvrb = 'a file '
    _objsep = ': '

    if not _isfile(obj):
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object user owner checks
def _uid_owns(obj):

    _objadj = 'object is '
    _objvrb = 'owned by uid '
    _objsep = ': '

    if os.stat(obj).st_uid == os.getuid():
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object user not owner checks
def _not_uid_owns(obj):

    _objadj = 'object is '
    _objvrb = 'owned by uid '
    _objsep = ': '

    if not _uid_owns(obj):
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object group owner checks
def _gid_owns(obj):

    _objadj = 'object is '
    _objvrb = 'owned by gid '
    _objsep = ': '

    if os.stat(obj).st_gid == os.getgid():
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object group not owner checks
def _not_gid_owns(obj):

    _objadj = 'object is '
    _objvrb = 'owned by gid '
    _objsep = ': '

    if not _gid_owns(obj):
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._info(msg)
        return False

#object user and group owner checks
def _id_owns(obj):

    _objadj = 'object is '
    _objvrb = {}
    _objvrb['uid'] = 'owned by uid '
    _objvrb['gid'] = 'owned by gid '
    _objsep = ': '

    if _uid_owns(obj) and _gid_owns(obj):
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] +  _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
        dcm._info(msg)
        return False


#object user and group not owner checks
def _not_id_owns(obj):

    _objadj = 'object is '
    _objvrb = {}
    _objvrb['uid'] = 'owned by uid '
    _objvrb['gid'] = 'owned by gid '
    _objsep = ': '

    if not _uid_owns(obj) or not _gid_owns(obj):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
        dcm._info(msg)
        return False

