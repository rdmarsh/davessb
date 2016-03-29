#!/usr/bin/env python3

import os

#dir existance checks
def _dir_does_exist(pathdir):
    if os.path.exists(pathdir):
        return True
    else:
        print ("dir does not exist: " + pathdir)
        return False

def _dir_does_not_exist(pathdir):
    if not os.path.exists(pathdir):
        return True
    else:
        print ("dir does exist: " + pathdir)
        return False


#dir is a dir checks
def _dir_is_a_dir(pathdir):
    if _dir_does_exist(pathdir):
        if os.path.isdir(pathdir):
            return True
        else:
            print ("dir is not a dir: " + pathdir)
            return False
    else:
        return False

def _dir_is_not_a_dir(pathdir):
    if _dir_does_exist(pathdir):
        if not os.path.isdir(pathdir):
            return True
        else:
            print ("dir is a dir: " + pathdir)
            return False
    else:
        return False


#dir empty checks
def _dir_is_empty(pathdir):
    if _dir_is_a_dir(pathdir):
        if not os.listdir(pathdir):
            return True
        else:
            print ("dir is not empty: " + pathdir)
            return False
    else:
        return False

def _dir_is_not_empty(pathdir):
    if _dir_is_a_dir(pathdir):
        if os.listdir(pathdir):
            return True
        else:
            print ("dir is not empty: " + pathdir)
            return False
    else:
        return False

#dir owner checks
def _uid_does_own_dir(pathdir):
    if _dir_is_a_dir(pathdir):
        if os.stat(pathdir).st_uid == os.getuid():
            return True
        else:
            print ("uid does not own dir: " + pathdir)
            return False
    else:
        return False

def _uid_does_not_own_dir(pathdir):
    if _dir_is_a_dir(pathdir):
        if os.stat(pathdir).st_uid != os.getuid():
            return True
        else:
            print ("uid does own dir: " + pathdir)
            return False
    else:
        return False

#dir group checks
def _gid_does_own_dir(pathdir):
    if _dir_is_a_dir(pathdir):
        if os.stat(pathdir).st_gid == os.getgid():
            return True
        else:
            print ("gid does not own dir: " + pathdir)
            return False
    else:
        return False

def _gid_does_not_own_dir(pathdir):
    if _dir_is_a_dir(pathdir):
        if os.stat(pathdir).st_gid != os.getgid():
            return True
        else:
            print ("gid does own dir: " + pathdir)
            return False
    else:
        return False



#user owns dir
#group owns dir
#dir perms
#can read dirs
