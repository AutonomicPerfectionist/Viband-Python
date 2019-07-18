from scipy.signal import lfilter
from numpy.fft import fft
import matplotlib.pyplot as plt
import numpy as np
import time
import struct

current_milli_time = lambda: int(round(time.time() * 1000))
def print_func(s):
     print s

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
fifo = open("/sys/class/misc/fastacc_mpu/device/fifo", 'rb', 12) #Open FIFO in Read-only binary mode, with a buffer size of 12 bytes
pwr = "/sys/class/misc/fastacc_mpu/device/pwr"
startTime = 0
xar = []
yar = ([], [], [])
def animate(val):
    #print "Animating..."
    vals = []
    
    hexVal = fifo.read(6)
    hexList = [struct.unpack('>h', ''.join(hexVal[i:i+2]))[0] for i in range(0, len(hexVal), 2)]
    print str(hexList)
    xar.append(current_milli_time() - startTime)
    yar[0].append(hexList[0])
    yar[1].append(hexList[1])
    yar[2].append(hexList[2])

with open(pwr, "w") as f:
     f.write('1')
startTime = current_milli_time()
samples = 500
for i in range(0, samples):
     animate(0)
     time.sleep(0.005)
time = current_milli_time() - startTime
fifo.close()
with open(pwr, 'w') as f:
     f.write('0')
ax1.clear()

powers = []
freqs = np.fft.fftfreq(np.asarray(yar[1]).size, (time * 1000) / samples)
idx = np.argsort(freqs)
for axis in yar:
    powers.append(np.abs(np.fft.fft(np.asarray(axis)) ** 2))

#for power in powers:
    #ax1.plot(power)
ax1.set_xscale('log')
ax1.autoscale()
ax1.plot(freqs[idx], powers[1][idx])
plt.show()
