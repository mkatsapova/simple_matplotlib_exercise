import numpy as np
import matplotlib.pyplot as plt
plt.subplot(111, polar=True)
phi = np.arange(0, 3*np.pi, 0.01)
rho = 2*phi
plt.plot(phi, rho, lw=5, color='pink')
plt.plot(phi, 3*rho, lw=2, color='y')
plt.savefig('figure_with_legend_ex_3.png')
plt.show()
