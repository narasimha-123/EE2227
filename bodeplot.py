from scipy import signal
import matplotlib.pyplot as plt
#-----------Bode Plot-------------------#

system = signal.lti([1],[1,-1001,10])  # Input Transfer Function
r = range(0, 1000000)
f,mag,phase = signal.bode(system,w=r)
plt.figure()
plt.title("Magnitude")
plt.grid(True, which="both")
plt.semilogx(f,mag)   # Frequency vs Magnitude plot
plt.figure()
plt.grid(True, which="both")
plt.title("Phase")
plt.semilogx(f,phase)    # Frequency vs Phase plot
plt.show()
