import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Sans"
plt.rcParams['font.size'] = 12
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['text.usetex'] = True

def plot_pat(ax: plt.Axes, pat: np.ndarray) -> None:
    '''Plot a pattern based on a given matrix.'''
    ax.imshow(pat)
    ax.set_xlabel(r'time (symbol)')
    ax.set_ylabel(r'frequency (subcarrier)')

subc_num = 12
sym_num = 14

# Type-1
p = np.zeros((subc_num, sym_num))
p[:, :2] = -1
v = np.array([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
p[:, 2] = v
fig, ax = plt.subplots(1, 2)
plot_pat(ax[0], p)
p[:, 3] = v
plot_pat(ax[1], p)
ax[0].set_xticks(np.arange(3))
ax[0].set_yticks(np.arange(0, subc_num))
ax[1].set_xticks(np.arange(4))
ax[1].set_yticks(np.arange(0, subc_num))
plt.tight_layout()
fig.savefig('nr_dmrs_type1.png', bbox_inches='tight')

# Type-2
p = np.zeros((subc_num, sym_num))
p[:, :2] = -1
v = np.array([1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3])
p[:, 2] = v
fig, ax = plt.subplots(1, 2)
plot_pat(ax[0], p)
p[:, 3] = v
plot_pat(ax[1], p)
ax[0].set_xticks(np.arange(3))
ax[0].set_yticks(np.arange(0, subc_num))
ax[1].set_xticks(np.arange(4))
ax[1].set_yticks(np.arange(0, subc_num))
plt.tight_layout()
fig.savefig('nr_dmrs_type2.png', bbox_inches='tight')
