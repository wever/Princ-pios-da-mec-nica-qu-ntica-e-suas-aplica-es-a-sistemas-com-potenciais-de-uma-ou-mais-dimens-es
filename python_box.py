import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

import matplotlib 
font = {'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

ax = plt.axes()
ax.plot([0,10], [0,0], 'b')

ax.plot([0,0], [0,10],'b')
ax.plot([10,10], [0,10],'b')

ax.plot([-0.5,-0.5], [0,10],'b')
ax.plot([10.5,10.5], [0,10],'b')

ax.plot([-0.5,0], [10,10],'b')
ax.plot([10,10.5], [10,10],'b')

ax.set_ylim([-1,15])
ax.yaxis.set_major_locator(plt.NullLocator())

labels=ax.axes.get_xticks().tolist()

ax.set_xticks([0,10])

ax.set_xticklabels(['0', 'a'])
print(labels)

ax.text(-0.5, 10.5, r'$\infty$')
ax.text(10, 10.5, r'$\infty$')


plt.show()
