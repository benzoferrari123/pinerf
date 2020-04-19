# Design PDF

This document explains the full electronic design process from learning about the Infinus Nerf electronic system to developing the electronic solution to meet our goal of allowing the gun to fire only when a face is detected. The document includes pictures, elements of the product’s patent filing, drawings, and basic schematics

# Simulation

This folder contains simulations of the main electronic solution used for this project. The bottom ciruit represents the voltage regulator used to get a usable voltage level for the Raspberry Pi from the batteries. The location of the voltage reference is where this system would connect to the Raspberry Pi. The circuit on top represents the switch system that is a desired alternative to the BJT system that had been tested before the hardware component of the project was disontinued. The location of the voltage reference on this part of the circuit represents the lead that would connect to the main circuit board for the Nerf gun, instructing the gun to fire. The 4 different states of the trigger/face detection system can be tested as follows while running simulation:

Left switch off & right switch off - No face detected and trigger not pulled -> Do not fire
Left switch on & right switch off - Face detected and trigger not pulled -> Do not fire
Left switch off & right switch on - No face detected and trigger pulled -> Do not fire
Left switch on & right switch on - Face detected and trigger pulled -> Fire

# Authors
CaesarBonsai - Andrew Benton
