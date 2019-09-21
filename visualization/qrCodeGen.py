import pyqrcode
import json

from pyqrcode import QRCode

from rand_item_generator import rand_item_generator

def add_item(rd_item, last=None):
  end = str()
  if last is None:
    end = ',\n'
  return (rd_item.get_item() + end)

def generateReceiptData(num_items=3):
  output_str = str()
  output_str += '[\n'
  rd_item =rand_item_generator()
  for index in range(0,num_items-1):
    output_str += add_item(rd_item)
  output_str += add_item(rd_item, last=True)
  output_str += "\n]"
  print(output_str)
  return output_str

def generateQR(file_name, receipt_string) :
  print("generating qr code ...")
  receipt = pyqrcode.create(receipt_string)#, error='L')
  receipt.png(file_name, scale=5)
  print("generating png")

def main():
  print("starting test script")
  file_name = "test.png"
  generateQR(file_name, generateReceiptData())

if __name__ == "__main__":
  main()