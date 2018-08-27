import serial
import logging
import traceback


class Rfid:
    def __init__(self):
        logging.basicConfig(level=logging.INFO);
        self.logger = logging.getLogger(__name__);
        self.logger.info('Starting...');
        self.portRF = serial.Serial('/dev/serial0', 115200)
        self.logger.info('Setup completed successfully !');

    def read(self):
        try:
            while True:
                id = ""
                read_byte = self.portRF.read();
                if read_byte == "\x02":
                    for Counter in range(10):
                        read_byte = self.portRF.read();
                        id += str(read_byte);
                    self.logger.info(id);
        except:
            self.logger.error('Unexpected error: ' + traceback.format_exc());
            raise;
