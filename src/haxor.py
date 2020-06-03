#!/usr/bin/env python

import sys
import time

def haxor(payload,delay=0.05):
    for char in payload:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('\r')

# if len(sys.argv) < 3:
    # print('usage: <haxor.py> \'hello world\' \'<delay>\'')
    # sys.exit(1)

# p=sys.argv[1]
# d=float(sys.argv[2])

# haxor(payload=p,delay=d)

