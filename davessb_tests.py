#!/usr/bin/env python3

import os
import settings

import davessb_common_module as dcm
import davessb_object_module as dom
import davessb_dir_module as ddm
import davessb_file_module as dfm


# dcm module checks

def _msg_checks():
    """Test message functions with and without parameters"""
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


# dom module checks

# only check existence
def _exists_checks():
    # these are special and should never be called directly
    print ()
    print (" --- object existence checks --- ")
    print ()

    _objadj = 'object does '
    _objvrb = 'exist '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_exists'

    if dom._exists(obj):
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_exists_not'

    if not dom._exists(obj):
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._fail(msg)
        raise SystemExit


# only check not existence
def _not_exists_checks():
    # these are special and should never be called directly
    print ()
    print (" --- object not existence checks --- ")
    print ()

    _objadj = 'object does '
    _objvrb = 'exist '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_exists_not'

    if dom._not_exists(obj):
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_exists'

    if not dom._not_exists(obj):
        _bool = ''
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = 'not '
        msg = _objadj + _bool + _objvrb + _objsep + obj
        dcm._fail(msg)
        raise SystemExit


# this only checks type, not existence
def _isdir_checks():
    print ()
    print (" --- dir type checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = 'a dir '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_isdir'

    # existence check is just for us
    if dom._exists(obj):
        if dom._isdir(obj):
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_isdir_not'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._isdir(obj):
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _not_isdir_checks():
    print ()
    print (" --- not dir type checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = 'a dir '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_isdir_not'

    # existence check is just for us
    if dom._exists(obj):
        if dom._not_isdir(obj):
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_isdir'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._not_isdir(obj):
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _isfile_checks():
    print ()
    print (" --- file type checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = 'a file '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_isfile'

    # existence check is just for us
    if dom._exists(obj):
        if dom._isfile(obj):
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_isfile_not'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._isfile(obj):
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _not_isfile_checks():
    print ()
    print (" --- not file type checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = 'a file '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_isfile_not'

    # existence check is just for us
    if dom._exists(obj):
        if dom._not_isfile(obj):
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_isfile'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._not_isfile(obj):
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _uid_owns_checks():
    print ()
    print (" --- object uid owns checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = 'owned by uid '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_uid_owns'

    # existence check is just for us
    if dom._exists(obj):
        if dom._uid_owns(obj):
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_uid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._uid_owns(obj):
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _not_uid_owns_checks():
    print ()
    print (" --- object uid not owns checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = 'owned by uid '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_uid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if dom._not_uid_owns(obj):
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_uid_owns'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._not_uid_owns(obj):
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _gid_owns_checks():
    print ()
    print (" --- object gid owns checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = 'owned by gid '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_gid_owns'

    # existence check is just for us
    if dom._exists(obj):
        if dom._gid_owns(obj):
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_gid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._gid_owns(obj):
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _not_gid_owns_checks():
    print ()
    print (" --- object gid not owns checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = 'owned by gid '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_gid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if dom._not_gid_owns(obj):
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_gid_owns'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._not_gid_owns(obj):
            _bool = ''
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            msg = _objadj + _bool + _objvrb + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _id_owns_checks():
    print ()
    print (" --- object id owns checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = {}
    _objvrb['uid'] = 'owned by uid '
    _objvrb['gid'] = 'owned by gid '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_id_owns'

    # existence check is just for us
    if dom._exists(obj):
        if dom._id_owns(obj):
            _bool = ''
            _junct = 'and is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            _junct = 'or is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative checks (uid)")
    print ()

    obj = test_objects + '_id_uid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._id_owns(obj):
            _bool = 'not '
            _junct = 'or is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            _junct = 'and is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative checks (gid)")
    print ()

    obj = test_objects + '_id_gid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._id_owns(obj):
            _bool = 'not '
            _junct = 'or is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            _junct = 'and is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative checks (uid and gid)")
    print ()

    obj = test_objects + '_id_uid_gid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._id_owns(obj):
            _bool = 'not '
            _junct = 'or is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            _junct = 'and is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# this only checks type, not existence
def _not_id_owns_checks():
    print ()
    print (" --- object id not owns checks --- ")
    print ()

    _objadj = 'object is '
    _objvrb = {}
    _objvrb['uid'] = 'owned by uid '
    _objvrb['gid'] = 'owned by gid '
    _objsep = ': '

    print (" positive checks (uid)")
    print ()

    obj = test_objects + '_id_uid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if dom._not_id_owns(obj):
            _bool = 'not '
            _junct = 'or is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            _junct = 'and is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" positive checks (gid)")
    print ()

    obj = test_objects + '_id_gid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if dom._not_id_owns(obj):
            _bool = 'not '
            _junct = 'or is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            _junct = 'and is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" positive checks (uid and gid)")
    print ()

    obj = test_objects + '_id_uid_gid_owns_not'

    # existence check is just for us
    if dom._exists(obj):
        if dom._not_id_owns(obj):
            _bool = 'not '
            _junct = 'or is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = ''
            _junct = 'and is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_id_owns'

    # existence check is just for us
    if dom._exists(obj):
        if not dom._not_id_owns(obj):
            _bool = ''
            _junct = 'and is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._pass(msg)
        else:
            _bool = 'not '
            _junct = 'or is '
            msg = _objadj + _bool + _objvrb['uid'] + _junct + _bool + _objvrb['gid'] + _objsep + obj
            dcm._fail(msg)
            raise SystemExit
    else:
        dcm._halt("object is missing" + _objsep + obj)
        raise SystemExit


# ddm module checks

# existence checks are incorporated into these tests
def _dir_exists_checks():
    print ()
    print (" --- dir existence and is a dir checks --- ")
    print ()

    _objadj = 'dir does '
    _objvrb = {}
    _objvrb['exist'] = 'exist '
    _objvrb['dir'] = 'a dir '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_dir_exists'

    if ddm._dir_exists(obj):
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative checks (not exists)")
    print ()

    obj = test_objects + '_dir_exists_not'

    if not ddm._dir_exists(obj):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative checks (not dir)")
    print ()

    obj = test_objects + '_dir_isdir_not'

    if not ddm._dir_exists(obj):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._fail(msg)
        raise SystemExit


# existence checks are incorporated into these tests
def _not_dir_exists_checks():
    print ()
    print (" --- dir not existence and is not a dir checks --- ")
    print ()

    _objadj = 'dir does '
    _objvrb = {}
    _objvrb['exist'] = 'exist '
    _objvrb['dir'] = 'a dir '
    _objsep = ': '

    print (" positive checks (not exists)")
    print ()

    obj = test_objects + '_dir_exists_not'

    if ddm._not_dir_exists(obj):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" positive checks (not dir)")
    print ()

    obj = test_objects + '_dir_isdir_not'

    if ddm._not_dir_exists(obj):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._fail(msg)
        raise SystemExit

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_dir_exists'

    if not ddm._not_dir_exists(obj):
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['dir'] + _objsep + obj
        dcm._fail(msg)
        raise SystemExit


# existence checks are incorporated into these tests
def _uid_owns_dir_checks():
    print ()
    print (" --- dir uid owns checks --- ")
    print ()

    _objadj = 'dir does '
    _objvrb = {}
    _objvrb['exist'] = 'exist '
    _objvrb['own'] = 'owned by uid '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_uid_does_own_dir'

    if ddm._uid_does_own_dir(obj):
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._fail(msg)

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_uid_does_not_own_dir'

    if not ddm._uid_does_own_dir(obj):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._fail(msg)

# existence checks are incorporated into these tests
def _not_uid_owns_dir_checks():
    print ()
    print (" --- dir uid not owns checks --- ")
    print ()

    _objadj = 'dir does '
    _objvrb = {}
    _objvrb['exist'] = 'exist '
    _objvrb['own'] = 'owned by uid '
    _objsep = ': '

    print (" positive check ")
    print ()

    obj = test_objects + '_uid_does_not_own_dir'

    if ddm._uid_does_not_own_dir(obj):
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._fail(msg)

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_uid_does_own_dir'

    if not ddm._uid_does_not_own_dir(obj):
        _bool = ''
        _junct = 'and is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = 'not '
        _junct = 'or is '
        msg = _objadj + _bool + _objvrb['exist'] + _junct + _bool + _objvrb['own'] + _objsep + obj
        dcm._fail(msg)


#dave here
def _dir_gid_checks():
    print ()
    print (" --- dir gid owns checks --- ")
    print ()

    print (" positive check ")
    print ()

    obj = test_objects + '_gid_does_own_dir'
    _objsep = ': '

    if ddm._gid_does_own_dir(obj):
        _bool = 'not '
        msg = "gid does " + _bool + "own dir" + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = 'not '
        msg = "gid does " + _bool + "own dir" + _objsep + obj
        dcm._fail(msg)

    print ()
    print (" negative check ")
    print ()

    obj = test_objects + '_gid_does_not_own_dir'

    if not ddm._gid_does_own_dir(obj):
        _bool = 'not '
        msg = "gid does " + _bool + "own dir" + _objsep + obj
        dcm._pass(msg)
    else:
        _bool = 'not '
        msg = "gid does " + _bool + "own dir" + _objsep + obj
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



    # from here down needs work

    print ()
    print (" --- dir contents checks --- ")
    print ()

    _objsep = ': '
    obj = test_objects + 'gdir_is_empty'
    passmsg = 'dir is empty' + _objsep + obj
    failmsg = 'dir is not empty' + _objsep + obj

    if ddm._dir_is_empty(obj):
        dcm._pass(passmsg)
    else:
        dcm._fail(failmsg)

    print ()

    obj = test_objects + 'gdir_is_not_empty'
    passmsg = 'dir is not empty' + _objsep + obj
    failmsg = 'dir is empty ' + _objsep + obj

    if ddm._dir_is_not_empty(obj):
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

    obj = ('gfile_does_not_exst')
    if dfm._file_does_not_exist(obj):
        dcm._pass("file does not exist" + _objsep + obj)
    else:
        dcm._fail("file does not exist" + _objsep + obj)

    obj = ('gfile_does_exist')
    if dfm._file_does_exist(obj):
        dcm._pass("file does exist" + _objsep + obj)
    else:
        dcm._fail("file does exist" + _objsep + obj)

    print ()
    print (" --- file is a file checks --- ")
    print ()

    obj = ('gfile_is_not_a_file')
    if dfm._file_is_not_a_file(obj):
        dcm._pass("file is not a file" + _objsep + obj)
    else:
        dcm._pass("file is a file" + _objsep + obj)

    obj = ('gfile_is_a_file')
    if dfm._file_is_a_file(obj):
        dcm._pass("file is a file" + _objsep + obj)
    else:
        dcm._pass("file is not a file" + _objsep + obj)

    print ()
    print (" --- file contents checks --- ")
    print ()

    obj = ('gfile_is_empty')
    if dfm._file_is_empty(obj):
        dcm._pass("file is empty" + _objsep + obj)
    else:
        dcm._pass("file is empty" + _objsep + obj)

    obj = ('gfile_is_not_empty')
    if dfm._file_is_not_empty(obj):
        dcm._pass("file is not empty" + _objsep + obj)
    else:
        dcm._pass("file is not empty" + _objsep + obj)

    print ()
    print (" --- file owner checks --- ")
    print ()

    obj = ('guid_does_own_file')
    if dfm._uid_does_own_file(obj):
        dcm._pass("uid does own file" + _objsep + obj)
    else:
        dcm._pass("uid does not own file" + _objsep + obj)

    obj = ('guid_does_not_own_file')
    if dfm._uid_does_not_own_file(obj):
        dcm._pass("uid does not own file" + _objsep + obj)
    else:
        dcm._pass("uid does not own file" + _objsep + obj)

    print ()
    print (" --- file group checks --- ")
    print ()

    obj = ('ggid_does_own_file')
    if dfm._gid_does_own_file(obj):
        dcm._pass("gid does  own file" + _objsep + obj)
    else:
        dcm._pass("gid does  not own file" + _objsep + obj)

    obj = ('ggid_does_not_own_file')
    if dfm._gid_does_not_own_file(obj):
        dcm._pass("gid does  not own file" + _objsep + obj)
    else:
        dcm._pass("gid does   own file" + _objsep + obj)


if __name__ == "__main__":
    print ()
    print ("########################################")
    print ()

    test_objects = os.path.expanduser("~") + '/tmp/test_objects/'

    main()

    print ()
    print ("########################################")
    print ()

    raise SystemExit
