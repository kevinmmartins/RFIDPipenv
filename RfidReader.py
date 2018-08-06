import serial
import RPi.GPIO as GPIO
import logging
import traceback

logging.basicConfig(level=logging.INFO);
logger = logging.getLogger(__name__);
logger.info('Starting...');
PortRF = serial.Serial('/dev/ttyAMA0', 9600)

logger.info('Setup completed successfully !');

while True:
    try:
        ID = ""
        read_byte = PortRF.read();
        if read_byte == "\x02":
            for Counter in range(12):
                read_byte = PortRF.read();
                ID += str(read_byte);
                logger.info(hex(ord(read_byte)));
            logger.info(ID);
    except:
        logger.error('Unexpected error: ' + traceback.format_exc());
        raise;
