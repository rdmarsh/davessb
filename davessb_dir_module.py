#!/usr/bin/env python3

import os
import davessb_common_module as dcm

#object existance checks
def _dir_does_exist(pathobject):
    if dcm._exists(pathobject):
        return True
    else:
        print ("dir does not exist: " + pathobject)
        return False

def _dir_does_not_exist(pathobject):
    if not dcm._exists(pathobject):
         return True
    else:
         print ("dir does exist: " + pathobject)
         return False

#dir is a dir checks
def _dir_is_a_dir(pathobject):
    if _dir_does_exist(pathobject):
        if os.path.isdir(pathobject):
            return True
        else:
            print ("dir is not a dir: " + pathobject)
            return False
    else:
        return False

def _dir_is_not_a_dir(pathobject):
    if _dir_does_exist(pathobject):
        if not os.path.isdir(pathobject):
            return True
        else:
            print ("dir is a dir: " + pathobject)
            return False
    else:
        return False


#dir empty checks
def _dir_is_empty(pathobject):
    if _dir_is_a_dir(pathobject):
        if not os.listdir(pathobject):
        #if os.stat(pathobject).st_size == 0:
            return True
        else:
            print ("dir is not empty: " + pathobject)
            return False
    else:
        return False

def _dir_is_not_empty(pathobject):
    if _dir_is_a_dir(pathobject):
        if os.listdir(pathobject):
        #if os.stat(pathobject).st_size > 0:
            return True
        else:
            print ("dir is not empty: " + pathobject)
            return False
    else:
        return False

#dir owner checks
def _uid_does_own_dir(pathobject):
    if _dir_is_a_dir(pathobject):
        if dcm._uid_owns(pathobject):
            return True
        else:
            print ("uid does not own dir: " + pathobject)
            return False
    else:
        return False

def _uid_does_not_own_dir(pathobject):
    if _dir_is_a_dir(pathobject):
        if not dcm._uid_owns(pathobject):
            return True
        else:
            print ("uid does own dir: " + pathobject)
            return False
    else:
        return False

#dir group checks
def _gid_does_own_dir(pathobject):
    if _dir_is_a_dir(pathobject):
        if dcm._gid_owns(pathobject):
            return True
        else:
            print ("gid does not own dir: " + pathobject)
            return False
    else:
        return False

def _gid_does_not_own_dir(pathobject):
    if _dir_is_a_dir(pathobject):
        if not dcm._gid_owns(pathobject):
            return True
        else:
            print ("gid does own dir: " + pathobject)
            return False
    else:
        return False



#user owns dir
#group owns dir
#dir perms
#can read dirs
