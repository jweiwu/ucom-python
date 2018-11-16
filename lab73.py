import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

randomSequence = \
    pd.DataFrame(np.random.normal(1.0, 0.08, (100, 8)))
accumulates = randomSequence.cumprod()
accumulates.plot()
plt.title('simulation')
plt.xlabel('time-sequence')
plt.ylabel('certain values')
plt.legend(loc=0)
plt.show()
