import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import numpy as np
import pylab as P

import sys
from os.path import join
import re


directory = sys.argv[1]

d1 = file(join(directory, "issue-times.txt")).read()
issueT = np.array(map(float, re.findall("\d+[.]\d+", d1)))
r1T = map(float, re.findall("\d+[.]\d+", file(join(directory, "r1-times.txt")).read()))
r2T = map(float, re.findall("\d+[.]\d+", file(join(directory, "r2-times.txt")).read()))


bins = np.arange(0,2, 0.075)
# the histogram of the data
n, bins, patches = plt.hist((issueT, r1T, r2T), bins, normed=1, alpha=0.75, label=["Issuing","Pay (Original)","Pay (Normal)"])

[p.set_hatch("/") for p in patches[0].patches]
[p.set_hatch("\\") for p in patches[1].patches]
[p.set_hatch("x") for p in patches[2].patches]


plt.xlabel('Latency (sec)')
plt.ylabel('Probability density')
plt.title(r'RSCoin Issue & Pay Protocol Latency')
plt.axis([0, 1.5, 0, 8])
plt.grid(True)

first_legend = plt.legend(loc=1)

plt.savefig(join(directory, "latency.pdf"))
plt.close()