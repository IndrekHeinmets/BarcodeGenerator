from barcode.writer import ImageWriter
from barcode import EAN13


def check_num(num):
    if len(str(num)) == 12 and all(char.isdigit() == True for char in str(num)):
        return True
    print('\nVale formaat või pikkus!')
    return False


def num_to_code(num):
    return EAN13(str(num), writer=ImageWriter())


def main():
    while True:
        number = input("\nSisesta number: ")
        if check_num(number):
            num_to_code(number).save('Ribakood')
            break


if __name__ == '__main__':
    main()