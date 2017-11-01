import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as inter
import bitstring

amplitude = 128
duracao = 10.0
Fs = 8000
f = 0.5
sample = 8000
sampling = 0.1

x = np.arange(0, duracao, duracao/sample)
y = amplitude * np.sin( np.pi * x * f)
z = inter.interp1d(x, y, kind='zero', axis=0)

xnew = np.arange(0, duracao, 0.1)
ynew = z(xnew)   # use interpolation function returned by `interp1d`
binary = np.empty(ynew.shape)
#for i in np.nditer(ynew):

plt.step(x, y, xnew, ynew.astype(int), '-', where="post")
#plt.plot(x, scipy.signal.cont2discrete(ynew))
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.show()
