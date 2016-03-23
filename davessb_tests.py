#!/usr/bin/env python3

import davessb_dir_module as ddm 
import davessb_file_module as dfm

import settings

def main():

    print ()
    print ("----------------------------------------")
    print (" dir checks")
    print ("----------------------------------------")

    print ()
    print (" --- dir exisistance checks --- ")
    print ()

    testobject=('test_objects/dir_does_not_exst')
    if ddm._dir_does_not_exist(testobject):
        print("PASS: dir does not exist: " + testobject)
    else:
        print ("FAIL")
        return False

    testobject=('test_objects/dir_does_exist')
    if ddm._dir_does_exist(testobject):
        print("PASS: dir does exist: " + testobject)
    else:
        print ("FAIL")
        return False

    print ()
    print (" --- dir is a dir checks --- ")
    print ()

    testobject=('test_objects/dir_is_not_a_dir')
    if ddm._dir_is_not_a_dir(testobject):
        print("PASS: dir is not a dir: " + testobject)
    else:
        print ("FAIL")
        return False

    testobject=('test_objects/dir_is_a_dir')
    if ddm._dir_is_a_dir(testobject):
        print("PASS: dir is a dir: " + testobject)
    else:
        print ("FAIL")
        return False

    print ()
    print (" --- dir contents checks --- ")
    print ()

    testobject=('test_objects/dir_is_empty')
    if ddm._dir_is_empty(testobject):
        print ("PASS: dir is empty: " + testobject)
    else:
        print ("FAIL")
        return False

    testobject=('test_objects/dir_is_not_empty')
    if ddm._dir_is_not_empty(testobject):
        print ("PASS: dir is not empty: " + testobject)
    else:
        print ("FAIL")
        return False

    print ()
    print (" --- dir owner checks --- ")
    print ()

    testobject=('test_objects/uid_does_own_dir')
    if ddm._uid_does_own_dir(testobject):
        print ("PASS: uid does own dir: " + testobject)
    else:
        print ("FAIL")
        return False

    testobject=('test_objects/uid_does_not_own_dir')
    if ddm._uid_does_not_own_dir(testobject):
        print ("PASS: uid does not own dir: " + testobject)
    else:
        print ("FAIL")
        return False


    print ()
    print ("----------------------------------------")
    print (" file checks")
    print ("----------------------------------------")
    print ()

    print ()
    print (" --- file existance checks --- ")
    print ()

    testobject=('test_objects/file_does_not_exst')
    if dfm._file_does_not_exist(testobject):
        print("PASS: file does not exist: " + testobject)
    else:
        print ("FAIL")
        return False

    testobject=('test_objects/file_does_exist')
    if dfm._file_does_exist(testobject):
        print("PASS: file does exist: " + testobject)
    else:
        print ("FAIL")
        return False

    print ()
    print (" --- file is a file checks --- ")
    print ()

    testobject=('test_objects/file_is_not_a_file')
    if dfm._file_is_not_a_file(testobject):
        print("PASS: file is not a file: " + testobject)
    else:
        print ("FAIL")
        return False

    testobject=('test_objects/file_is_a_file')
    if dfm._file_is_a_file(testobject):
        print("PASS: file is a file: " + testobject)
    else:
        print ("FAIL")
        return False

    print ()
    print (" --- file contents checks --- ")
    print ()

    testobject=('test_objects/file_is_empty')
    if dfm._file_is_empty(testobject):
        print ("PASS: file is empty: " + testobject)
    else:
        print ("FAIL")
        return False

    testobject=('test_objects/file_is_not_empty')
    if dfm._file_is_not_empty(testobject):
        print ("PASS: file is not empty: " + testobject)
    else:
        print ("FAIL")
        return False

    print ()
    print (" --- file owner checks --- ")
    print ()

    testobject=('test_objects/uid_does_own_file')
    if dfm._uid_does_own_file(testobject):
        print ("PASS: uid does own file: " + testobject)
    else:
        print ("FAIL")
        return False

    testobject=('test_objects/uid_does_not_own_file')
    if dfm._uid_does_not_own_file(testobject):
        print ("PASS: uid does not own file: " + testobject)
    else:
        print ("FAIL")
        return False


if __name__ == "__main__":
    print ()
    print ("########################################")
    print ()

    main()

    print ()
    print ("########################################")
    print ()

