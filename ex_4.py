import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 2*np.pi, 0.01)
r = 4
plt.plot(r*np.sin(t), r*np.cos(t), lw=1, color='g')
plt.axis('equal')
plt.savefig('figure_with_legend_ex_4.png')
plt.show()
