'''
This script will handle the control signal used to initiate the trigger.
pin 22 is used as the gun control signal
'''

import time
import socket
import RPi.GPIO as gpio

BUFFER = 1024

# ignore all warnings regarding the pins being in use as we dont care
gpio.setwarnings(False)

# set reset pin
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()

connected = False
while not connected:
    try:
        client_socket.connect(('192.168.4.1', 9696))
        connected = True
        print("Connected!")
        break
    except Exception as e:
        print("Failed to connect: " + format(e) + " retrying...")
        time.sleep(1)
        pass

# listen for incoming data
socket.listen(1)
conn, addr = socket.accept()

while True:
    data = conn.recv(BUFFER)
    print("Received: ", data)
    if data == 1:
        gpio.out(22, 1)
        time.sleep(2)  # provide a time delay to prevent switching too fast
    elif data == 0:
        gpio.out(22, 0)
        time.sleep(2)  # provide a time delay to prevent switching too fast
