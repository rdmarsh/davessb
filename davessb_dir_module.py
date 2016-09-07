#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#only top checks are not infos
#negative checks call positive with 'nots', don't redo checks

import os

import davessb_common_module as dcm
import davessb_object_module as dom

#dir exists and is a correct object checks
def _dir_exists(pathobj):
    if (dom._exists(pathobj) and dom._isdir(pathobj)):
        _bool = ''
        _junct = 'and '
        dcm._info("dir does " + _bool + "exist " + _junct + "is " + _bool + "a dir: " + pathobj)
        return True
    else:
        _bool = 'not '
        _junct = 'or '
        dcm._info("dir does " + _bool + "exist " + _junct + "is " + _bool + "a dir: " + pathobj)
        return False

def _not_dir_exists(pathobj):
    if not _dir_exists(pathobj):
        return True
    else:
        return False

#dir empty checks
def _dir_is_empty(pathobj):
    if _dir_exists(pathobj):
        if not os.listdir(pathobj):
        #if os.stat(pathobj).st_size == 0:
            _bool = ''
            dcm._info("dir is" + _bool + "empty: " + pathobj)
            return True
        else:
            _bool = 'not '
            dcm._warn("dir is" + _bool + "empty: " + pathobj)
            return False

def _dir_is_not_empty(pathobj):
    if _dir_exists(pathobj):
        if os.listdir(pathobj):
        #if os.stat(pathobj).st_size == 0:
            _bool = 'not '
            dcm._info("dir is" + _bool + "empty: " + pathobj)
            return True
        else:
            _bool = ''
            dcm._warn("dir is" + _bool + "empty: " + pathobj)
            return False

#dir owner checks
def _uid_does_own_dir(pathobj):
    if _dir_exists(pathobj):
        if dcm._uid_owns(pathobj):
            _bool = ''
            dcm._info("uid does " + _bool + "own dir: " + pathobj)
            return True
        else:
            _bool = 'not '
            dcm._warn("uid does " + _bool + "own dir: " + pathobj)
            return False
    else:
        return False

def _uid_does_not_own_dir(pathobj):
    if not _uid_does_own_dir(pathobj):
        if not dom._uid_owns(pathobj):
            _bool = 'not '
            dcm._info("uid does " + _bool + "own dir: " + pathobj)
            return True
        else:
            _bool = ''
            dcm._warn("uid does " + _bool + "own dir: " + pathobj)
            return False
    else:
        return False

#dir group checks
def _gid_does_own_dir(pathobj):
    if _dir_exists(pathobj):
        if dom._gid_owns(pathobj):
            _bool = ''
            dcm._info("gid does " + _bool + "own dir: " + pathobj)
            return True
        else:
            _bool = 'not '
            dcm._warn("gid does " + _bool + "own dir: " + pathobj)
            return False
    else:
        return False

def _gid_does_not_own_dir(pathobj):
    if _dir_exists(pathobj):
        if not dom._gid_owns(pathobj):
            _bool = 'not '
            dcm._info("gid does " + _bool + "own dir: " + pathobj)
            return True
        else:
            _bool = ''
            dcm._warn("gid does " + _bool + "own dir: " + pathobj)
            return False
    else:
        return False

#dir perms
#can read dirs

