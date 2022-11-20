import numpy as np
import matplotlib.pyplot as plt
import sys

predicted = np.genfromtxt(f"{sys.argv[1]}", skip_header=1, dtype=None, encoding=None, names= ["ID", "SCORE"])
scores = np.ndarray.tolist(predicted["SCORE"])
genes = predicted["ID"]

gene_predictions = []

for i, line in enumerate(open(sys.argv[2])):
    if line.strip('"').startswith("##"):
        header = np.array(line.strip('"\r\n').split('\t'))
        k562_obs_idx = np.where(header == "E123")[0][0]
    elif not line.strip('"').startswith("#"):
        fields = line.strip('"\r\n').split('\t')
        gene_predictions.append(float(fields[4]))

fig, ax = plt.subplots()
ax.scatter(sorted(scores[0:18377]), sorted(gene_predictions), color="blue", s=0.25, alpha=1)
ax.set_xlabel("Predicted K562 expression level, \nfrom paper")
ax.set_ylabel("K562 expression level predicted from Xpresso")
b = np.polyfit(sorted(scores[0:18377]), sorted(gene_predictions), deg=1)
xseq = np.linspace(-1.5, 2, num=100)
ax.plot(xseq, b[1] + b[0] * xseq, color="red", lw=1, alpha=0.7)
ax.text(-1.5, 1.5, "r^2 = " + str(b[0]) + "\nn = 18377")
plt.tight_layout()
fig.savefig("prediction_graph.png")

