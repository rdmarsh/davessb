#!/usr/bin/env python3

import os

def _dir_exists(pathdir):
    if os.path.exists(pathdir):
        return True
    else:
        return False

def _dir_doesnt_exist(pathdir):
    if os.path.exists(pathdir):
        return True
    else:
        return False
