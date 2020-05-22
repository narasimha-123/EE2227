#Code by V. L. Narasimha
#May 22nd,2020
#Released under GNU GPL
import numpy as np  
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data1=np.loadtxt('ee18btech11046_spice3_1.dat')
data2=np.loadtxt('ee18btech11046_spice3_2.dat')  
plt.plot(data1[:,1],data2[:,1])  
plt.grid()
plt.xlabel("Ib")
plt.ylabel("Vbe")
plt.title('Vbe vs Ib characteristics')

slope = (data2[:,1][741]-data2[:,1][740])/(data1[:,1][741]-data1[:,1][740]) # Gives slope of curve at near Q-point
print('rpi = ',slope)
plt.show()



#if using termux
plt.savefig('./figs/ee18btech11046/ee18btech11046_spice_result3.pdf')
plt.savefig('./figs/ee18btech11046/ee18btech11046_spice_result3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11046/ee18btech11046_spice_result3.pdf"))
