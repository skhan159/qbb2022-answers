
import numpy
from scipy.stats import poisson
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multitest import multipletests

array = numpy.zeros(1000000)
for i in range(50000): #this range can be altered for the set number of reads required for a genome at a specific depth. In this case, it is set for 100bp reads of a 1Mbp genome at 5x depth
    start = numpy.random.randint(0, high=999900)
    for h in range(start, start+100):
        array[h] += 1

fig, ax = plt.subplots()
ax.hist(array, label = "Distribution")
x = numpy.arange(0, 50, 1) #this range is arbitrary, but can be changed to fit the data better
y = poisson.pmf(x, 5)*1000000 #the second poisson call is lambda. Here it is set at 5, which is the depth of coverage specified before in the array
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
print(count) #this bit of code is used to track the locations of zero coverage in the array

lol = poisson.pmf(x, 5)*1000000
print(lol) #this bit of code is used to track the poisson predicted locations of zero coverage. The first number of this printed array is the zero coverage.


