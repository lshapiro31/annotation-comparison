#!/usr/bin/env python

import sys
import re
import getopt

# This script returns the genes associated with a list of starts and stops.
# Inputs: list of starts and stops, gff file 

def usage():
    print "getGenesFromPositions.py <positions file> <gff file>"

def read_positions(positionsFile):
    posList = []
    inFile = open(positionsFile, 'r')
    for line in inFile:
        line = line.strip()
        items = line.split()
        start = int(items[0])
        stop = int(items[1])
        posList.append([start,stop])
    inFile.close()
    return posList

def read_genes(gffFile):
    genesList = []
    genesDict = {}
    inFile = open(gffFile, 'r')
    for line in inFile:
        if line[0] == '#':
            continue
        if line[0] == '>':
            break
        line = line.strip()
        items = line.split()
        strand = items[6]
        feature = items[2]
        start = int(items[3])
        stop = int(items[4])
        if feature == "gene":
            geneID = items[8].split(';')[0].split('=')[1]
        else:
            continue
        genesList.append(geneID)
        genesDict[geneID] = [start, stop]
    inFile.close()
    return (genesList, genesDict)

def genes_in_pos(posList, genesList, genesDict):
    posGenes = []
    for region in posList:
        genesInRegion = []
        posStart = region[0]
        posStop = region[1]
        for gene in genesList:
            geneStart = genesDict[gene][0]
            geneStop = genesDict[gene][1]
            if (geneStart >= posStart and geneStart <= posStop) or \
                (geneStop >= posStart and geneStop <= posStop):
                genesInRegion.append(gene)
        for gene in genesInRegion:
            posGenes.append((gene, posStart, posStop))
            genesList.remove(gene)
    outFile = open("genes.txt", 'w')
    for gene in posGenes:
        outFile.write("%s\t%i\t%i\n" % gene)
    outFile.close()

            
if len(sys.argv) != 3:
    usage()
    sys.exit(2)
    
positionsFile, gffFile = sys.argv[1:]

posList = read_positions(positionsFile)
genesList, genesDict = read_genes(gffFile)
genes_in_pos(posList, genesList, genesDict)

