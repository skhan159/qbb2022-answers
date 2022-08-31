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
    tuple = (line[0], line[1]) #defines a tuple as the index 1 and 2 of lines
    psnpsdict[tuple] = line[2]
vcf = vcfParser.parse_vcf(genome)
for i in range(0, 2, len(vcf)):
    snpf = vcf[i]
    candp.append(vcf[i]) #this is honestly where I got stuck, but I know I need to compare each key in the dictionary I made above
                        #to the extracted index lines 0 and 1 from the parsed random_snipped.vcf file. 
print(candp)
