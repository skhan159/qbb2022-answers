import sys
import matplotlib.pyplot as plt
import numpy as np
import vcfParser

pca = np.genfromtxt(f"{sys.argv[1]}", encoding = None, skip_header=1, names= ["chr", "snp", "bp", "A1", "TEST", "NMISS", "BETA", "STAT", "P"])

fig, ax = plt.subplots()
pvals = pca["P"]
value = 10e-5
cols = []
for i in pvals:
    if i < value:
        cols.append("magenta")
    else:
        cols.append("cyan")
ax.scatter(np.arange(0, len(pvals)), -np.log(pvals), c=cols)
ax.set_xlabel("Locus")
ax.set_ylabel("-log p-value")
ax.set_title(f"{sys.argv[1]} SNPs")
# fig.savefig(f"{sys.argv[1]}.png")
genotypes = vcfParser.parse_vcf(sys.argv[2])

big_SNP = "rs7257475"
index = np.where(genotypes[:] == big_SNP)
matching_snp = genotypes[index]
print(matching_snp)



