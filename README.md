# Facial Recognition Nerf Blaster Locking System - PiNerf

![PiNerf System](/Documentation/pinerf.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This application uses a Raspberry Pi and Raspberry Pi Zero to recognise authorized faces for the use of a Nerf Elite Infinus Blaster.

The low power Pi Zero captures images through it's own camera and transmits them to the base station. The base station will perform the facial recognition algorithm and will send a signal back to the Pi Zero once it has successfully identified a face. This will 'unlock' the gun and allow it to be used.

The scripts for the Nerf Gun will be created using Python as it provides a better interface for the camera. **All of the main processing will be done on the Turret Base and is created using C++.**

# Usage
This project uses two Rasbperry Pis. One must be embeded within the gun itself and another located attached to a turret base.

Each script has been split into different folders. The gun controller script **must** be loaded onto the Pi that is embedded within the gun. It is advised that the script be set as a **system service** that automatically starts when the Pi turns on.

The turret base scripts **must** be loaded onto the Pi that is connected to the turret base. The scripts here will perform **all** of the key image processing/facial recognition.

Both of these Pis **must** be connected on the same network, along with any computer system used for debugging/verification. Advice has also been given on how to secure the system to prevent unauthorised access to the network. Any input/output pins required on the Pis will be listed in the appropriate files.

The 3D model which can be found must be printed if a custom turret mount is desired. The electrionic ciruit design that accompanies the Pi in the gun can also be found along with documentation instructing how it can be connected.

Each folder for each part of the project will have further information, where appropriate, explaining more about how to use it.

# Social Media

https://twitter.com/pi_nerf

# Contributers
benzoferrari123 - Ben Hanmer - Turret Base Pi Scripts

iShauny - Shaun Loughery - Gun Control Scripts

LShaw1872 - Lewis Shaw - 3D Modelling Design

CaesarBonsai - Drew Benton - Electronic Circuit Design
