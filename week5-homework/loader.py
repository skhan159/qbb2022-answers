import bdg_loader
import sys
import matplotlib.pyplot as plt
import numpy as np

data1 = bdg_loader.load_data(sys.argv[1])
data2 = bdg_loader.load_data(sys.argv[2])
data3 = bdg_loader.load_data(sys.argv[3])
data4 = bdg_loader.load_data(sys.argv[4])
fig, ax = plt.subplots(ncols=2,nrows=2)
ax[0,0].plot(data1['X'], data1['Y'])
ax[0,1].plot(data2['X'], data2['Y'])
ax[1,0].plot(data3['X'], data3['Y'])
ax[1,1].plot(data4['X'], data4['Y'])
ax[0,0].fill_between(data1['X'], data1['Y'])
ax[0,1].fill_between(data2['X'], data2['Y'])
ax[1,0].fill_between(data3['X'], data3['Y'])
ax[1,1].fill_between(data4['X'], data4['Y'])
ax[0,0].set_title("H3k27ac DO")
ax[0,1].set_title("H3k27ac D2")
ax[1,0].set_title("Klf4")
ax[1,1].set_title("Sox2")
plt.tight_layout()
fig.savefig("ex5_pt1.png")
