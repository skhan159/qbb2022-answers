#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
ax.hist( ac, density=True )
ax.set_yscale("log") #set y to log 
ax.set_ylabel("Density") #set y axis label to Density
ax.set_xlabel("Allele counts") #set x axis label to Allele counts
ax.set_title(vcf) #set graph title to file name
fig.savefig( vcf + "improved.png" )

fs.close()

