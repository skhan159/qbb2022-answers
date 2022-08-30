#!/usr/bin/env python

import sys
import statistics
import bed_parser
fname = sys.argv[1]
bed = bed_parser.parse_bed(fname)
medvals = []
lengthbed = len(bed)
for i in range(0, lengthbed):
    medvals.append(int(bed[i][9]))
print(statistics.median(medvals))
#wc -l sys.argv[1] = gene count
#in our case, that is 3273
#exons = 19668



