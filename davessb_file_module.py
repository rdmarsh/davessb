#!/usr/bin/env python3

import os

#file existance checks
def _file_does_exist(pathfile):
    if os.path.isfile(pathfile):
        return True
    else:
        print ("file does not exist: " + pathfile)
        return False

def _file_does_not_exist(pathfile):
    if not os.path.isfile(pathfile):
        return True
    else:
        print ("file does exist: " + pathfile)
        return False

#file empty checks
def _file_is_empty(pathfile):
    if _file_does_exist(pathfile):
        if os.stat(pathfile).st_size == 0:
            return True
        else:
            print ("file is not empty: " + pathfile)
            return False
    else:
        return False

def _file_is_not_empty(pathfile):
    if _file_does_exist(pathfile):
        if os.stat(pathfile).st_size > 0:
            return True
        else:
            print ("file is not empty: " + pathfile)
            return False
    else:
        return False

#file owner checks
def _uid_does_own_file(pathfile):
    if _file_does_exist(pathfile):
        if os.stat(pathfile).st_uid == os.getuid():
            return True
        else:
            print ("uid does not own file: " + pathfile)
            return False
    else:
        return False

def _uid_does_not_own_file(pathfile):
    if _file_does_exist(pathfile):
        if os.stat(pathfile).st_uid != os.getuid():
            return True
        else:
            print ("uid does own file: " + pathfile)
            return False
    else:
        return False


#user owns file
#group owns file
#file perms
#can read files
