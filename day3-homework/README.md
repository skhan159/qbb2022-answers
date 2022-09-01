# QBB2022 - Day 3 - Homework Exercises Submission

1. plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3

2. I would assume the stronger clustering between the two variables indicates similarity between the variables between the two principal cluster components.

3.
#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as col

vals_per_gene = np.genfromtxt("joined_file.txt", dtype = None, encoding = None, names= ["locus1", "locus2", "val1", "val2", "val3", "pop", "super_pop", "gender"])

fig, ax = plt.subplots()
pop = np.unique(vals_per_gene["pop"])
for i in pop:
    x = []
    y = []
    for thingy in vals_per_gene:
        if i == thingy[5]:
            x.append(thingy[2])
            y.append(thingy[3])
            ax.scatter(x, y)
ax.legend(pop)
ax.set_ylabel("PC2")
ax.set_xlabel("PC1")
ax.set_title("PC1 vs PC2 per population")
fig.tight_layout()
plt.savefig("ex3_a.png")

suppop = np.unique(vals_per_gene["super_pop"])
for i in suppop:
    x = []
    y = []
    for thingy in vals_per_gene:
        if i == thingy[6]:
            x.append(thingy[2])
            y.append(thingy[3])
            ax.scatter(x, y)
ax.legend(suppop)
ax.set_ylabel("PC2")
ax.set_xlabel("PC1")
ax.set_title("PC1 vs PC2 per super population")
fig.tight_layout()
plt.savefig("ex3_b.png")

sex = np.unique(vals_per_gene["gender"])
for i in sex:
    x = []
    y = []
    for thingy in vals_per_gene:
        if i == thingy[7]:
            x.append(thingy[2])
            y.append(thingy[3])
            ax.scatter(x, y)
ax.legend(sex)
ax.set_ylabel("PC2")
ax.set_xlabel("PC1")
ax.set_title("PC1 vs PC2 per gender")
fig.tight_layout()
plt.savefig("ex3_c.png")
