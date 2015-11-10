import numpy as np
import matplotlib.pyplot as pp

data = np.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')

fig =pp.figure(figsize=(10.0,3.0))

axes1 = fig.add_subplot(1,3,1)
axes2 = fig.add_subplot(1,3,2)
axes2 = fig.add_subplot(1,3,3)

axes1.set_ylabal('average')
axes1.plot(data.mean(axis=0))
axes2.set_ylabal('max')
axes2.plot(data.mean(axis=0))
axes3.set_ylabal('min')
axes3.plot(data.mean(axis=0))

fig.tight_layout()

pp.show()
