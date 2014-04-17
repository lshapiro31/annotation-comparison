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

	infile = open(infileName, 'r')	
	for line in infile:
		if line[0] == "#":
			continue
		if line[0] == ">":
			break
        	line = line.strip()
        	entries = line.split()
        	strand = entries[6]
        	feature = entries[2]
        	start = entries[3]
        	stop = entries[4]
        	if strand == "+":
               		if feature == "CDS":
               	        	pCDS.add(Interval(start,stop))
		elif strand == "-":
          	     	if feature == "CDS":
               	        	mCDS.add(Interval(start,stop))

	gffDict = {}
	gffDict['pCDS'] = pCDS
	gffDict['mCDS'] = mCDS
	infile.close()

	return gffDict

gffDict1 = read_gff(sys.argv[1])
gffDict2 = read_gff(sys.argv[2])

#Write files
prefix = os.path.splitext(sys.argv[1])[0]+ "_" + os.path.splitext(sys.argv[2])[0] + "_"
for key in gffDict1:
	outfile = open(prefix + key + "1", 'w')
	for i in (gffDict1[key] - gffDict2[key]):
		outfile.write(i.lower_bound +'\t' +i.upper_bound + '\n')
	outfile.close()
for key in gffDict1:
	outfile = open(prefix + key + "2", 'w') 
	for i in (gffDict2[key] - gffDict1[key]):
		outfile.write(i.lower_bound + '\t' + i.upper_bound + '\n')
	outfile.close()

