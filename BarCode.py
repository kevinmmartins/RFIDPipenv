import traceback
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Starting');

while True:
    try:
        barcode = input('Pass the product: ');
        logger.info('Barcode scanned: '+ barcode);
    except:
        logger.error('Unexpected error: ' + traceback.format_exc());
        raise
    
