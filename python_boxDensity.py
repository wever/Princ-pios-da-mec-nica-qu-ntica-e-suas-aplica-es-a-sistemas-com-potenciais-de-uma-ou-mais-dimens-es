import numpy as np

import matplotlib 

matplotlib.rcParams.update({'font.size': 24})

import matplotlib.pyplot as plt

def waveFunction(n):
    return np.sin(n*np.pi*x/(L[-1] - L[0]))

L = [0,5]
step = 0.05
x = np.arange(L[0],L[-1]+step,step)

N = 4

for n in range(1,N+1):
    plt.axhline(n**2, 0, L[-1],color='k', lw=2)
    plt.plot(x, waveFunction(n)*waveFunction(n)+n**2, lw=2)
#plt.ticks([],[])

plt.ylabel(r'$n^2$')
plt.xlabel('L (a - 0) / au')
plt.xlim(L[0],L[-1])
plt.show()
