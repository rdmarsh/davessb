#!/usr/bin/env python3

import os

#file existance checks
def _file_does_exist(pathfile):
    if os.path.exists(pathfile):
        return True
    else:
        print ("file does not exist: " + pathfile)
        return False

def _file_does_not_exist(pathfile):
    if not os.path.exists(pathfile):
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

