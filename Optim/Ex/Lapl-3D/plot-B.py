import matplotlib
import numpy as np

matplotlib.use('Agg')
from matplotlib import pyplot as plt

A = np.loadtxt("orig.txt", usecols=(0, 6))
B = np.loadtxt("blck.txt", usecols=(0, 6))

fig = plt.figure(1, frameon=False)
fig.clf()
ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
ax.plot(A[:,0], A[:,1], marker="o", color="r", ls="-", label="Orig.")
ax.plot(B[:,0], B[:,1], marker="s", color="b", ls="-", label="Blocked")
ax.legend(loc="lower right")
ax.set_ylim(0)
ax.set_ylabel(r"$\beta_{FP}$ [Gflop/s]")
ax.set_xlabel(r"$N_{omp}$")
fig.savefig("B.png", transparent=True, dpi=300)
