import numpy as np
import matplotlib.pyplot as plt
import control

num = [6,0]         # Coefficients of Numerator of Tranfer Function
den = [1,2,5]       # Coefficients of Denominator of Tranfer Function
G = control.TransferFunction(num, den)  # Transfer Function

rlist, klist = control.rlocus(G)   # Root Locus of Transfer Function


ans1 = np.roots(num)   # Zeros of Transfer Fuunction
ans2 = np.roots(den)   # Poles of Transfer Function

X1 = [x.real for x in ans1]
Y1 = [x.imag for x in ans1]
plt.scatter(X1,Y1, color='orange', label = 'Zeros')  # Plotting zeros of Transfer Function
X2 = [x.real for x in ans2]
Y2 = [x.imag for x in ans2]
plt.scatter(X2,Y2, marker = 'x',color = 'blue', label = 'Poles')  # Plotting poles of Transfer Function
plt.scatter(-np.sqrt(5),0,color = 'red', label = 'Breakaway Point') #Breakaway point
plt.xlabel('Real axis')
plt.ylabel('Imaginary axis')
plt.title('Root Locus Plot')
plt.legend()
plt.grid()
plt.show()