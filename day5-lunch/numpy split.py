
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.stats.weightstats as smw

df = np.genfromtxt("the_final_final.txt", delimiter=" ", dtype=None, encoding=None, names=["proband_ID", "paternal_age", "maternal_age", "paternal_mutations", "maternal_mutations"])
# fig, ax = plt.subplots()
# ax.scatter(df["maternal_age"], df["maternal_mutations"], alpha = 0.5, label = "Mothers")
# ax.scatter(df["paternal_age"], df["paternal_mutations"], alpha = 0.5, label = "Fathers")
# ax.set_xlabel("Ages")
# ax.set_ylabel("Number of mutations")
# ax.set_title("De novo mutations originating from gender of parents to kids")
# ax.legend()
# fig.savefig("ex2_a_and_b.png")

# fig, ax = plt.subplots()
# ax.hist(df["maternal_mutations"], alpha = 0.5, label = "Mothers")
# ax.hist(df["paternal_mutations"], alpha = 0.5, label = "Fathers")
# ax.legend()
# ax.set_ylabel("Mutations")
# ax.set_xlabel("Proband")
# ax.set_title("Paternal and Maternal de novo mutations")
# fig.savefig("ex2_c.png")

# model = smf.ols(formula = "paternal_mutations ~ 1 + paternal_age", data = df)
# results = model.fit()
# print(results.summary())

model = smw.ttest_ind(df["maternal_mutations"], df["paternal_mutations"])
print(model)

