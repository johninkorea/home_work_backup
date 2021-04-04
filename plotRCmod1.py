import numpy as np
from scipy.special import i0 as bessi0
from scipy.special import i1 as bessi1
from scipy.special import k0 as bessk0
from scipy.special import k1 as bessk1
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def fEFE(p,x):  # MOND model: a0 - critical acceleration,  e - EFE parameter (see Chae et al. 2020)
    a0=p[0]
    e=p[1]
    u=1/x
    Ae=e*(1+e/2)/(1+e)
    Be=1+e
    return 0.5-Ae*u+np.sqrt((0.5-Ae*u)**2+Be*u)

GMsun_kpc = 4.300917248e-6 # G*M_sun/kpc (km/s)^2
GMsun_kpc2 = 1.3938e-19 # G*M_sun/kpc^2 m/s^2

Md = 1.e11   #  mass of the disk in solar masses
a0 = 1.2e-10   # MOND critical acceleration in m/s^2
Rd = 5.        # disk scale length in kpc
R = np.logspace(-2.,1.7,100)   #  radius in units of kpc
M_R = Md*(1-np.exp(-R/Rd)*(1+R/Rd))
Vsphere = np.sqrt(GMsun_kpc*M_R/R)
y = R/(2*Rd)
bess = bessi0(y)*bessk0(y)-bessi1(y)*bessk1(y)
Vd = np.sqrt(2*GMsun_kpc*(Md/Rd)*y**2*bess)

Mb = 2.e10
R_H=1.5/(1.+np.sqrt(2.))       # Hernquist radius in kpc
Vb=1.e-3*np.sqrt(Mb)*np.sqrt(4.3)*(R/(R+R_H)**2)**0.5  # rotation velocity due to the bulge (km/s)

Vtot=np.sqrt(Vb**2+Vd**2)
gtot=(1.e3*Vtot)**2/(R*3.086e+19)
Vtot_mond = np.sqrt(fEFE([a0,0.],gtot/a0))*Vtot

fig = plt.figure(figsize=(15,10))
gs = gridspec.GridSpec(10,10) 
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes',labelsize=25)
plt.rcParams['axes.linewidth'] = 1.5
plt.subplots_adjust(left=0.07,right=0.97,bottom=0.05,top=0.97) #,wspace=100.,hspace=40.)
ax = plt.subplot2grid((100,100), (0,0), rowspan=95, colspan=99) 
plt.xlabel(r'$R$ [kpc]')
plt.ylabel(r'$V(R)$ [km/s]')
ax.plot(R,Vd,c='b',label=r'Exponential disk')
ax.plot(R,Vb,c='r',label=r'Hernquist bulge')
ax.plot(R,Vsphere,c='b',ls='--',label=r'Sphere')
ax.plot(R,Vtot,c='k',label=r'Disk + Bulge')
ax.plot(R,Vtot_mond,c='k',ls='--',label=r'Disk + Bulge: MOND')
ax.legend(fontsize=20)

fig.tight_layout()
plt.savefig('fig_RC_efe.png')
plt.close(fig)
