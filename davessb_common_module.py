#!/usr/bin/env python3

#only deepest tests get to say anything or return anything
#only top checks are not infos
#negative checks call positive with 'nots', don't redo checks

class bcolors:
    FAIL = '\033[31m'
    PASS = '\033[32m'
    WARN = '\033[33m'
    INFO = '\033[34m'
    HALT = '\033[4;31m'
    ENDC = '\033[0m'

#messages
def _fail(msg):
    print("❤️  " + bcolors.FAIL + "[FAIL]: " + msg + bcolors.ENDC)

def _pass(msg):
    print("💚  " + bcolors.PASS + "[PASS]: " + msg + bcolors.ENDC)

def _warn(msg):
    print("💛  " + bcolors.WARN + "[WARN]: " + msg + bcolors.ENDC)

def _info(msg):
    print("💙  " + bcolors.INFO + "[INFO]: " + msg + bcolors.ENDC)

def _halt(msg):
    print("💔  " + bcolors.HALT + "[HALT]: " + msg + bcolors.ENDC)

