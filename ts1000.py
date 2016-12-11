#!/bin/python3

import pifacedigitalio as p
from time import sleep

raiseduration = 3
lowerduration = 3
position = 0

def raise_lift(event):
    print("Raising TV-lift for ", raiseduration, "s..."  )
    event.chip.output_pins[0].turn_on()
    sleep(raiseduration)
    event.chip.output_pins[0].turn_off()
    print("Done raising TV-lift!"  )

def lower_lift(event):
    print("Lowering TV-lift for ", lowerduration, "s..."  )
    event.chip.output_pins[1].turn_on()
    sleep(raiseduration)
    event.chip.output_pins[1].turn_off()
    print("Done lowering TV-lift!"  )
    

if __name__ == "__main__":
    
    pifacedigital = p.PiFaceDigital()
    inputpin = 0

    listener = p.InputEventListener(chip=pifacedigital)
    listener.register(inputpin, p.IODIR_OFF, raise_lift)
    listener.register(inputpin, p.IODIR_ON, lower_lift)
    listener.activate()

