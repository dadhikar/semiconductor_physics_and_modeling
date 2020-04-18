# author : Dasharath Adhikari 
import sys
import math
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True


def fermi_potential_shift(T, fermi_int, intrinsic_carrier, major_carrier, state):
    """
    intrinsic Fermi potential - Ei/q , where q electronic charge
    extrinsic Fermi potenial - Ef/q
    potential shift due to doping = (Ef - Ei) / q, defined as phi
    phi = + phi_T * ln(no/ni);  phi_T =  kB*T/q for n-type doping
    phi = - phi_T * ln(po/ni);  phi_T =  kB*T/q for n-type doping
    we can consider no ~ ND (donor concentration) and po ~ NA (acceptor concentration)
    """  
    phi_T = 0.0259 *(T/300)     # in Volts
    if state == - 1.0:           # for p-type
        phi_T *= state
    else:                       # for n-type
        phi_T = phi_T
    fermi_pot = fermi_int  + phi_T * np.log(major_carrier/intrinsic_carrier)
    return fermi_pot

# Room temperature study
#for  n-type doping
T = 300     # in Kelvin
fermi_int = 0.1   # in Volts and is taken arbitrary
intrinsic_carrier = 1e10  # per cm^3
x = np.arange(10, 21, 1, dtype=float)
n_carrier = np.power(10, x)   # different donor-doping concentration per cm3 
state = 1
potential_n = fermi_potential_shift(T, fermi_int, intrinsic_carrier, n_carrier, state)
# for p-type doping 
p_carrier = np.power(10, x)   # different donor-doping concentration per cm3 
state = -1
potential_p = fermi_potential_shift(T, fermi_int, intrinsic_carrier, p_carrier, state)
fig, ax = plt.subplots(1,1, figsize=(5, 5), dpi= 150)
ax.semilogx(n_carrier, potential_n,  label = 'n-type, T = 300 K')
ax.semilogx(p_carrier, potential_p,  label = 'p-type, T = 300 K')
#ax.axvline(x=0, c='r', ls='--',lw='0.5', label = 'pn junction')
ax.axhline(y=0.1, c ='r', ls='--',lw='0.5', label = 'Intrinsic Fermi Level')
ax.set_xlabel(r'N$_{D}$(or N$_{A}$) [cm$^{-3}$]')
ax.set_ylabel('Fermi Potential [V]')
ax.set_xlim(1e10, 2e20)
ax.legend(loc =2)
ax.text(1e12, 0.12, 'V  = 0.1 V', c='r', fontsize=12)
ax.set_title('Fermi Potential on Carrier Concentration')
plt.show()

# Temperature dependence study
T = np.arange(250, 360, 10, dtype=float)  # temperature range

# for n-type doping 
for i in range(len(T)):
    #print(T[i])
    fermi_int = 0.1   # in Volts and is taken arbitrary
    intrinsic_carrier = 1e10  # per cm^3
    x = np.arange(10, 21, 1, dtype=float)
    n_carrier = np.power(10, x)   # different donor-doping concentration per cm3 
    state = 1
    potential_n = fermi_potential_shift(T[i], fermi_int, intrinsic_carrier, n_carrier, state)
    plt.semilogx(n_carrier, potential_n,  label = r'{} K'.format(T[i]))
    plt.hlines(y=0.1, xmin= n_carrier.min(), xmax=n_carrier.max(), colors='r', linestyles='--',linewidth=.5)
    plt.xlabel(r'Donor Concentration (N$_{D}$) [cm$^{-3}$]')
    plt.ylabel('Fermi Potential [V]')
    plt.xlim(1e10, 2e20)
    plt.legend(loc =2)
    plt.text(1e12, 0.12, 'V  = 0.1 V', c='r', fontsize=12)
    plt.title(r'n-type semiconductor')
plt.show()


# for p-type doping 
for i in range(len(T)):
    #print(T[i])
    fermi_int = 0.1   # in Volts and is taken arbitrary
    intrinsic_carrier = 1e10  # per cm^3
    x = np.arange(10, 21, 1, dtype=float)
    p_carrier = np.power(10, x)   # different acceptor-doping concentration per cm3 
    state = 1
    potential_p = fermi_potential_shift(T[i], fermi_int, intrinsic_carrier, p_carrier, state)
    plt.semilogx(n_carrier, potential_p,  label = r'{} K'.format(T[i]))
    plt.hlines(y=0.1, xmin= n_carrier.min(), xmax=n_carrier.max(), colors='b', linestyles='--',linewidth=.5)
    plt.xlabel(r'Acceptor Concentration (N$_{A}$) [cm$^{-3}$]')
    plt.ylabel('Fermi Potential [V]')
    plt.xlim(1e10, 2e20)
    plt.legend(loc =2)
    plt.text(1e12, 0.12, 'V  = 0.1 V', c='b', fontsize=12)
    plt.title(r'p-type semiconductor')
plt.show()