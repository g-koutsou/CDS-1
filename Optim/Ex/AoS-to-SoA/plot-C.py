import matplotlib
import numpy as np

matplotlib.use('Agg')
from matplotlib import pyplot as plt

A = np.loadtxt("aos.txt", usecols=(5, 13))
B = dict()
vl = 2
while True:
    try:
        B[vl] = np.loadtxt("soa-vl%d.txt" % vl, usecols=(8, 16))
    except FileNotFoundError:
        break
    vl *= 2

fig = plt.figure(1)
fig.clf()
ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
ax.plot(np.log2(A[:,0]), A[:,1], marker="o", color="r", ls="-", label="AoS")
for vl in sorted(B):
    ax.plot(np.log2(B[vl][:,0]), B[vl][:,1], marker="s", ls="-", label="SoA, VL=%d" % vl)
ax.set_xticklabels("$2^{%d}$" % x for x in ax.get_xticks())
ax.legend(loc="upper left")
ax.set_ylabel(r"$\beta_{IO}$ [GBytes/s]")
ax.set_xlabel(r"$L$")
fig.savefig("C.png", dpi=300, transparent=True)
