This folder contains the Arduino sketch for pacemaker regulation.
This Arduino sketch receives ECG data from the Raspberry Pi and regulates it. It uses basic threshold logic to simulate pacemaker action—represented by LED blinking—when abnormal heart rate is detected.

Key Features:

Listens to serial input from Raspberry Pi

Controls LED based on signal value (simulates pacemaker)

Can be powered by piezoelectric energy in case of low power
