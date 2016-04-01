#!/usr/bin/env python3

import os

#object existance checks
def _exists(pathobject):
    if os.path.exists(pathobject):
        return True
    else:
        return False

#object user owner checks
def _uid_owns(pathobject):
    if os.stat(pathobject).st_uid == os.getuid():
        return True
    else:
        return False

#object group owner checks
def _gid_owns(pathobject):
    if os.stat(pathobject).st_gid == os.getgid():
        return True
    else:
        return False

