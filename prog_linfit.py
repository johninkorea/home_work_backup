import numpy as np
from scipy.optimize import minimize
from scipy.odr import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import gridspec

#np.random.seed(seed=456)
x0=np.linspace(0.,10.,100)
x=x0+0.5*((x0-5)/5+2)*np.random.randn(100)
y=0.5*x+0.5*((x0-5)/5+2)*np.random.randn(100)
yerr=0.3*((x0-5)/5+2)+0.03*np.random.randn(100)
xerr=0.3*((x0-5)/5+2)+0.03*np.random.randn(100)

def dsq(p):
    a=p[0]
    b=p[1]
    res = np.sum(((y-a-b*x)/yerr)**2)
    return res

sol=minimize(dsq,x0=[0.,0.5])  # minimize the sum of squared normalized residuals
pfit=sol.x

xpt=np.array([-100,100])

yfit=pfit[0]+pfit[1]*xpt

def f(p,x):
    res = p[0]+p[1]*x
    return res

linear = Model(f)

mydata = RealData(x, y, sx=xerr, sy=yerr)

myodr = ODR(mydata, linear, beta0=[0., 0.5])

myoutput = myodr.run()

myoutput.pprint()

p_odr = myoutput.beta
s_odr = myoutput.sd_beta

yodr=p_odr[0]+p_odr[1]*xpt

y0=0.5*x0

fig = plt.figure(figsize=(20,12))
gs = gridspec.GridSpec(10,20)
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.rc('axes',labelsize=12)

ax = plt.subplot2grid((100,200), (3, 0), rowspan=95, colspan=90)   # panel 1
ax.scatter(x,y,s=10,c='b',marker='o',alpha=1.,label='data')
ax.errorbar(x,y,xerr=xerr,yerr=yerr,c='b',fmt='none',elinewidth=1,capsize=1)
ax.plot(x0,y0,c='r',lw='2',label='true')
ax.plot(xpt,yfit,c='g',ls='--',lw='2',label='lsq fit')
ax.plot(xpt,yodr,c='orange',ls='--',lw='2',label='odr fit')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('linear relation',fontsize='25')
ax.set_xlim(-1,12)
ax.set_ylim(-1,7)
ax.legend(fontsize=10)

ax = plt.subplot2grid((100,200), (3, 120), rowspan=40, colspan=75)   # panel 2
dy=y-y0
hist = ax.hist(dy,bins=9,range=(-2.,2.),color='r',edgecolor='k',lw=2)
ax.set_xlabel('y residual')
ax.set_ylabel('number')

ax = plt.subplot2grid((100,200), (58, 120), rowspan=40, colspan=75)   # panel 3
dy=dy/np.std(dy)
hist = ax.hist(dy,bins=9,range=(-4,4),color='deepskyblue',edgecolor='k',lw=2)
ax.set_xlabel('y normalized residual')
ax.set_ylabel('number')

fig.tight_layout()
plt.show()
#plt.savefig('fig_linfit.png')
#plt.savefig('fig_linfit.pdf')
plt.close(fig)
