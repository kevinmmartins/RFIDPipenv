#!/usr/bin/env python

import serial

def read_serial():
    PortRF = serial.Serial('/dev/serial0', 9600)
    while True:
        ID = ""
        read_byte = PortRF.read()
        if read_byte=="\x02":
            for Counter in range(12):
                read_byte=PortRF.read()
                ID = ID + str(read_byte)
            return ID
