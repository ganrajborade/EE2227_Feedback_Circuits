# License
'''
Code by Ganraj Borade
May 16,2020
Released under GNU GPL
'''

#Bode phase plot using scipy in python
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


#Defining the transfer function 

s1 = signal.lti([8*(np.pi**3)*3.16*(10**21)],[1, (2*np.pi*((10**6)+4.16*(10**5))),(4*(np.pi**2)*44.76*(10**10)),(8*(np.pi**3)*3.16*(10**16))])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)

#plotting phase plot of G(s)H :
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')

plt.axhline(y = -135,xmin=0,xmax= 0.6,color = 'r',linestyle='dashed',linewidth=2.0)
plt.axvline(x = 1.9782*(10**6),ymin=-0.6,ymax=0.6,color='k',linestyle='dashed',linewidth=2.0)
plt.plot(1.9782*(10**6),-135,'o')
plt.text(1.9782*(10**6)+(10**5),-135+4, '({}, {})'.format(1.9782e6,-135))
plt.title('Phase plot of G(s)H')
plt.semilogx(w,phase,linewidth=2.0)          # Bode phase plot
plt.grid() 
plt.show()

#if using termux
plt.savefig('./figs/ee18btech11016/ee18btech11016_resultbode.pdf')
plt.savefig('./figs/ee18btech11016/ee18btech11016_resultbode.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11016/ee18btech11016_resultbode.pdf"))
#else




