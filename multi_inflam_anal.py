import numpy as np
import matplotlib.pyplot as pp
import glob 

filenames = glob.glob('../data/inflammation*.csv')
filenames_slice3 = filenames[0:3]

for file in filenames_slice3:
    data = np.loadtxt(fname=file, delimiter=',')

    fig = pp.figure(figsize=(10.0,3.0))

    axes1 = fig.add_subplot(1,3,1)
    axes2 = fig.add_subplot(1,3,2)
    axes3 = fig.add_subplot(1,3,3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))
    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))
    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    fig.tight_layout()

pp.show()
