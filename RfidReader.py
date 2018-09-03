from BarCode import BarCode
from Rfid import Rfid

def main():
    while True:
        reader= Rfid()
        barcodeStore= BarCode()
        reader.read()
        barcodeStore.add_product()

if __name__ == "__main__":
    main()


