# Gun Scripts
The script in here is used as the controller for the PiZero connected to the Gun. This script serves two functions: sending camera data to the base turret and receiving data from the turret to control the Gun.

This script creates a socket connection with the Turret Base which acts as a socket server. The camera connected to the PiZero is used and the incoming camera data is sent over this socket on a predefined port.

Once the turret base receives the camera data, it will perform any processing on the image and will respond with either a '0' (face not reconised) or a '1' (face recognised). This signal is used to either switch on or off a data pin on the PiZero which will turn on/off a transistor.

Additionally, incase the PiZero crashes, a pin is used for a reset signal so that the gun does not need to be opened to reset the microcontroller. The gun peforms no processing on the image.

# Testing Scripts
Unit tests are included for this script. The script is modified to remove all interface with the Pi as it is a purely software test. This script tests the socket connections.

This script uses the host PCs webcam instead of the Pi camera to send the data signal. 

A mock 'server' has been included. This receives the data from the webcam and simply shows it on the screen. It also sends some sample data back to the gun to test that the gun can also receive data, as well as send it. 

Both scripts should be ran on the same computer, with the server script ran first, then the test gun controller.

# Authors
iShauny - Shaun Loughery
