from barcode.writer import ImageWriter
from barcode import EAN13

    
def check_num(num):
    if len(str(num)) not in [12, 13]:
        if not str(num).isdigit():
            print('\nVale Formaat ja Pikkus! (12-13 numbrit)')
        else:
            print('\nVale Pikkus! (12-13)')
        return False
    elif not str(num).isdigit():
        print('\nVale Formaat (numbrid)!')
        return False
    else:
        return True


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