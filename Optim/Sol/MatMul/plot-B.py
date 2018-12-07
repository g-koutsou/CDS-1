import matplotlib
import numpy as np

matplotlib.use('Agg')
from matplotlib import pyplot as plt

A = np.loadtxt("orig-sorted.txt", usecols=(0, 13))
B = np.loadtxt("blck-sorted.txt", usecols=(0, 13))

fig = plt.figure(1, frameon=False)
fig.clf()
ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
ax.plot(np.log2(A[:,0]), A[:,1]/1e3, marker="o", color="r", ls="-", label="Orig.")
ax.plot(np.log2(B[:,0]), B[:,1]/1e3, marker="s", color="b", ls="-", label="Blocked")
ax.set_xticklabels("$2^{%d}$" % x for x in ax.get_xticks())
ax.legend(loc="lower right")
ax.set_ylim(0)
ax.set_ylabel(r"$\beta_{FP}$ [Gflop/s]")
ax.set_xlabel(r"$M\times N$")
fig.savefig("B.png", transparent=True, dpi=300)
