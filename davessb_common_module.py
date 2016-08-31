#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#only top checks are not infos
#negative checks call positive with 'nots', don't redo checks

class msgends:
    INFO = '💙  \033[34m[INFO]: '
    PASS = '💚  \033[32m[PASS]: '
    WARN = '💛  \033[33m[WARN]: '
    FAIL = '❤️  \033[31m[FAIL]: '
    HALT = '💔  \033[4;31m[HALT]: '
    ENDC = '\033[0m'

#messages
def _info(msg=''):
    print(msgends.INFO + msg + msgends.ENDC)
    if not msg:
        _warn('no text provided for previous INFO message')

def _pass(msg=''):
    print(msgends.PASS + msg + msgends.ENDC)
    if not msg:
        _warn('no text provided for previous PASS message')

def _warn(msg=''):
    print(msgends.WARN + msg + msgends.ENDC)
    if not msg:
        _warn('no text provided for previous WARN message')

def _fail(msg=''):
    print(msgends.FAIL + msg + msgends.ENDC)
    if not msg:
        _warn('no text provided for previous FAIL message')

def _halt(msg=''):
    print(msgends.HALT + msg + msgends.ENDC)
    if not msg:
        _warn('no text provided for previous HALT message')

