from CryoSwitchController.CryoSwitchController import Cryoswitch
import matplotlib.pyplot as plt
import numpy as np

# Initialize
switch = Cryoswitch()

# Start controller hardware
switch.start()   # enables rails

# Set voltage and pulse duration
switch.set_output_voltage(25)
switch.set_pulse_duration_ms(15)

# Switch actuator contact
switch.connect(port='A', contact=5)
test = switch.disconnect(port='A', contact=5)
print(test)

xpoints = np.linspace(0, 25, len(test))
ypoints = np.array(test)

plt.plot(xpoints, ypoints)
plt.title("Current Waveform for Room Temperature")
plt.xlabel("Time (ms)")
plt.ylabel("Current (mA)")
plt.show()
