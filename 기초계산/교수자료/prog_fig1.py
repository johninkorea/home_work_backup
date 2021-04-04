import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

x=np.linspace(0.,10.,20)
y=0.5*x+0.2*np.random.randn(20)
yerr=0.15+0.03*np.random.randn(20)

y0=0.5*x

fig = plt.figure(figsize=(10,6))
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes',labelsize=25)

plt.scatter(x,y,s=10,c='b',marker='o',alpha=1.,label='data')
plt.errorbar(x,y,yerr=yerr,c='b',fmt='none',elinewidth=1,capsize=1)
plt.plot(x,y0,c='r',lw='2',label='line fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('linear relation',fontsize='25')
plt.legend(fontsize=20)

fig.tight_layout()
plt.show()
#plt.savefig('fig1.png')
#plt.savefig('fig1.pdf')
