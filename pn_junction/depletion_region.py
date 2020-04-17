"""Created on Mon Mar  9 14:57:04 2020 @author: dadhikar """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True


# Electric field profile for p-region
def Field_P_Region(x):
    e = 1 # charge 
    Na = 1 # donor density
    es = 1 # semiconductor permitivity
    xp = 1 # junction edge
    return (-1/es)*(x + xp)*(e*Na)

# Electric potential profile for p-region
def Potential_P_Region(x):
    e = 1 # charge 
    Na = 1 # donor density
    es = 1 # semiconductor permitivity
    xp = 1 # junction edge
    return (0.5/es)*(e*Na)*(x + xp)**2


# Electric field profile for n-region
def Field_N_Region(x):
    e = 1 # charge 
    Nd = 1 # donor density
    es = 1 # semiconductor permitivity
    xn = 1 # junction edge
    return (-1/es)*(xn - x)*(e*Nd)
# Electric potential profile for p-region
def Potential_N_Region(x):
    e = 1 # charge 
    Nd = 1 # donor density
    Na = 1 # acceptor density
    es = 1 # semiconductor permitivity
    xn = 1 # n - junction edge
    xp = 1 # p - junction edge
    return (1/es)*(e*Nd)*(xn*x - 0.5*x**2) + (0.5/es)*(e*Na)*xp**2

xp = np.arange(-1, 0, 0.001)
Ep = Field_P_Region(xp)
Vp = Potential_P_Region(xp)
xn = np.arange(0, 1, 0.001)
En = Field_N_Region(xn)
Vn = Potential_N_Region(xn)
fig, ax = plt.subplots(1,2, figsize=(10,10), dpi= 150)

ax[0].plot(xp, Ep, 'b', label = 'Electric field')
ax[0].plot(xn, En, 'b')
ax[0].axvline(x=0, c='r', ls='--',lw='0.5', label = 'pn junction')
ax[0].set_xlabel('x (cm)')
ax[0].set_ylabel('Electric Field (ab. unit)')
ax[0].set_xlim(-1, 1)
ax[0].legend()

ax[1].plot(xp, Vp, 'g', label = 'Electric Potential')
ax[1].plot(xn, Vn, 'g')
ax[1].axvline(x=0, c='r', ls='--',lw='0.5', label = 'pn junction')
ax[1].axhline(y=0, c ='k', ls='--',lw='0.5')
ax[1].axhline(y=1, c ='k', ls='--',lw='0.5')
ax[1].set_xlabel('x (cm)')
ax[1].set_ylabel('Electric Potential (ab. unit)')
ax[1].set_xlim(-1, 1)
ax[1].legend(loc =4)

plt.show()