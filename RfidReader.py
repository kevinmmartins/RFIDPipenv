import serial
import RPi.GPIO as GPIO
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(23, False)
GPIO.output(24, False)
PortRF = serial.Serial('/dev/ttyAMA0', 9600)

while True:
    ID = ""
    read_byte = PortRF.read()
    if read_byte == "\x02":
        for Counter in range(12):
            read_byte = PortRF.read()
            ID += str(read_byte)
            logger.info(hex(ord(read_byte)));
        logger.info(ID);
