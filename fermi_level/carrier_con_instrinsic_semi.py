"""
For an intrinsic semiconductor, calculating electron density
at conduction band.
This involves solving Fermi-Dirac integral
"""
# importing required libraries 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True
from scipy.integrate import quad


def fermi_dirac_dist(e, ef, T):
    """
    define Fermi-Dirac distribution function
    where, e - energy level in eV
    ef - fermi energy level in eV
    T - temperature
    return:
    probability value for the distribution
    """
    kb = 8.33e-5      # Boltzmann constant in eV/K
    if T == 0.0:   
        if e <= ef:
            f2 = 1.0
        else:
            f2 = 0.0    
    else:
        f1 = np.exp((e-ef)/(kb*T))
        f2 = 1/(1+f1)           
    return f2

# T = np.linspace(2, 100, 20, endpoint=True)
# e = np.linspace(0.2, 0.4, 50, endpoint=True)
# print(T)
# f = fermi_dirac_dist(e, 0.3, 300)
# plt.plot(e, f)
# plt.show()

def density_of_states(e, ec):
    """
    Density of states near the bottom of the conduction band
    for low-enough carrier density and temperature
    ec (in eV) - conduction band edge
    e (in eV)- energy value close to ec
    """
    me = 0.5110e6   # electron mass (in eV)
    factor = 0.91   # this will be material dependent
    meff = factor*me  # effective electron mass
    h_cross = 6.582e-16  # in eV-s
    f1 = (np.sqrt(2)/np.power(np.pi, 2))*np.power(meff, 1.5)
    f2 = np.power(e-ec, 0.5)/np.power(h_cross, 3)
    return f1*f2

# print(density_of_states(0.302, 0.3))


def fermi_dirac_integrand(x, xf):
    """
    x = (e-ec)/kB*T
    xf = (ef-ec)/kB*T
    ef = Fermi enegry in eV
    ec = conduction band edge in eV
    kB = Boltzmann constant
    T = Temperature
    """
    return np.power(x, 0.5)/(1+np.exp(x-xf))


def fermi_dirac_integral(xf):
    """
    """
    integral_value, _ = quad(func= fermi_dirac_integrand, a=0, b=10, args=(xf),
                                           full_output=0, epsabs=1.49e-08, epsrel=1.49e-08, limit=50,
                                           points=None, weight=None, wvar=None, wopts=None, maxp1=50, limlst=50)
    return integral_value

fermi_integral = []
xf = np.linspace(-10, 10, 1000)
for x in xf:
    integral_value = fermi_dirac_integral(x)
    # print(xf, integral_value)
    fermi_integral.append(integral_value)

plt.semilogy(xf, np.asarray(fermi_integral), 'ro', ms=2.5, label=r'Fermi-Dirac')
plt.semilogy(xf, 0.5*np.power(np.pi, 0.5)*np.exp(xf), 'ko', ms=2.5, label=r'Boltzmann approx.' )
plt.vlines(x=0.0, ymin= 1e-5, ymax= 30, colors='g', linestyles='--',linewidth=2.0)
plt.xlabel(r'(E$_{f}$ - E$_{c}$) / k$_{B}$T [no unit]')
plt.ylabel('Fermi-Dirac Integral [ab. unit]')
plt.xlim(-10, 10)
plt.ylim(1e-5, 25)
plt.legend()
#plt.text(0.55, 0.5, r'E$_{f}$ = 0.5 eV', c='r', fontsize=12)
plt.title(r'Intrinsic Semiconductor')
plt.show()