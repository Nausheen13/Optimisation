import numpy as np
import matplotlib.pyplot as plt

def Rosen(X):
    """
    Rosenbrock function
    """
    x, y = X
    return (1-x)**2 + 100. * (y-x**2)**2


x = np.linspace(-2., 2., 100)
y = np.linspace(-1., 3., 100)
X, Y = np.meshgrid(x,y)
Z = Rosen( (X, Y) )

fig = plt.figure(0)
plt.clf()
plt.contourf(X, Y, Z,20)
plt.colorbar()
plt.contour(X, Y, Z,20, colors = "black")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()



# %%
# %%
