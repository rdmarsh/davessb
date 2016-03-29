#!/usr/bin/env python3

import os

#object existance checks
def _does_exist(pathobject):
    if os.path.exists(pathobject):
        return True
    else:
        print ("does not exist: " + pathobject)
        return False

def _does_not_exist(pathobject):
    if not os.path.exists(pathobject):
        return True
    else:
        print ("does exist: " + pathobject)
        return False

