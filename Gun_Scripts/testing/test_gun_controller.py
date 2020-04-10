'''
Author: Shaun Loughery

Credit:
https://picamera.readthedocs.io/en/release-1.9/recipes1.html#capturing-to-a-network-stream
https://gist.github.com/kittinan/e7ecefddda5616eab2765fdb2affed1b

This script is a modified version of the gun controller script used for
testing verification.

All interfaces with the Pi have been removed.
This test is to verify the operation of the Socket connections to ensure
the camera data is sent.
'''

import time
import socket
import struct
import cv2
import pickle

BUFFER = 1024  # buffer for incoming data
CAMERA_PORT = 6969  # port used to send camera images
BOUNCE_TIME = 2000
RESET_PIN = 18
GUN_CONTROL_PIN = 22
TURRET_BASE_IP = '127.0.0.1'

# Connect a camera client socket
camera_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish camera socket - retries until successful
connected = False
while not connected:
    try:
        camera_socket.connect((TURRET_BASE_IP, CAMERA_PORT))
        connected = True
        print("Connected!")
        break
    except Exception as e:
        print("Failed to connect: " + format(e) + " retrying...")
        time.sleep(1)
        pass

# Make a file-like object out of the connection
connection = camera_socket.makefile('wb')
cam = cv2.VideoCapture(0)
cam.set(3, 320)
cam.set(4, 240)
img_counter = 0
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
try:
    while True:

        ret, frame = cam.read()
        result, frame = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(frame, 0)
        size = len(data)

        print("{}: {}".format(img_counter, size))
        camera_socket.sendall(struct.pack(">L", size) + data)
        img_counter += 1

        # check the data being received from the base
        data = camera_socket.recv(BUFFER)
        print("Received: ", data)

finally:
    connection.close()
    camera_socket.close()
