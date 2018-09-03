import serial
import logging
import traceback


class Rfid(object):
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info('Starting...')
        self.port_rf = serial.Serial('/dev/serial0',115200)
        self.logger.info('Setup completed successfully !')

    def read(self):
        try:
            id = ""
            read_byte = self.port_rf.read()
            if read_byte == "\x02":
                for bits in range(12):
                    read_byte = self.port_rf.read()
                    id += str(read_byte)
                    self.logger.info(hex(ord(read_byte)))
                self.logger.info(id)
        except:
            self.logger.error('Unexpected error: ' + traceback.format_exc())
            raise
