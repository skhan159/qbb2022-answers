import sys
import matplotlib.pyplot as plt
import numpy as np
import vcfParser

pca = np.genfromtxt(f"{sys.argv[1]}", encoding = None, skip_header=1, names= ["chr", "snp", "bp", "A1", "TEST", "NMISS", "BETA", "STAT", "P"])
# IC50 = np.genfromtxt(f"{sys.argv[3]}", encoding = None, skip_header=1, deletechars="NA", names= ["FID", "IID", "IC50"]) #these extract the IC50 and ".assoc.linear" outs from plink for each phenotype 
fig, ax = plt.subplots()
pvals = pca["P"]
value = 10e-5
cols = []
for i in pvals:
    if i < value:
        cols.append("magenta")
    else:
        cols.append("cyan") #defines p-values below 10e-5 to be magenta and above 10e-5 to be cyan
ax.scatter(np.arange(0, len(pvals)), -np.log(pvals), c=cols) #important: -log here for y-axis.
ax.set_xlabel("Locus")
ax.set_ylabel("-log p-value")
ax.set_title(f"{sys.argv[1]} SNPs")
# fig.savefig(f"{sys.argv[1]}.png")
# genotypes = vcfParser.parse_vcf(sys.argv[2]) #imports the genotypes.vcf file to be compared to later

max_P = np.min(pca["P"])
print(max_P) #this code was used to find the lowest p-value. I used less in bash to search for the respective SNPid using the P-value
# big_SNP = "rs7257475" #this was found as stated above
# homo_rec = []
# het = []
# homo_dom = []
# for q in genotypes:
#     if q[2] == big_SNP:
#         line = q
#         count = 1
#         for u in line:
#             if np.isnan(IC50["IC50"][count]): #ignores nan (undefined) data points, asks program to move to next data point
#                 count +=1
#             elif u == "0/0":
#                 homo_rec.append(IC50["IC50"][count]) # "0/0" appended as homo_rec
#                 count += 1
#             elif u == "0/1":
#                 het.append(IC50["IC50"][count]) # "0/1" appended as het
#                 count += 1
#             elif u == "1/1":
#                 homo_dom.append(IC50["IC50"][count]) # "1/1" appended as homo_dom
#                 count += 1
# listlist = [homo_dom, het, homo_rec] #create a list of lists for the boxplot
# fig, ax = plt.subplots()
# ax.set_xticklabels(["Homo_dom", "Het", "Homo_rec"]) #set boxplot labels
# ax.set_ylabel("flip")
# ax.boxplot(listlist)
# ax.set_title(f"{sys.argv[2]}")
# fig.savefig(f"{sys.argv[2]}.png")





