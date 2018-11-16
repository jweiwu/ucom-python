import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0, 2)
x3 = np.linspace(0.1, 10)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
y3 = np.tan(x3) * np.log2(x3)
plt.subplot(3, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('')
plt.ylabel('figure1')
plt.subplot(3, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time')
plt.ylabel('figure2')
plt.subplot(3, 1, 3)
plt.plot(x3, y3, 'g*-')
print x1
print x2
print x3
plt.show()
