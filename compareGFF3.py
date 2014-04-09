#!/usr/bin/env python

import sys
import os

sys.path.insert(1, "/opt/PepPrograms/interval-1.0.0")
try:
    from interval import Interval, IntervalSet
except ImportError:
    print "oops, the import didn't work"
    sys.exit()

# This script...

def usage():
    print "compareGFF3.py <.gff 1> <.gff 2>"

if len(sys.argv) != 3:
    usage()
    sys.exit()


