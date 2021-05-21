import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

import matplotlib
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

kB = 1.380658e-23 # J⋅K−1 
c = 2.998e8             # m/s
h = 6.62607004e-34       # m2 kg/s


def planckDistribution(lamb, T):
    return 8.0*np.pi*h*c/(lamb**5*(np.exp(h*c/(lamb*kB*T))-1))

def rayleigh_jeans(lamb,T):
    return 8.0*np.pi*kB*T/lamb**4


lamb = np.linspace(50,80000,1000)*1e-9  # m
T = 300 # K

print(planckDistribution(lamb,T))

fig, ax1 = plt.subplots()

plt.title("Temperatura = 300 K")
ax1.plot(lamb/1e-9, planckDistribution(lamb,T),label="Distribuição de Planck")

ax1.plot(lamb/1e-9, rayleigh_jeans(lamb,T),label="Lei de Rayleigh-Jeans")

ax1.set_ylim([0,0.5])

ax1.set_xlabel("Comprimento de onda (nm)")
ax1.set_ylabel(r"Distrubuição de probabilidade ($\rho$)")

ax1.legend()

axins = zoomed_inset_axes(ax1,40,loc='center right', 
                          axes_kwargs={"facecolor" : "lightgray"})

# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
pp,p1,p2 = mark_inset(ax1, axins,loc1=1,loc2=3, ec="0.8")
pp.set_fill(True)
pp.set_facecolor("lightgray")
pp.set_edgecolor("k")

axins.plot(lamb/1e-9, planckDistribution(lamb,T),label="Distribuição de Planck")
axins.set_xlim([50,800])
axins.set_ylim([0,0.005])


plt.show()
