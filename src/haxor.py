#!/usr/bin/env python3

import sys
import time

def haxor(payload,delay=0.05):
    for char in payload:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('\r')

