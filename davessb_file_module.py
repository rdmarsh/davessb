#!/usr/bin/env python3

#only deepest tests get to say anything or return anything

import os

import davessb_common_module as dcm
import davessb_object_module as dom

#object existence checks
def _file_does_exist(pathobj):
    if dom._exists(pathobj):
        dcm._fail("file does exist: " + pathobj)
        return True
    else:
        dcm._fail("file does not exist: " + pathobj)
        return False

def _file_does_not_exist(pathobj):
    if not _file_does_exist(pathobj):
         dcm._fail("file does not exist: " + pathobj)
         return True
    else:
         dcm._fail("file does exist: " + pathobj)
         return False

#file is a file checks
def _file_is_a_file(pathobj):
    if _file_does_exist(pathobj):
        if os.path.isfile(pathobj):
            dcm._fail("file is a file: " + pathobj)
            return True
        else:
            dcm._fail("file is not a file: " + pathobj)
            return False

def _file_is_not_a_file(pathobj):
    if not _file_does_exist(pathobj):
        return True
        dcm._fail("file is not a file: " + pathobj)
    else:
        dcm._fail("file is a file: " + pathobj)
        return False


#file empty checks
def _file_is_empty(pathobj):
    if _file_is_a_file(pathobj):
        #if not os.listdir(pathobj):
        if os.stat(pathobj).st_size == 0:
            dcm._fail("file is empty: " + pathobj)
            return True
        else:
            dcm._fail("file is not empty: " + pathobj)
            return False

def _file_is_not_empty(pathobj):
    if _file_is_a_file(pathobj):
        #if os.listdir(pathobj):
        if os.stat(pathobj).st_size > 0:
            return True
        else:
            dcm._fail("file is not empty: " + pathobj)
            return False
    else:
        return False

#file owner checks
def _uid_does_own_file(pathobj):
    if _file_is_a_file(pathobj):
        if dom._uid_owns(pathobj):
            return True
        else:
            dcm._fail("uid does not own file: " + pathobj)
            return False
    else:
        return False

def _uid_does_not_own_file(pathobj):
    if _file_is_a_file(pathobj):
        if not dom._uid_owns(pathobj):
            return True
        else:
            dcm._fail("uid does own file: " + pathobj)
            return False
    else:
        return False

#file group checks
def _gid_does_own_file(pathobj):
    if _file_is_a_file(pathobj):
        if dom._gid_owns(pathobj):
            return True
        else:
            dcm._fail("gid does not own file: " + pathobj)
            return False
    else:
        return False

def _gid_does_not_own_file(pathobj):
    if _file_is_a_file(pathobj):
        if not dom._gid_owns(pathobj):
            return True
        else:
            dcm._fail("gid does own file: " + pathobj)
            return False
    else:
        return False



#file perms
#can read files
