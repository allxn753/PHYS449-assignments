from CryoSwitchController.CryoSwitchController import Cryoswitch


switch = Cryoswitch()

switch.start()   # enables rails

# Set voltage and pulse duration
switch.set_output_voltage(25)
switch.set_pulse_duration_ms(15)

for i in range(1,7):
    switch.disconnect(port='A', contact=i)
