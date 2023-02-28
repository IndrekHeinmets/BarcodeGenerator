from barcode.writer import ImageWriter
from barcode import EAN13

# number = '9021230168366'

number = input("Enter the number: ")

def num_to_code(num):
    code = EAN13(num, writer=ImageWriter())
    return code

def main():
    my_code = num_to_code(number)
    my_code.save("codes\\code2")