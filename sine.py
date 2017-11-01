import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as inter

amplitude = 5.0
duracao = 100.0
Fs = 8000
f = 0.5
sample = 800 * duracao
sampling = 3
b_number = 8
sens = amplitude / (2 ** b_number - 1)

x = np.arange(0, duracao, duracao / sample)
y = amplitude * np.sin(np.pi * x * f)
z = inter.interp1d(x, y, kind = 'zero', axis = 0)

def plotting():
	global b_number
	global amplitude
	global sens

	xnew = np.arange(0, duracao, sampling)
	ynew = z(xnew)

	count = 0
	ylist = ynew.tolist()
	for i in ylist:
		i = int(i / (amplitude / 2 ** b_number))
		binaryl = '{0:16b}'.format(i)
		print str(binaryl) + "\n"
		intyl = int(binaryl, 2)
		ylist[count] = intyl * sens
		count = count + 1
	plt.step(x, y, xnew, ylist, '-', where = "post")
	plt.xlabel('Tempo(s)')
	plt.ylabel('Amplitude')
	plt.show()

if __name__ == "__main__":
  plotting()
			
