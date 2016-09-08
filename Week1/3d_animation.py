import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

alpha = 7.56
beta_x = 0.981
beta_y = 1.23
gamma = 10

def theory(x, y, i):
    return np.sin(beta_x*x + beta_y*y + gamma*i)
def animate(i):
    surf.set_zdata(theory(X, Y, i))
    return surf,

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = theory(X, Y, 0)

surf = ax.plot_wireframe(X, Y, Z)
surfs = [surf]

ax.set_zlim(-alpha, alpha)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

surf_ani = animation.FuncAnimation(fig, animate, 200, interval=100, blit=True) 

plt.show()