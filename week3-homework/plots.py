import vcfParser
import matplotlib.pyplot as plt
import sys

da_file = vcfParser.parse_vcf(sys.argv[1])
reads = []
qual = []
allele = []
effect = []
for i in da_file[1:]:
    for j in i[9:]:
        reads.append(j[4])
        qual.append(j[1]) #extracts reads and quality scores from the vcfParser output
    allele.append(i[7]['AF'])
    effect_ent=i[7]['ANN']
    effects=effect_ent.split('|')
    effect.append(effects[2]) #extracts effect size and allele count from the vcfParser output

effect_dictionary={}
for i in effect:
    if i in effect_dictionary.keys():
        effect_dictionary[i] += 1
    else:
        effect_dictionary[i] = 1 #defines a dictionary to save the effect sizes and keys for each effect size
reads = [int(d) for d in reads if d != '.']
qual = [float(d) for d in qual if d != '.']
allele = [float(d) for d in allele if d != '.'] #cleans/removes non-defined data (defined by ".")

fig, ax = plt.subplots(ncols=2,nrows=2)
ax[0,0].hist(reads)
ax[0,0].set_xlabel("Loci")
ax[0,0].set_ylabel("reads per locus") #plots reads
ax[1,0].hist(qual)
ax[1,0].set_xlabel("Loci")
ax[1,0].set_ylabel("quality score per locus") #plots quality scores
ax[0,1].hist(allele)
ax[0,1].set_xlabel("Loci")
ax[0,1].set_ylabel("Allele frequency per locus") #plots allele frequencies
ax[1,1].bar(*zip(*effect_dictionary.items())) #this is an interesting bit of code I found on stack overflow.
ax[1,1].set_xlabel("Strength of effect")
ax[1,1].set_ylabel("Number per strength")
fig.tight_layout()
fig.savefig("graphs.png")
