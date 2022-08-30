#!/usr/bin/env python

import sys
import statistics #stats for median
import bed_parser #former script call
fname = sys.argv[1]
bed = bed_parser.parse_bed(fname) #define variable as the script result
medvals = [] #list of median variables
lengthbed = len(bed) #length of former script result
for i in range(0, lengthbed):
    medvals.append(int(bed[i][9])) #median of exons per gene
print(statistics.median(medvals))
#wc -l sys.argv[1] = gene count
#in our case, that is 3273
#exons = 19668



