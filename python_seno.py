import numpy as np
import matplotlib.pyplot as plt

import matplotlib 
font = {'weight' : 'bold',
        'size'   : 88}

matplotlib.rcParams.update({'font.size': 32})

color=['m','g','r','b']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)


left,right = ax.get_xlim()
low,high = ax.get_ylim()
plt.arrow( left, 0, right -left, 0, length_includes_head = True, head_width = 0.05 )
plt.arrow( 0, low, 0, high-low, length_includes_head = True, head_width = 0.05 ) 

plt.arrow( left, 0, -right +left, 0, length_includes_head = True, head_width = 0.05 )
plt.arrow( 0, low, 0, -high+low, length_includes_head = True, head_width = 0.05 ) 

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(1.0)

x = r*np.cos(theta)
y = r*np.sin(theta)

#plt.axis('off')

plt.text(0.75, 0, r'$\pi$')
plt.text(0, 0.75, r'$\pi$')

plt.text(-0.75, 0, r'$\pi$')
plt.text(0, -0.75, r'$\pi$')

plt.text(1.25, 0, r'$\pi$')
plt.text(0, 1.25, r'$\pi$')

plt.text(-1.25, 0, r'$\pi$')
plt.text(0, -1.25, r'$\pi$')

plt.xlim([-1.25,1.25])
plt.ylim([-1.25,1.25])

plt.plot(x,y)
#plt.grid()

plt.show()
