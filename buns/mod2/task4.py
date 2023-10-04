number = input()

if not number.isdigit() or int(number) < 1:
    print('Неверный ввод')

binary = ''
octal = ''
hexadecimal = ''
hexadecimal_digits = "0123456789ABCDEF"

digit = int(number)
while digit > 0:
    binary = str(digit % 2) + binary
    digit //= 2

digit = int(number)
while digit > 0:
    octal = str(digit % 8) + octal
    digit //= 8

digit = int(number)
while digit > 0:
    remainder = digit % 16
    hexadecimal = hexadecimal_digits[remainder] + hexadecimal
    digit //= 16

print(binary, octal, hexadecimal, sep=', ')