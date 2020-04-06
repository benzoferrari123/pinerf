# Facial Recognition Nerf Blaster Locking System - pinerf
This application uses a Raspberry Pi and Raspberry Pi Zero to recognise authorized faces for the use of a Nerf Elite Infinus Blaster.

The low power Pi Zero captures images through it's own camera and transmits them to the base station. The base station will perform the facial recognition algorithm and will send a signal back to the Pi Zero once it has successfully identified a face. This will 'unlock' the gun and allow it to be used.

The scripts for the Nerf Gun will be created using Python as it provides a better interface for the camera. All of the main processing will be done on the Turret Base and is created using C++.

# Contributers
benzoferrari123 - Ben Hanmer - Turret Base Pi Scripts

iShauny - Shaun Loughery - Gun Control Scripts

LShaw1872 - Lewis Shaw - 3D Modelling Design

CaesarBonsai - Drew Benton - Electronic Circuit Design
