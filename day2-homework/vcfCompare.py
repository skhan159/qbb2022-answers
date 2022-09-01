#!/usr/bin/env python

import sys
import vcfParser
snps = open(sys.argv[1])
genome = sys.argv[2] #defines the sys file-pulls
psnpsdict = {} #defines the dictionary variable
candp = []
for snp in snps:
    if snp.startswith("#"): #removes header
        continue
    line = snp.rstrip().split() #strips and splits lines
    tuplea = (line[0], line[1]) #defines a tuple as the index 1 and 2 of lines
    psnpsdict[tuplea] = line[2] #ID as second value assigned to each key
vcf = vcfParser.parse_vcf(genome)
i = [(x[0], x[1]) for x in vcf] #tuple comprehension?
count = 0
did_this_work = []
for k in i:
    if k in psnpsdict:
        did_this_work.append("YES")
        count = + 1
    else:
        did_this_work.append("NO")
        count = + 1
print(did_this_work) #this entire block is my attempt to debug why this specific code was not matching the list of keys I had generated with the keys in the dictonary. This is as far as I got
