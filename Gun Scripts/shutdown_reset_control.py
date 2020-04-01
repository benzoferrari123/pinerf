# https://www.hackster.io/glowascii/raspberry-pi-shutdown-restart-button-d5fd07

import RPi.GPIO as gpio
import time
import os

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)


def Restart(channel):
    print("System GPIO reboot event. The system is rebooting NOW!")
    time.sleep(1)
    os.system("sudo shutdown -r now")


gpio.add_event_detect(18, gpio.FALLING, callback=Restart, bouncetime=2000)

while True:
    time.sleep(1)