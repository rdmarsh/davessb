#!/usr/bin/env python3

import os

#object existance checks
def _exists(pathobject):
    if os.path.exists(pathobject):
        return True
    else:
        return False

