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
        qual.append(j[1])
    allele.append(i[7]['AF'])
    effect_ent=i[7]['ANN']
    effects=effect_ent.split('|')
    effect.append(effects[2])

effect_dictionary={}
for i in effect:
    if i in effect_dictionary.keys():
        effect_dictionary[i] += 1
    else:
        effect_dictionary[i] = 1
reads = [int(d) for d in reads if d != '.']
qual = [float(d) for d in qual if d != '.']
allele = [float(d) for d in qual if d != '.']

fig, ax = plt.subplots(ncols=2,nrows=2)
ax[0,0].hist(reads)
ax[1,0].hist(qual)
ax[0,1].hist(allele)
ax[1,1].bar(effect_dictionary, effect_dictionary.keys())
plt.show()
