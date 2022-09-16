
import numpy
from scipy.stats import poisson
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multitest import multipletests

array = numpy.zeros(1000000)
for i in range(50000):
    start = numpy.random.randint(0, high=999900)
    for h in range(start, start+100):
        array[h] += 1

fig, ax = plt.subplots()
ax.hist(array, label = "Distribution")
x = numpy.arange(0, 50, 1)
y = poisson.pmf(x, 5)*1000000
ax.plot(x, y, label = "Poisson")
ax.set_xlabel("Number of reads")
ax.set_ylabel("Coverage of reads")
ax.legend()
ax.set_title("15x coverage of 1Mbp genome at 100bp reads")
fig.tight_layout()
# fig.savefig("week1x15.png")
count = 0
for u in array:
    if u == 0:
        count += 1
print(count)

lol = poisson.pmf(x, 5)*1000000
print(lol)
# count2 = 0
# for l in lol:
#     if l == 0:
#         count2 += 1
# print(count2)

