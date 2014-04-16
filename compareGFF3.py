#!/usr/bin/env python

import sys
import os

sys.path.insert(1, "/opt/PepPrograms/interval-1.0.0")
try:
    from interval import Interval, IntervalSet
except ImportError:
    print "oops, the import didn't work"
    sys.exit()

# This script will create sets from imported gff files.

def usage():
    print "compareGFF3.py <.gff 1> <.gff 2>"

if len(sys.argv) != 3:
    usage()
    sys.exit()




#Separate genes into categories based on strand and feature type
def read_gff(infileName):
	pCDS = IntervalSet()
	mCDS = IntervalSet()
	ptRNA = IntervalSet()
	mtRNA = IntervalSet()
	prRNA = IntervalSet()
	mtRNA = IntervalSet()

	for line in infileName:
        	line = line.strip()
        	entries = line.split()
        	strand = entries[7]
        	feature = entries[2]
        	start = entries[3]
        	stop = entires[4]

        	if strand == "+":
                	if feature == "CDS":
                        	pCDS.add(Interval(start,stop))
                	elif feature == "tRNA":
                        	ptRNA.add(Interval(start,stop))
                	else:
                        	prRNA.add(Interval(start,stop))
        	else:
                	if feature == "CDS":
                        	mCDS.add(Interval(start,stop))
                	elif feature == "tRNA":
                        	mtRNA.add(Interval(start,stop))
                	else:
                        	mrRNA.add(Interval(start,stop))
	gffDict = {}
	gffDict['pCDS'] = pCDS
	gffDict['mCDS'] = mCDS
	gffDict['ptRNA'] = ptRNA
	gffDict['mtRNA'] = mtRNA
	gffDict['prRNA'] = ptRNA
	gffDict['mrRNA'] = mtRNA
	
	return gffDict


gffDict1 = read_gff(sys.argv[1])
gffDict2 = read_gff(sys.argv[2])


