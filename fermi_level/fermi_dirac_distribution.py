# author : Dasharath Adhikari 
import sys
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True

# Fermi_Dirac distribution
def fermi_dirac_dist(e, ef, T):
    """
    e - energy level in eV
    ef - fermi energy level in eV
    T - temperature
    """
    kb = 8.33e-5      # Boltzmann constant in eV/K
    
    if T == 0.0:
        f2 = []
        for i in range(len(e)):
            if e[i] <= ef:
                f2.append(1.0)
            else:
                f2.append(0.0)    
        f2 = np.asarray(f2)
    else:
        f1 = np.exp((e-ef)/(kb*T))
        f2 = 1/(1+f1)           
    return f2

ef = 0.5 
e = np.arange(0.01, 1.05, 0.01)
fdd = fermi_dirac_dist(e, ef, 0.0)
#print(fdd)
#sys.exit()
fig, ax = plt.subplots(1,1, figsize=(5, 5), dpi= 150)
ax.plot(e, fdd, 'o--', lw='1', markersize=3, c='g', label = 'T = 0.0 K')
ax.axvline(x=0.5, c='r', ls='--',lw='0.5')
#ax.axhline(y=0.1, c ='r', ls='--',lw='0.5', label = 'Intrinsic Fermi Level')
ax.set_xlabel(r'Energy [eV]')
ax.set_ylabel('Fermi-Dirac Distribution [ab. unit]')
#ax.set_xlim(1e10, 2e20)
ax.legend()
ax.text(0.55, 0.5, r'E$_{f}$ = 0.5 eV', c='r', fontsize=12)
ax.set_title('Fermi Dirac Distribution')
plt.show()


# Temperature dependence
T = np.arange(0, 450, 50, dtype=float) 
# for n-type doping 
for i in range(len(T)):
    #print(T[i])
    fdd = fermi_dirac_dist(e, ef, T[i])
    plt.plot(e, fdd,  label = r'{} K'.format(T[i]))
    #plt.plot(e, fdd, 'o--', lw='1', markersize=3, label = r'{} K'.format(T[i]))
    plt.vlines(x=0.5, ymin= fdd.min()-0.05, ymax= fdd.max()+0.05, colors='r', linestyles='--',linewidth=.5)
    plt.xlabel(r'Energy [eV]')
    plt.ylabel('Fermi-Dirac Distribution [ab. unit]')
    plt.xlim(0, 1)
    plt.ylim(-0.05, 1.05)
    plt.legend()
    plt.text(0.55, 0.5, r'E$_{f}$ = 0.5 eV', c='r', fontsize=12)
    plt.title(r'Fermi Dirac Distribution')
plt.show()





