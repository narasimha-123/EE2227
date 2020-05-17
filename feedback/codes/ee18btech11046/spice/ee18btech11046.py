import numpy as np  
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11046_1.dat')  
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time in sec")
plt.ylabel("Output Voltage")
plt.title('Closed loop system Output Voltage')
#plt.show()


#if using termux
plt.savefig('./figs/ee18btech11046/ee18btech11046_spice_result.pdf')
plt.savefig('./figs/ee18btech11046/ee18btech11046_spice_result.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11046/ee18btech11046_spice_result.pdf"))
