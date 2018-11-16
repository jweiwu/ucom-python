import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 10, 0.5)
plt.figure(1)
plt.subplot(311)
plt.plot(t, t, 'r-')
plt.subplot(312)
plt.plot(t, t ** 2, 'g*-')
plt.subplot(3, 1, 3)
plt.plot(t, t ** 3, 'b^')
plt.show()
