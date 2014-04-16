#!/usr/bin/env python

import sys
import os

sys.path.insert(1, "/opt/PepPrograms/interval-1.0.0")
try:
    from interval import Interval, IntervalSet
except ImportError:
    print "oops, the import didn't work"
    sys.exit()

# This script will compare the start and stop locations of genes in a gff file

def usage():
    print "compareGFF3.py <.gff 1> <.gff 2>"

if len(sys.argv) != 3:
    usage()
    sys.exit()

#Create dictionary containing start and stop locations for each feature
def read_gff(infileName):
	pCDS = IntervalSet()
	mCDS = IntervalSet()
	ptRNA = IntervalSet()
	mtRNA = IntervalSet()
	prRNA = IntervalSet()
	mtRNA = IntervalSet()

	infile = open(infileName, 'r')
	for line in infile:
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
	
	infile.close()

	return gffDict

gffDict1 = read_gff(sys.argv[1])
gffDict2 = read_gff(sys.argv[2])

#Write files

for key in gffDict1:
	outfile = open(key + "1", 'w')
	for i in (gffDict1[key] - gffDict2[key]):
		outfile.write(i + '\n')
	outfile.close()
for key in gffDict1:
	outfile = open(key + "2", 'w') 
	for i in (gffDict2[key] - gffDict1[key]):
		outfile.write(i + '\n')
	outfile.close()

