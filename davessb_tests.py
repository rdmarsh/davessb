#!/usr/bin/env python3

import os
import settings

import davessb_common_module as dcm
import davessb_object_module as dom
import davessb_dir_module as ddm 
import davessb_file_module as dfm


## dcm module checks

def _msg_checks():
    print ()
    print (" --- messages tests --- ")
    print ()

    print (" basic message test ")
    print ()

    dcm._info("info test message")
    dcm._pass("pass test message")
    dcm._warn("warn test message")
    dcm._fail("fail test message")
    dcm._halt("halt test message")

    print ()
    print (" blank message test ")
    print ()

    dcm._info("")
    dcm._pass("")
    dcm._warn("")
    dcm._fail("")
    dcm._halt("")

    print ()
    print (" null message tests ")
    print ()

    dcm._info()
    dcm._pass()
    dcm._warn()
    dcm._fail()
    dcm._halt()


## dom module checks

#only check existence
def _exists_checks():
    #these are special and should never be called directly
    print ()
    print (" --- object existence checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_exists'

    if dom._exists(testobj):
        _bool=' '
        msg="object does" + _bool + "exist: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="object does" + _bool + "exist: " + testobj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_exists_not'

    if not dom._exists(testobj):
        _bool=' not '
        msg="object does" + _bool + "exist: " + testobj
        dcm._pass(msg)
    else:
        _bool=' '
        msg="object does" + _bool + "exist: " + testobj
        dcm._fail(msg)
        raise SystemExit

#only check not existence
def _not_exists_checks():
    #these are special and should never be called directly
    print ()
    print (" --- object not existence checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_exists_not'

    if dom._not_exists(testobj):
        _bool=' not '
        msg="object does" + _bool + "exist: " + testobj
        dcm._pass(msg)
    else:
        _bool=' '
        msg="object does" + _bool + "exist: " + testobj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_exists'

    if not dom._not_exists(testobj):
        _bool=' '
        msg="object does" + _bool + "exist: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="object does" + _bool + "exist: " + testobj
        dcm._fail(msg)
        raise SystemExit

#only check type, existence check is just for us
def _isdir_checks():
    print ()
    print (" --- dir type checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_isdir'

    if dom._exists(testobj):
        if dom._isdir(testobj):
            _bool=' '
            msg="object is" + _bool + "a dir: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            msg="object is" + _bool + "a dir: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_isdir_not'

    if dom._exists(testobj):
        if not dom._isdir(testobj):
            _bool=' not '
            msg="object is" + _bool + "a dir: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="object is" + _bool + "a dir: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check type, existence check is just for us
def _not_isdir_checks():
    print ()
    print (" --- not dir type checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_isdir_not'

    if dom._exists(testobj):
        if dom._not_isdir(testobj):
            _bool=' not '
            msg="object is" + _bool + "a dir: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="object is" + _bool + "a dir: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_isdir'

    if dom._exists(testobj):
        if not dom._not_isdir(testobj):
            _bool=' '
            msg="object is" + _bool + "a dir: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            msg="object is" + _bool + "a dir: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check type, existence check is just for us
def _isfile_checks():
    print ()
    print (" --- file type checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_isfile'

    if dom._exists(testobj):
        if dom._isfile(testobj):
            _bool=' '
            msg="object is" + _bool + "a file: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            msg="object is" + _bool + "a file: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_isfile_not'

    if dom._exists(testobj):
        if not dom._isfile(testobj):
            _bool=' not '
            msg="object is" + _bool + "a file: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="object is" + _bool + "a file: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check type, existence check is just for us
def _not_isfile_checks():
    print ()
    print (" --- not file type checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_isfile_not'

    if dom._exists(testobj):
        if dom._not_isfile(testobj):
            _bool=' not '
            msg="object is" + _bool + "a file: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="object is" + _bool + "a file: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_isfile'

    if dom._exists(testobj):
        if not dom._not_isfile(testobj):
            _bool=' '
            msg="object is" + _bool + "a file: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            msg="object is" + _bool + "a file: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check uid, existence check is just for us
def _uid_owns_checks():
    print ()
    print (" --- object uid owns checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_uid_owns'

    if dom._exists(testobj):
        if dom._uid_owns(testobj):
            _bool=' '
            msg="object is" + _bool + "owned by uid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            msg="object is" + _bool + "owned by uid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_uid_owns_not'

    if dom._exists(testobj):
        if not dom._uid_owns(testobj):
            _bool=' not '
            msg="object is" + _bool + "owned by uid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="object is" + _bool + "owned by uid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check uid, existence check is just for us
def _not_uid_owns_checks():
    print ()
    print (" --- object uid not owns checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_uid_owns_not'

    if dom._exists(testobj):
        if dom._not_uid_owns(testobj):
            _bool=' not '
            msg="object is" + _bool + "owned by uid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="object is" + _bool + "owned by uid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_uid_owns'

    if dom._exists(testobj):
        if not dom._not_uid_owns(testobj):
            _bool=' '
            msg="object is" + _bool + "owned by uid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            msg="object is" + _bool + "owned by uid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check gid, existence check is just for us
def _gid_owns_checks():
    print ()
    print (" --- object gid owns checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_gid_owns'

    if dom._exists(testobj):
        if dom._gid_owns(testobj):
            _bool=' '
            msg="object is" + _bool + "owned by gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            msg="object is" + _bool + "owned by gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_gid_owns_not'

    if dom._exists(testobj):
        if not dom._gid_owns(testobj):
            _bool=' not '
            msg="object is" + _bool + "owned by gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="object is" + _bool + "owned by gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check gid, existence check is just for us
def _not_gid_owns_checks():
    print ()
    print (" --- object gid not owns checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_gid_owns_not'

    if dom._exists(testobj):
        if dom._not_gid_owns(testobj):
            _bool=' not '
            msg="object is" + _bool + "owned by gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="object is" + _bool + "owned by gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_gid_owns'

    if dom._exists(testobj):
        if not dom._not_gid_owns(testobj):
            _bool=' '
            msg="object is" + _bool + "owned by gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            msg="object is" + _bool + "owned by gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check id, existence check is just for us
def _id_owns_checks():
    print ()
    print (" --- object id owns checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_id_owns'

    if dom._exists(testobj):
        if dom._id_owns(testobj):
            _bool=' '
            _junct=' and '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            _junct=' or '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative checks (uid)")
    print ()

    testobj='test_objects/_id_uid_owns_not'

    if dom._exists(testobj):
        if not dom._id_owns(testobj):
            _bool=' not '
            _junct=' or '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            _junct=' and '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative checks (gid)")
    print ()

    testobj='test_objects/_id_gid_owns_not'

    if dom._exists(testobj):
        if not dom._id_owns(testobj):
            _bool=' not '
            _junct=' or '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            _junct=' and '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative checks (uid and gid)")
    print ()

    testobj='test_objects/_id_uid_gid_owns_not'

    if dom._exists(testobj):
        if not dom._id_owns(testobj):
            _bool=' not '
            _junct=' or '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            _junct=' and '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#only check id, existence check is just for us
def _not_id_owns_checks():
    print ()
    print (" --- object id not owns checks --- ")
    print ()

    print (" positive checks (uid)")
    print ()

    testobj='test_objects/_id_uid_owns_not'

    if dom._exists(testobj):
        if dom._not_id_owns(testobj):
            _bool=' not '
            _junct=' and '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            _junct=' or '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" positive checks (gid)")
    print ()

    testobj='test_objects/_id_gid_owns_not'

    if dom._exists(testobj):
        if dom._not_id_owns(testobj):
            _bool=' not '
            _junct=' and '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            _junct=' or '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" positive checks (uid and gid)")
    print ()

    testobj='test_objects/_id_uid_gid_owns_not'

    if dom._exists(testobj):
        if dom._not_id_owns(testobj):
            _bool=' not '
            _junct=' and '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            _junct=' or '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_id_owns'

    if dom._exists(testobj):
        if not dom._not_id_owns(testobj):
            _bool=' '
            _junct=' or '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._pass(msg)
        else:
            _bool=' not '
            _junct=' and '
            msg="object is" + _bool + "owned by uid" + _junct + "gid: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit


## ddm module checks

#existence checks are incorporated into these tests
def _dir_exists_checks():
    print ()
    print (" --- dir existence and is a dir checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_dir_exists'

    if ddm._dir_does_exist(testobj):
        _bool=' '
        msg="dir does" + _bool + "exist: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="dir does" + _bool + "exist: " + testobj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative checks (not exists)")
    print ()

    testobj='test_objects/_dir_exists_not'

    if not ddm._dir_does_exist(testobj):
        _bool=' not '
        msg="dir does" + _bool + "exist: " + testobj
        dcm._pass(msg)
    else:
        _bool=' '
        msg="dir does" + _bool + "exist: " + testobj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative checks (not dir)")
    print ()

    testobj='test_objects/_dir_isdir_not'

    #existence check is just for us
    if dom._exists(testobj):
        if not ddm._dir_does_exist(testobj):
            _bool=' not '
            msg="dir does" + _bool + "exist: " + testobj
            dcm._pass(msg)
        else:
            _bool=' '
            msg="dir does" + _bool + "exist: " + testobj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing: " + testobj)
        raise SystemExit

#existence checks are incorporated into these tests
def _dir_uid_checks():
    print ()
    print (" --- dir uid owns checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_uid_does_own_dir'

    if ddm._uid_does_own_dir(testobj):
        _bool=' not '
        msg="uid does" + _bool + "own dir: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="uid does" + _bool + "own dir: " + testobj
        dcm._fail(msg)

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_uid_does_not_own_dir'

    if not ddm._uid_does_own_dir(testobj):
        _bool=' not '
        msg="uid does" + _bool + "own dir: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="uid does" + _bool + "own dir: " + testobj
        dcm._fail(msg)

def _dir_gid_checks():
    print ()
    print (" --- dir gid owns checks --- ")
    print ()

    print (" positive check ")
    print ()

    testobj='test_objects/_gid_does_own_dir'

    if ddm._gid_does_own_dir(testobj):
        _bool=' not '
        msg="gid does" + _bool + "own dir: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="gid does" + _bool + "own dir: " + testobj
        dcm._fail(msg)

    print ()
    print (" negative check ")
    print ()

    testobj='test_objects/_gid_does_not_own_dir'

    if not ddm._gid_does_own_dir(testobj):
        _bool=' not '
        msg="gid does" + _bool + "own dir: " + testobj
        dcm._pass(msg)
    else:
        _bool=' not '
        msg="gid does" + _bool + "own dir: " + testobj
        dcm._fail(msg)

def main():

    print ()

    print ()
    print ("----------------------------------------")
    print (" common checks")
    print ("----------------------------------------")
    print ()

    _msg_checks()

    print ()
    print ("----------------------------------------")
    print (" object checks")
    print ("----------------------------------------")
    print ()

    _exists_checks()
    _not_exists_checks()

    _isdir_checks()
    _not_isdir_checks()

    _isfile_checks()
    _not_isfile_checks()

    _uid_owns_checks()
    _not_uid_owns_checks()

    _gid_owns_checks()
    _not_gid_owns_checks()

    _id_owns_checks()
    _not_id_owns_checks()

    print ()
    print ("----------------------------------------")
    print (" dir checks")
    print ("----------------------------------------")
    print ()

    _dir_exists_checks()
    _not_dir_exists_checks()

    _uid_owns_dir_checks()
    _not_uid_owns_dir_checks()

    _gid_owns_dir_checks()
    _not_gid_owns_dir_checks()

    _id_owns_dir_checks()
    _not_id_owns_dir_checks()

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
    print (" --- file existence checks --- ")
    print ()

    testobj=('test_objects/file_does_not_exst')
    if dfm._file_does_not_exist(testobj):
        dcm._pass("file does not exist: " + testobj)
    else:
        dcm._fail("file does not exist: " + testobj)

    testobj=('test_objects/file_does_exist')
    if dfm._file_does_exist(testobj):
        dcm._pass("file does exist: " + testobj)
    else:
        dcm._fail("file does exist: " + testobj)

    print ()
    print (" --- file is a file checks --- ")
    print ()

    testobj=('test_objects/file_is_not_a_file')
    if dfm._file_is_not_a_file(testobj):
        dcm._pass("file is not a file: " + testobj)
    else:
        dcm._pass("file is a file: " + testobj)

    testobj=('test_objects/file_is_a_file')
    if dfm._file_is_a_file(testobj):
        dcm._pass("file is a file: " + testobj)
    else:
        dcm._pass("file is not a file: " + testobj)

    print ()
    print (" --- file contents checks --- ")
    print ()

    testobj=('test_objects/file_is_empty')
    if dfm._file_is_empty(testobj):
        dcm._pass("file is empty: " + testobj)
    else:
        dcm._pass("file is empty: " + testobj)

    testobj=('test_objects/file_is_not_empty')
    if dfm._file_is_not_empty(testobj):
        dcm._pass("file is not empty: " + testobj)
    else:
        dcm._pass("file is not empty: " + testobj)

    print ()
    print (" --- file owner checks --- ")
    print ()

    testobj=('test_objects/uid_does_own_file')
    if dfm._uid_does_own_file(testobj):
        dcm._pass("uid does own file: " + testobj)
    else:
        dcm._pass("uid does not own file: " + testobj)

    testobj=('test_objects/uid_does_not_own_file')
    if dfm._uid_does_not_own_file(testobj):
        dcm._pass("uid does not own file: " + testobj)
    else:
        dcm._pass("uid does not own file: " + testobj)

    print ()
    print (" --- file group checks --- ")
    print ()

    testobj=('test_objects/gid_does_own_file')
    if dfm._gid_does_own_file(testobj):
        dcm._pass("gid does own file: " + testobj)
    else:
        dcm._pass("gid does not own file: " + testobj)

    testobj=('test_objects/gid_does_not_own_file')
    if dfm._gid_does_not_own_file(testobj):
        dcm._pass("gid does not own file: " + testobj)
    else:
        dcm._pass("gid does  own file: " + testobj)


if __name__ == "__main__":
    print ()
    print ("########################################")
    print ()

    main()

    print ()
    print ("########################################")
    print ()

    raise SystemExit
