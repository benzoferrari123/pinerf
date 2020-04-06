'''
https://picamera.readthedocs.io/en/release-1.9/recipes1.html#capturing-to-a-network-stream

This script will control the PiZero for the nerf blaster gun.

Pin 18 is used for a RESET signal to force reset the pi if it crashes,
disconnects etc...

pin 22 is used as the gun control signal. This will turn on/off a
transistor which will enable/disable operation of the gun.
'''

import time
import socket
import RPi.GPIO as gpio
from picamera import PiCamera
import os
import io
import struct

BUFFER = 1024  # buffer for incoming data
DATA_PORT = 9696  # port used to recieve data about when to operate the gun
CAMERA_PORT = 6969  # port used to send camera images
BOUNCE_TIME = 2000
RESET_PIN = 18
GUN_CONTROL_PIN = 22

# ignore all warnings regarding the pins being in use as we dont care
gpio.setwarnings(False)

# set reset pin
gpio.setmode(gpio.BCM)
gpio.setup(GUN_CONTROL_PIN, gpio.OUT)
gpio.setup(RESET_PIN, gpio.IN, pull_up_down=gpio.PUD_UP)


# function for restarting the pi
def Restart(channel):
    print("System GPIO reboot event. The system is rebooting NOW!")
    time.sleep(1)
    os.system("sudo shutdown -r now")


# add the pi restart event
gpio.add_event_detect(RESET_PIN,
                      gpio.FALLING,
                      callback=Restart,
                      bouncetime=BOUNCE_TIME)

# Connect a camera client socket
camera_socket = socket.socket()

# establish camera socket - retries until successful
connected = False
while not connected:
    try:
        camera_socket.connect(('192.168.4.1', CAMERA_PORT))
        connected = True
        print("Connected!")
        break
    except Exception as e:
        print("Failed to connect: " + format(e) + " retrying...")
        time.sleep(1)
        pass

# Connect a client socket for receiving data
data_socket = socket.socket()

# establish a data receiving socket - retries until successful
connected = False
while not connected:
    try:
        data_socket.connect(('192.168.4.1', DATA_PORT))
        connected = True
        print("Connected!")
        break
    except Exception as e:
        print("Failed to connect: " + format(e) + " retrying...")
        time.sleep(1)
        pass

data_socket.listen(1)
conn, addr = data_socket.accept()

# Make a file-like object out of the connection
connection = camera_socket.makefile('wb')
try:
    with PiCamera() as camera:
        camera.resolution = (640, 480)
        # Start a preview and let the camera warm up for 2 seconds
        camera.start_preview()
        time.sleep(2)
        # Note the start time and construct a stream to hold image data
        # temporarily (we could write it directly to connection but in this
        # case we want to find out the size of each capture first to keep
        # our protocol simple)
        start = time.time()
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'jpeg'):
            # Write the length of the capture to the stream and flush to
            # ensure it actually gets sent
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            # Rewind the stream and send the image data over the wire
            stream.seek(0)
            connection.write(stream.read())
            # If we've been capturing for more than 30 seconds, quit
            if time.time() - start > 30:
                break
            # Reset the stream for the next capture
            stream.seek(0)
            stream.truncate()

            # check the data being received from the base
            data = conn.recv(BUFFER)
            print("Received: ", data)
            if data == 1:
                gpio.out(GUN_CONTROL_PIN, 1)
            elif data == 0:
                gpio.out(GUN_CONTROL_PIN, 0)

    # Write a length of zero to the stream to signal we're done
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    camera_socket.close()
    data_socket.close()
