from BarCode import BarCode
from Rfid import Rfid

if __name__ == "__main__":
    while True:
        reader= Rfid()
        barcodeStore= BarCode()
        reader.read()
        barcodeStore.add_product()

