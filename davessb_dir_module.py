#!/usr/bin/env python3

import os

#dir existance checks
def _dir_does_exist(pathdir):
    if os.path.isdir(pathdir):
        return True
    else:
        print ("dir does not exist: " + pathdir)
        return False

def _dir_does_not_exist(pathdir):
    if not os.path.isdir(pathdir):
        return True
    else:
        print ("dir does exist: " + pathdir)
        return False

#dir empty checks
def _dir_is_empty(pathdir):
    if _dir_does_exist(pathdir):
        if not os.listdir(pathdir):
            return True
        else:
            print ("dir is not empty: " + pathdir)
            return False
    else:
        return False

def _dir_is_not_empty(pathdir):
    if _dir_does_exist(pathdir):
        if os.listdir(pathdir):
            return True
        else:
            print ("dir is not empty: " + pathdir)
            return False
    else:
        return False

