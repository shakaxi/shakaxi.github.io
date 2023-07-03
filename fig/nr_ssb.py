import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Sans"
plt.rcParams['font.size'] = 12
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['text.usetex'] = True

subc_num = 12 * 20
sym_num = 4
p = np.zeros((subc_num, sym_num))
p[56:184, 0] = 1
p[56:184, 2] = 2
p[:, 1::2] = 3
p[:49, 2] = 3
p[-48:, 2] = 3
fig, ax = plt.subplots()
ax.imshow(p, aspect=0.1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(r'time')
ax.set_ylabel(r'frequency')
fig.savefig('nr_ssb.png', bbox_inches='tight')
