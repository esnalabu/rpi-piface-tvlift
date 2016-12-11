#!/bin/python3
# Author: Anders Myren
# This script is for controlling a Venset TV-lift using power from an USB-port as trigger. Add a pulldown resistor between inputpin and common/ground/0V.

import pifacedigitalio as p
from time import sleep

# Set input and output pins
inputpin = 0	# Pin used for triggering lift
raisepin = 0	# Pin used for raising lift
lowerpin = 0	# Pin used for lowering lift

# Set default position and operating variables
raiseduration = 3	# The time lift uses to reach to appropriate height
lowerduration = 3	# The time lift uses from raised position to lowered position
usb_status = 1		# Input of piface is active low, so this sets default usb_status to active indicating connected . I recommend connecting rpi/piface to a USB-port with no power when setting up to avoid raising an already raised lift.

# Define functions raising and lowering TV-lift
def raise_lift():
    print("Raising TV-lift for ", raiseduration, "s..."  )
    p.digital_write(raisepin,1)
    sleep(raiseduration)
    p.digital_write(raisepin,0)
    print("Done raising TV-lift!"  )

def lower_lift():
    print("Lowering TV-lift for ", lowerduration, "s..."  )
    p.digital_write(lowerpin,1)
    sleep(raiseduration)
    p.digital_write(lowerpin,0)
    print("Done lowering TV-lift!"  )

# Run, check for new status, raise/lower on change, sleep for stability
if __name__ == "__main__":
    p.init()					# Start interfacing with piface
    pifacedigital = p.PiFaceDigital()		# Set piface address
    p.core.digital_write_pullup(inputpin,0,0)	# Disable internal pullup resistor since we're using an "external" pulldown resistor

    while(True):
        new_status = p.digital_read(inputpin)
        if new_status != usb_status:
            if new_status == 0:
                raise_lift()
                sleep(3)
            elif new_status == 1:
                lower_lift()
                sleep(3)
        usb_status = new_status
