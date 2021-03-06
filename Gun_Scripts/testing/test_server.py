"""
Author: Shaun Loughery

Credit to:
https://gist.github.com/kittinan/e7ecefddda5616eab2765fdb2affed1b

 This script acts as a test 'server' for the test gun controller script

"""

import socket
import cv2
import pickle
import struct

HOST = '127.0.0.1'
CAMERA_PORT = 6969

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created')

socket.bind((HOST, CAMERA_PORT))

print('Socket bind complete')

socket.listen(1)
print('Socket now listening')

conn, addr = socket.accept()

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))

while True:
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += conn.recv(4096)

    print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow('ImageWindow', frame)
    # test sending data
    conn.send(b'1')
    cv2.waitKey(1)
