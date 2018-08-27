import traceback
import logging


class BarCode:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info('Starting');

    def get_product_code(self):
        while True:
            try:
                barcode = input('Pass the product: ');
                self.logger.info('Barcode scanned: ' + barcode);
            except:
                self.logger.error('Unexpected error: ' + traceback.format_exc());
                raise
