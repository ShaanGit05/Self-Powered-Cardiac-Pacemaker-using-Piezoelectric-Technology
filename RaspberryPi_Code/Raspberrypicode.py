import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Serial communication setup
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# ECG signal simulation
def gen_ecg_sig():
    t = np.linspace(0.2 * np.pi, np.pi, 100)
    return 500 + 200 * np.sin(t)

ecg_data = gen_ecg_sig()
sent_data = []

# Live plotting setup
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, len(ecg_data))
ax.set_ylim(250, 750)
ax.set_title("ECG Signal Sent to Arduino")
ax.set_xlabel("Sample")
ax.set_ylabel("ECG Value")

# Plot and send data function
def update(frame):
    if frame < len(ecg_data):
        value = int(ecg_data[frame])
        sent_data.append(value)

        # Send to Arduino
        ser.write(f"{value}\n".encode())
        print(f"Sent: {value}")

        # Read Arduino acknowledgment (optional)
        if ser.in_waiting:
            ack = ser.readline().decode().strip()
            print(f"Arduino: {ack}")
    else:
        plt.close(fig)

    line.set_data(range(len(sent_data)), sent_data)
    return line,

ani = FuncAnimation(fig, update, frames=range(len(ecg_data)), blit=True, interval=50)
plt.show()
ser.close(
