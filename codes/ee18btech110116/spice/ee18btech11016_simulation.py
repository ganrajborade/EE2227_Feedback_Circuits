

import numpy as np
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11016_sim.dat')
plt.plot(data[:,0],data[:,1],linewidth=2.0)

plt.grid()
plt.xlabel("time")
plt.ylabel("Step response")
plt.title('Spice simulation for PM = 45 degrees')

#if using termux

'''
plt.savefig('./figs/ee18btech11016/ee18btech11016_spice_result.pdf')
plt.savefig('./figs/ee18btech11016/ee18btech11016_spice_result.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11016/ee18btech11016_spice_result.pdf"))
#else
'''
plt.show()


