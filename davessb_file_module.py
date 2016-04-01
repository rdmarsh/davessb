#!/usr/bin/env python3

import os
import davessb_common_module as dcm

#object existance checks
def _file_does_exist(pathobject):
    if dcm._exists(pathobject):
        return True
    else:
        print ("file does not exist: " + pathobject)
        return False

def _file_does_not_exist(pathobject):
    if not dcm._exists(pathobject):
         return True
    else:
         print ("file does exist: " + pathobject)
         return False

#file is a file checks
def _file_is_a_file(pathobject):
    if _file_does_exist(pathobject):
        if os.path.isfile(pathobject):
            return True
        else:
            print ("file is not a file: " + pathobject)
            return False
    else:
        return False

def _file_is_not_a_file(pathobject):
    if _file_does_exist(pathobject):
        if not os.path.isfile(pathobject):
            return True
        else:
            print ("file is a file: " + pathobject)
            return False
    else:
        return False


#file empty checks
def _file_is_empty(pathobject):
    if _file_is_a_file(pathobject):
        #if not os.listdir(pathobject):
        if os.stat(pathobject).st_size == 0:
            return True
        else:
            print ("file is not empty: " + pathobject)
            return False
    else:
        return False

def _file_is_not_empty(pathobject):
    if _file_is_a_file(pathobject):
        #if os.listdir(pathobject):
        if os.stat(pathobject).st_size > 0:
            return True
        else:
            print ("file is not empty: " + pathobject)
            return False
    else:
        return False

#file owner checks
def _uid_does_own_file(pathobject):
    if _file_is_a_file(pathobject):
        if dcm._uid_owns(pathobject):
            return True
        else:
            print ("uid does not own file: " + pathobject)
            return False
    else:
        return False

def _uid_does_not_own_file(pathobject):
    if _file_is_a_file(pathobject):
        if not dcm._uid_owns(pathobject):
            return True
        else:
            print ("uid does own file: " + pathobject)
            return False
    else:
        return False

#file group checks
def _gid_does_own_file(pathobject):
    if _file_is_a_file(pathobject):
        if dcm._gid_owns(pathobject):
            return True
        else:
            print ("gid does not own file: " + pathobject)
            return False
    else:
        return False

def _gid_does_not_own_file(pathobject):
    if _file_is_a_file(pathobject):
        if not dcm._gid_owns(pathobject):
            return True
        else:
            print ("gid does own file: " + pathobject)
            return False
    else:
        return False



#user owns file
#group owns file
#file perms
#can read files
