from scipy import signal
import matplotlib.pyplot as plt
#-----------Bode Plot-------------------#

#if using termux
import subprocess
import shlex
#end if

system = signal.lti([-1/3.605],[0,-2,-4,-6,-1/(1.4936*3.605)],[96/1.4936])  # Input Transfer Function with poles and zeros as input

w,mag,phase = signal.bode(system)
y1 = w/w * 0
y2 = w/w * -150

plt.subplot(2,1,1)
plt.axvline(x=1.10953,linestyle = '--')
plt.plot(w,y1,linestyle='--',color = 'red') 
plt.plot(1.10953,0,'o',label='Point at Gain Crossover frequency') # Gain Crossover point
plt.text(1.10953,0, '({}, {})'.format(1.10953,0)) # Annotating the Gain Crossover point
plt.grid(True, which="both")
plt.ylabel('Magnitude()in dB')
plt.title('Bode plots of compensated system G(s)Gc(s)')
plt.semilogx(w,mag,'b',label = 'Magnitude Bodeplot')   # Frequency vs Magnitude plot
plt.legend()

plt.subplot(2,1,2)
plt.axvline(x=1.10953,linestyle = '--')
plt.plot(w,y2,linestyle='--',color = 'red')
plt.plot(1.10953,-150,'o',label='Point with Phase margin 30 degrees')
plt.text(1.10953,-150, '({}, {})'.format(1.10953,-150))
plt.grid(True, which="both")
plt.xlabel('Frequency(in Hz)')
plt.ylabel('Phase')
plt.semilogx(w,phase,label='Phase Bodeplot')    # Frequency vs Phase plot
plt.legend()


#if using termux
#plt.savefig('./figs/ee18btech11046_2.pdf')
#plt.savefig('./figs/ee18btech11046_2.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11046_2.pdf"))
plt.show()
