import pyqrcode

from pyqrcode import QRCode

def generateReciptData(file_name, recipt_string) :
  print("generating qr code ...")
  recipt = pyqrcode.create(recipt_string)
  recipt.png(file_name, scale=5)
  print("generating png")

# def main():
#   print("starting test script")
#   file_name = "test.png"
#   generateReciptData(file_name, "hello, world!")

# if __name__ == "__main__":
#   main()