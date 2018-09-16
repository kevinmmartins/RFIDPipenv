#!/usr/bin/env python

import serial

class Rfid(object):
    
    def __init__(self):
        self.PortRF = serial.Serial('/dev/serial0', 9600)
    
    def read_serial(self):
        print "Pass the card"
        ID = ""
        read_byte=""
        while read_byte!="\x02":
            read_byte = self.PortRF.read()
        for Counter in range(12):
            read_byte=self.PortRF.read()
            ID = ID + str(read_byte)
        return ID
    
    def close_serial(self):
        self.PortRF.flush()
        self.PortRF.flushInput()
        self.PortRF.flushOutput()
        self.PortRF.close()
