import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

x=np.linspace(0.,10.,100)
y=0.5*x+0.2*np.random.randn(100)
yerr=0.15+0.03*np.random.randn(100)

y0=0.5*x

fig = plt.figure(figsize=(20,12))
gs = gridspec.GridSpec(10,20)
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes',labelsize=25)

ax = plt.subplot2grid((100,200), (5, 0), rowspan=95, colspan=90)   # panel 1
ax.scatter(x,y,s=10,c='b',marker='o',alpha=1.,label='data')
ax.errorbar(x,y,yerr=yerr,c='b',fmt='none',elinewidth=1,capsize=1)
ax.plot(x,y0,c='r',ls='dashed',lw='2',label='line fit')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('linear relation',fontsize='25')
ax.set_xlim(-1,11)
ax.set_ylim(-1,6)
ax.legend(fontsize=20)
axins = inset_axes(ax,width="30%",height="30%",loc=4, borderpad=3) # in-set
dy=y-y0
hist = axins.hist(dy,bins=9,range=(-0.5,0.5),color='r',edgecolor='k',lw=2)

ax = plt.subplot2grid((100,200), (5, 120), rowspan=40, colspan=75)   # panel 2
dy=y-y0
hist = ax.hist(dy,bins=9,range=(-0.5,0.5),color='r',edgecolor='k',lw=2)
ax.set_xlabel('y residual')
ax.set_ylabel('number')

ax = plt.subplot2grid((100,200), (60, 120), rowspan=40, colspan=75)   # panel 3
dy=dy/np.std(dy)
hist = ax.hist(dy,bins=9,range=(-4,4),color='deepskyblue',edgecolor='k',lw=2)
ax.set_xlabel('y normalized residual')
ax.set_ylabel('number')

fig.tight_layout()
#plt.show()
plt.savefig('fig2.png')
#plt.savefig('fig2.pdf')
plt.close(fig)
