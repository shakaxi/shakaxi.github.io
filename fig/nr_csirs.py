import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Consolas"
plt.rcParams['font.size'] = 8
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['text.usetex'] = True

def plot_pat(ax: plt.Axes, pat: np.ndarray) -> None:
    '''Plot a pattern based on a given matrix.'''
    ax.imshow(pat)
    ax.set_xticks([0], [r'$\ell_0$'])
    ax.set_yticks([], None)

subc_num = 12

# Single-port
p1 = np.zeros((subc_num, 1))
for f in np.arange(4):
    p1[f::4] = f
fig1, ax1 = plt.subplots()
plot_pat(ax1, p1)
fig1.savefig('nr_csirs_1port.png', bbox_inches='tight')

# 2-port
p2 = np.zeros((subc_num, 1))
for f in np.arange(6):
    p2[2 * f: 2 * (f + 1)] = f
fig2, ax2 = plt.subplots()
plot_pat(ax2, p2)
ax2.set_title('2x-FD-OCC')
fig2.savefig('nr_csirs_2port.png', bbox_inches='tight')

# 4-port
p41 = p2
p42 = np.concatenate((p2, p2 + 6), 1)
fig4, ax4 = plt.subplots(1, 2)
plot_pat(ax4[0], p41)
plot_pat(ax4[1], p42)
ax4[0].set_title('2x-FD-OCC')
ax4[1].set_title('2x-FD-OCC')
fig4.savefig('nr_csirs_4port.png', bbox_inches='tight')

# 8-port
p81 = p2
p82 = p42
p83 = np.concatenate((p2, p2), 1)
fig8, ax8 = plt.subplots(1, 3, width_ratios=[1, 1, 3])
plot_pat(ax8[0], p81)
plot_pat(ax8[1], p82)
plot_pat(ax8[2], p83)
ax8[0].set_title('2x-FD-OCC')
ax8[1].set_title('2x-FD-OCC')
ax8[2].set_title('2x-FD-OCC + 2x-TD-OCC')
fig8.savefig('nr_csirs_8port.png', bbox_inches='tight')

# 12-port
p121 = p2
p122 = np.concatenate((p2, p2), 1)
fig12, ax12 = plt.subplots(1, 2, width_ratios=[1, 2])
plot_pat(ax12[0], p121)
plot_pat(ax12[1], p122)
ax12[0].set_title('2x-FD-OCC')
ax12[1].set_title('2x-FD-OCC + 2x-TD-OCC')
fig12.savefig('nr_csirs_12port.png', bbox_inches='tight')

# 16-port
p161 = np.concatenate((p2, p2 + 6), 1)
p162 = np.concatenate((p2, p2), 1)
fig16, ax16 = plt.subplots(1, 2, width_ratios=[1, 2])
plot_pat(ax16[0], p161)
plot_pat(ax16[1], p162)
ax16[0].set_title('2x-FD-OCC')
ax16[1].set_title('2x-FD-OCC + 2x-TD-OCC')
fig16.savefig('nr_csirs_16port.png', bbox_inches='tight')

# 24-port and 32-port
p241 = np.concatenate((p2, p2 + 6, -1 * np.ones((subc_num, 1)), p2, p2 + 6), 1)
p242 = np.concatenate((p2, p2, -1 * np.ones((subc_num, 1)), p2, p2), 1)
p243 = np.concatenate((p2, p2, p2, p2), 1)
fig24, ax24 = plt.subplots(1, 3)
ax24[0].imshow(p241)
ax24[0].set_xticks([0, 3], [r'$\ell_0$', r'$\ell_1$'])
ax24[0].set_yticks([], None)
ax24[1].imshow(p242)
ax24[1].set_xticks([0, 3], [r'$\ell_0$', r'$\ell_1$'])
ax24[1].set_yticks([], None)
plot_pat(ax24[2], p243)
ax24[0].set_title('2x-FD-OCC')
ax24[1].set_title('2x-FD-OCC + 2x-TD-OCC')
ax24[2].set_title('2x-FD-OCC + 4x-TD-OCC')
for f in ax24:
    f.set_aspect('auto')
fig24.savefig('nr_csirs_24port.png', bbox_inches='tight')
fig24.savefig('nr_csirs_32port.png', bbox_inches='tight')
