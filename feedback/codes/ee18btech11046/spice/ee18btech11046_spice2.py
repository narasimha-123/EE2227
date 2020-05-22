import numpy as np  
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data1=np.loadtxt('ee18btech11046_spice2_1.dat')
data2=np.loadtxt('ee18btech11046_spice2_2.dat')  
plt.plot(data1[:,1],data2[:,1])  
plt.grid()
plt.xlabel("Vbe")
plt.ylabel("Ic")
plt.title('Ic vs Vbe characteristics')

slope = (data2[:,1][741]-data2[:,1][740])/(data1[:,1][741]-data1[:,1][740]) # Gives slope of curve
print('gm = ',slope)
plt.show()



#if using termux
#plt.savefig('./figs/ee18btech11046/ee18btech11046_spice_result2.pdf')
#plt.savefig('./figs/ee18btech11046/ee18btech11046_spice_result2.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11046/ee18btech11046_spice_result2.pdf"))
