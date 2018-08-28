import traceback
import logging


class BarCode:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info('Starting')
        self.barcode_list = []

    def add_product(self):
        try:
            barcode = input('Pass the product: ')
            self.logger.info('Barcode scanned: ' + barcode)
            self.barcode_list.append(barcode)
        except:
            self.logger.error('Unexpected error: ' + traceback.format_exc())
            raise

    def clear_product_list(self):
        self.barcode_list.clear()

    def get_product_list(self):
        return self.barcode_list
