#!/usr/bin/env python3

import os

def _dir_exists(pathdir):
    if os.path.exists(pathdir):
        return True
    else:
        return False

def _file_exists(pathfile):
    if os.path.exists(pathfile):
        return True
    else:
        return False


