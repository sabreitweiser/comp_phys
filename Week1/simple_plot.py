import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

plt.close()
alpha = 7.56
beta = 0.981
x = np.linspace(0,10)
x_exp = np.linspace(0,10,20)
def theory(x):
    return alpha*np.sin(beta*x)
plt.ylabel("Strain (10e-21)")
plt.xlabel("Time (s)")
plt.title("Strain v. Time, Detector 1")
th, = plt.plot(x, theory(x), label = "Numerical GR Prediction (30 SM)")
exp, = plt.plot(x_exp, theory(x_exp) + 0.5*npr.randn(np.size(x_exp)), 'ro', label = "Detector results")
plt.legend(handles = [th, exp], loc=1)
plt.show()