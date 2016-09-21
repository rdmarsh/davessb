#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#only top checks are not infos
#negative checks call positive with 'nots', don't redo checks

import os

import davessb_common_module as dcm
import davessb_object_module as dom

#dir exists and is a correct object checks
def _dir_exists(obj):

    _objadj = 'dir does '
    _objvrb = {}
    _objvrb['exist'] = 'exist '
    _objvrb['dir'] = 'a dir '
    _objsep = ': '

    if (dom._exists(obj) and dom._isdir(obj)):
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._info(msg)
        return False


#dir does not exists or is not a correct object checks
def _not_dir_exists(obj):

    _objadj = 'dir does '
    _objvrb = {}
    _objvrb['exist'] = 'exist '
    _objvrb['dir'] = 'a dir '
    _objsep = ': '

    if not (dom._exists(obj) and dom._isdir(obj)):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._info(msg)
        return False

#dir does exists and is correct owner checks
def _uid_does_own_dir(obj):

    _objadj = 'dir does '
    _objvrb = {}
    _objvrb['exist'] = 'exist '
    _objvrb['own'] = 'owned by uid '
    _objsep = ': '

    if (_dir_exists(obj) and dom._uid_owns(obj)):
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._info(msg)
        return False

#dir does not exists or is not correct owner checks
def _uid_does_not_own_dir(obj):

    _objadj = 'dir does '
    _objvrb = {}
    _objvrb['exist'] = 'exist '
    _objvrb['own'] = 'owned by uid '
    _objsep = ': '

    if not (_dir_exists(obj) and dom._uid_owns(obj)):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._info(msg)
        return True
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._info(msg)
        return False


#dave here
#dir empty checks
def _dir_is_empty(obj):
    if _dir_exists(obj):
        if not os.listdir(obj):
        #if os.stat(obj).st_size == 0:
            _bool = ''
            dcm._info("dir is" + _bool + "empty: " + obj)
            return True
        else:
            _bool = 'not '
            dcm._warn("dir is" + _bool + "empty: " + obj)
            return False

def _dir_is_not_empty(obj):
    if _dir_exists(obj):
        if os.listdir(obj):
        #if os.stat(obj).st_size == 0:
            _bool = 'not '
            dcm._info("dir is" + _bool + "empty: " + obj)
            return True
        else:
            _bool = ''
            dcm._warn("dir is" + _bool + "empty: " + obj)
            return False

#dir group checks
def _gid_does_own_dir(obj):
    if _dir_exists(obj):
        if dom._gid_owns(obj):
            _bool = ''
            dcm._info("gid does " + _bool + "own dir: " + obj)
            return True
        else:
            _bool = 'not '
            dcm._warn("gid does " + _bool + "own dir: " + obj)
            return False
    else:
        return False

def _gid_does_not_own_dir(obj):
    if _dir_exists(obj):
        if not dom._gid_owns(obj):
            _bool = 'not '
            dcm._info("gid does " + _bool + "own dir: " + obj)
            return True
        else:
            _bool = ''
            dcm._warn("gid does " + _bool + "own dir: " + obj)
            return False
    else:
        return False

#dir perms
#can read dirs

