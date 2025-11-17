from CryoSwitchController.CryoSwitchController import Cryoswitch

# Initialize
switch = Cryoswitch()

# Start controller hardware
switch.start()   # enables rails

# Set voltage and pulse duration
switch.set_output_voltage(25)
switch.set_pulse_duration_ms(15)

# Switch actuator contact
switch.connect(port='A', contact=1)



