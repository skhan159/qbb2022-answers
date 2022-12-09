import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def simulation(start_freq, pop_size):
    list = [start_freq]
    freq = start_freq
    while (freq < 1) and (freq > 0):
        freq = (np.random.binomial(pop_size, freq))/pop_size
        list.append(freq)
    return (list)

# allele=simulation(0.5, 1000)

# def plot(allele):
#     x=range(len(allele))
#     plt.plot(x, allele)
#     plt.xlabel("generation")
#     plt.ylabel("Allele frequency")
#     plt.title("Allele freq of 0.5 and a population of 1000")
#     plt.savefig("plot.png")

# plot(allele)

# runs = []
# for i in range(1000):
#     runs.append(len(simulation(0.5,100)))
#
# plt.hist(runs)
# plt.xlabel("# generations to fixation")
# plt.ylabel("Count")
# plt.savefig("plot2.png")

# time = []
# x = [100, 1000, 10000, 100000, 1000000, 10000000]
# for j in x:
#     time.append(len(simulation(0.5, j)))
# plt.plot(x, time)
# plt.xlabel("population")
# plt.ylabel("time to fix")
# plt.savefig("plot3.png")

df = {'alfreq': [], 'fixtimes': []}
fix_time_df = pd.DataFrame(df)
x = np.linspace(0.1, 1, num=10)
for i in x:
    df = {'alfreq': [i]*100, 'fixtimes': np.zeros(100)}
    fixed = pd.DataFrame(df)
    for j in range(100):
        fixed.loc[j, 'fixtimes']=len(simulation(i, 1000))
    fix_time_df = pd.concat([fix_time_df, fixed], axis=0)

sns.stripplot(y="fixtimes", x="alfreq", data=fix_time_df)
plt.title('population size of 1000')
plt.tight_layout()
plt.savefig("plot4.png")

