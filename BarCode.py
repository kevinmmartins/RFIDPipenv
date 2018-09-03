import traceback
import logging


class BarCode(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info('Starting..')
        self.barcode_list = []
        self.logger.info('Setup completed successfully !')

    def add_product(self):
        try:
            barcode = input()
            self.logger.info('Barcode scanned: ' + barcode)
            self.barcode_list.append(barcode)
            self.logger.info(self.barcode_list)
        except:
            self.logger.error('Unexpected error: ' + traceback.format_exc())
            raise

    def clear_product_list(self):
        self.barcode_list.clear()

    def get_product_list(self):
        self.logger.info(self.barcode_list)
        return self.barcode_list
