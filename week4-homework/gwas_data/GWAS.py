import sys
import matplotlib.pyplot as plt
import numpy as np
import vcfParser

pca = np.genfromtxt(f"{sys.argv[1]}", encoding = None, skip_header=1, names= ["chr", "snp", "bp", "A1", "TEST", "NMISS", "BETA", "STAT", "P"])
# IC50 = np.genfromtxt(f"{sys.argv[3]}", encoding = None, skip_header=1, deletechars="NA", names= ["FID", "IID", "IC50"])
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
# genotypes = vcfParser.parse_vcf(sys.argv[2])

max_P = np.min(pca["P"])
print(max_P)
# big_SNP = "rs7257475"
# homo_rec = []
# het = []
# homo_dom = []
# for q in genotypes:
#     if q[2] == big_SNP:
#         line = q
#         count = 1
#         for u in line:
#             if np.isnan(IC50["IC50"][count]):
#                 count +=1
#             elif u == "0/0":
#                 homo_rec.append(IC50["IC50"][count])
#                 count += 1
#             elif u == "0/1":
#                 het.append(IC50["IC50"][count])
#                 count += 1
#             elif u == "1/1":
#                 homo_dom.append(IC50["IC50"][count])
#                 count += 1
# listlist = [homo_dom, het, homo_rec]
# fig, ax = plt.subplots()
# ax.set_xticklabels(["Homo_dom", "Het", "Homo_rec"])
# ax.set_ylabel("flip")
# ax.boxplot(listlist)
# ax.set_title(f"{sys.argv[2]}")
# fig.savefig(f"{sys.argv[2]}.png")





