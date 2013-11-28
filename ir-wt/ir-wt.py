#!/usr/bin/python

# Several little tools built around capturing, decrypting, and reading new .PKX
# format Pokemon data from the X and Y games. Lots of code inspired by
# Infinite Recursion and LordLandon's IR-GTS projects. Uses "xypkmcrypt.exe",
# created by Xfr and Bond697.
#
# - chickenmatt5

import os
from platform import system
from array import array
from src import wtver
from src.stats import statana
from src.decrypt import adecrypt
#from src.packetcap import getmac

def getpath():
    
    while True:
        path = raw_input('Enter .PKX file path:').strip()
        path = os.path.normpath(path)
        if system() != 'Windows':
            path = path.replace('\\', '')

        if path.startswith('"') or path.startswith("'"):
            path = path[1:]
        if path.endswith('"') or path.endswith("'"):
            path = path[:-1]
        if os.path.exists(path) and path.lower().endswith('.pkx'): break
        elif os.path.exists(path) and path.lower().endswith('.bin'): break
        else:
            print 'Invalid file name, try again'
            continue
        if len(pkx) != 232:
            print 'Invalid filesize: %d bytes. Needs to be 232 bytes.' % len(pkx)
            continue
        else: break
        
    with open(path, 'rb') as f:
        pkx = f.read()

    p = array('B')
    p.fromstring(pkx)

    if p[0x04] != 00:
        print 'Sanity placeholder is not present (offset 0x04 does not equal 00), invalid Pokemon data!'
        print '\n\nPress ctrl + c to exit...'
    else: return [path,p,pkx]

print '\nIR-WT version ' + wtver.version

while True:
    print '\nChoose:'
    print 'a - analyze .pkx file'
    print 'd - decrypt a .bin or .pkx file'
#    print 'i - intercept and save Wonder Trade Pokemon'
    print 'q - quit\n'
    choice = raw_input().strip().lower()

    if choice.startswith('a'):
        data = getpath()
        statana(data[0],data[1])
        print '\nReturning to main menu...'
        continue
    elif choice.startswith('d'):
        data = getpath()
        adecrypt(data[0],data[1])
        print '\nReturning to main menu...'
        continue
#    elif choice.startswith('i'): getmac()
    elif choice.startswith('q'):
        print 'Quitting program'
        exit()
    else:
        print 'Invalid option, please try again.'
        continue
