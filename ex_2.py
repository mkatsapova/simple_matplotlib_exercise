import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10.01, 0.01)
t = np.arange(-10, 11, 1)

# subplot 1
sp = plt.subplot(221)
plt.plot(x, np.sin(x))
plt.title(r'$\sin(x)$')
plt.grid(True)

# subplot 2
sp = plt.subplot(222)
plt.plot(x, np.cos(x), 'g')
plt.axis('equal')
plt.grid(True)
plt.title(r'$\cos(x)$')

# subplot 3
sp = plt.subplot(223)
plt.plot(x, x**2, t, t**2, 'ro')
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
sp.spines['right'].set_position('center')
sp.spines['top'].set_position('center')
plt.title(r'$x^2$')

# subplot 4
sp = plt.subplot(224)
plt.plot(x, x)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
sp.spines['right'].set_position('center')
sp.spines['top'].set_position('center')
plt.grid(True)
plt.title(r'$x$')

plt.savefig('figure_with_legend_ex_2.png')
plt.show()
