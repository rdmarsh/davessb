#!/usr/bin/env python3

import davessb_common_module as dcm
import davessb_dir_module as ddm 
import davessb_file_module as dfm

import os
import settings

def main():

    print ()
    print ()
    print ("----------------------------------------")
    print (" object checks")
    print ("----------------------------------------")
    print ()

    print ()
    print (" --- object exisistance checks --- ")
    print ()

    #these are special and should never be called directly
    print (" positive check ")

    testobj='test_objects/_exists'

    if dcm._exists(testobj):
        _bool=' '
        msg="object does" + _bool + "exist: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="object does" + _bool + "exist: " + testobj
        dcm._fail(msg)

    print ()
    print (" negative check ")

    testobj='test_objects/_exists_not'

    if not dcm._exists(testobj):
        _bool=' not '
        msg="object does" + _bool + "exist: " + testobj
        dcm._pass(msg)
    else:
        _bool=' '
        msg="object does" + _bool + "exist: " + testobj
        dcm._fail(msg)

    print ()
    print (" --- object uid checks --- ")
    print ()

    print (" positive check ")

    testobj='test_objects/_uid_owns'

    if dcm._uid_owns(testobj):
        _bool=' '
        msg="object uid does" + _bool + "own: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="object uid does" + _bool + "own: " + testobj
        dcm._fail(msg)

    print ()
    print (" negative check ")

    testobj='test_objects/_uid_owns_not'

    if not dcm._uid_owns(testobj):
        _bool=' not '
        msg="object uid does" + _bool + "own: " + testobj
        dcm._pass(msg)
    else:
        _bool=' '
        msg="object uid does" + _bool + "own: " + testobj
        dcm._fail(failmsg)

    print ()
    print (" --- object gid checks --- ")
    print ()

    print (" positive check ")

    testobj='test_objects/_gid_owns'

    if dcm._gid_owns(testobj):
        _bool=' '
        msg="object gid does" + _bool + "own: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="object gid does" + _bool + "own: " + testobj
        dcm._fail(msg)

    print ()
    print (" negative check ")

    testobj='test_objects/_gid_owns_not'

    if not dcm._gid_owns(testobj):
        _bool=' not '
        msg="object gid does" + _bool + "own: " + testobj
        dcm._pass(msg)
    else:
        _bool=' '
        msg="object gid does" + _bool + "own: " + testobj
        dcm._fail(failmsg)

    print ()
    print ("----------------------------------------")
    print (" dir checks")
    print ("----------------------------------------")
    print ()

    print ()
    print (" --- dir exisistance and is a dir checks --- ")
    print ()

    testobj='test_objects/_dir_does_exst'
    passmsg='dir does exist: ' + testobj
    failmsg='dir does not exist: ' + testobj

    if ddm._dir_does_exist(testobj):
        dcm._pass(passmsg)
    else:
        dcm._fail(failmsg)

    print ()

    testobj='test_objects/_dir_does_not_exist'
    passmsg='dir does not exist: ' + testobj
    failmsg='dir does exist: ' + testobj

    if ddm._dir_does_not_exist(testobj):
        dcm._pass(passmsg)
    else:
        dcm._fail(failmsg)

    print ()
    print (" --- dir uid checks --- ")
    print ()

    pos_test_obj='test_objects/uid_does_own_dir'
    neg_test_obj='test_objects/uid_does_own_dir'

    passmsg='uid_does_own_dirot exist: ' + testobj
    failmsg='dir does exist: ' + testobj

    testnme='uid_does_not_own_dir'
    testobj='test_objects/' + testnme
    passmsg=testnme + ': ' + testobj
    failmsg='dir not owned by uid: ' + testobj

    if ddm._uid_does_own_dir(testobj):
        dcm._pass(passmsg)
    else:
        dcm._fail(failmsg)

    testobj='test_objects/uid_does_not_own_dir'
    passmsg='dir not owned by uid: ' + testobj
    failmsg='dir owned by uid: ' + testobj

    if ddm._uid_does_not_own_dir(testobj):
        dcm._pass(passmsg)
    else:
        dcm._fail(failmsg)

    print ()
    print (" --- dir gid checks --- ")
    print ()

    testobj=('test_objects/gid_does_own_dir')
    if ddm._gid_does_own_dir(testobj):
        dcm._pass("gid does own dir: " + testobj)
    else:

    testobj=('test_objects/gid_does_not_own_dir')
    if ddm._gid_does_not_own_dir(testobj):
        dcm._pass("gid does not own dir: " + testobj)
    else:

    print ()
    print (" --- dir contents checks --- ")
    print ()

    testobj='test_objects/dir_is_empty'
    passmsg='dir is empty: ' + testobj
    failmsg='dir is not empty: ' + testobj

    if ddm._dir_is_empty(testobj):
        dcm._pass(passmsg)
    else:
        dcm._fail(failmsg)

    print ()

    testobj='test_objects/dir_is_not_empty'
    passmsg='dir is not empty: ' + testobj
    failmsg='dir is empty: ' + testobj

    if ddm._dir_is_not_empty(testobj):
        dcm._pass(passmsg)
    else:
        dcm._fail(failmsg)

    print ()
    print ()
    print ("----------------------------------------")
    print (" file checks")
    print ("----------------------------------------")
    print ()

    print ()
    print (" --- file existance checks --- ")
    print ()

    testobj=('test_objects/file_does_not_exst')
    if dfm._file_does_not_exist(testobj):
        dcm._pass("file does not exist: " + testobj)
    else:

    testobj=('test_objects/file_does_exist')
    if dfm._file_does_exist(testobj):
        dcm._pass("file does exist: " + testobj)
    else:

    print ()
    print (" --- file is a file checks --- ")
    print ()

    testobj=('test_objects/file_is_not_a_file')
    if dfm._file_is_not_a_file(testobj):
        dcm._pass("file is not a file: " + testobj)
    else:

    testobj=('test_objects/file_is_a_file')
    if dfm._file_is_a_file(testobj):
        dcm._pass("file is a file: " + testobj)
    else:

    print ()
    print (" --- file contents checks --- ")
    print ()

    testobj=('test_objects/file_is_empty')
    if dfm._file_is_empty(testobj):
        dcm._pass("file is empty: " + testobj)
    else:

    testobj=('test_objects/file_is_not_empty')
    if dfm._file_is_not_empty(testobj):
        dcm._pass("file is not empty: " + testobj)
    else:

    print ()
    print (" --- file owner checks --- ")
    print ()

    testobj=('test_objects/uid_does_own_file')
    if dfm._uid_does_own_file(testobj):
        dcm._pass("uid does own file: " + testobj)
    else:

    testobj=('test_objects/uid_does_not_own_file')
    if dfm._uid_does_not_own_file(testobj):
        dcm._pass("uid does not own file: " + testobj)
    else:

    print ()
    print (" --- file group checks --- ")
    print ()

    testobj=('test_objects/gid_does_own_file')
    if dfm._gid_does_own_file(testobj):
        dcm._pass("gid does own file: " + testobj)
    else:

    testobj=('test_objects/gid_does_not_own_file')
    if dfm._gid_does_not_own_file(testobj):
        dcm._pass("gid does not own file: " + testobj)
    else:


if __name__ == "__main__":
    print ()
    print ("########################################")
    print ()

    main()

    print ()
    print ("########################################")
    print ()

