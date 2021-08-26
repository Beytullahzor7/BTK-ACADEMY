import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

"""
figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) #grafigin konum bilgilerini gireriz(sol,yukarı,genişlik,yükseklik)

axes_cube.plot(x,y,'y')
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.17,0.6,0.25,0.25])

axes_square.plot(x,z,'r')
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Z Axis")
axes_square.set_title("Quad")
"""

# figure = plt.figure()

# axes = figure.add_axes([0,0,1,1])

# axes.plot(x,z,label = "Sqaure")
# axes.plot(x,y,label = "Cube")
# axes.legend(loc=4)

fig,axes = plt.subplots(nrows = 2,ncols = 1)

axes[0].plot(x,y)
axes[0].set_title("Square")

axes[1].plot(x,z)
axes[1].set_title("Cube")

plt.tight_layout()
fig.savefig("Matplotlib/figure1.png")
plt.show()