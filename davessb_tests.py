#!/usr/bin/env python3

import davessb_file_module as dfm
import davessb_dir_module as ddm 

import settings

def main():

    #file existance checks
    testfile=('test_files/file_does_not_exst')
    if dfm._file_does_not_exist(testfile):
        print("PASS: file does not exist: " + testfile)
    else:
        print ("FAIL")
        return False

    testfile=('test_files/file_does_exist')
    if dfm._file_does_exist(testfile):
        print("PASS: file does exist: " + testfile)
    else:
        print ("FAIL")
        return False

    #file contents checks
    testfile=('test_files/file_is_empty')
    if dfm._file_is_empty(testfile):
        print ("PASS: file is empty: " + testfile)
    else:
        print ("FAIL")
        return False

    testfile=('test_files/file_is_not_empty')
    if dfm._file_is_not_empty(testfile):
        print ("PASS: file is not empty: " + testfile)
    else:
        print ("FAIL")
        return False

if __name__ == "__main__":
    main()
