decimal = input()

if not decimal.isdigit() or int(decimal) < 1:
    print('Неверный ввод')

binary = ''
octal = ''
hexadecimal = ''
hexadecimal_alphabet = "0123456789ABCDEF"

number = int(decimal)
while number > 0:
    binary = str(number % 2) + binary
    number //= 2

number = int(decimal)
while number > 0:
    octal = str(number % 8) + octal
    number //= 8

number = int(decimal)
while number > 0:
    remainder = number % 16
    hexadecimal = hexadecimal_alphabet[remainder] + hexadecimal
    number //= 16

print(binary, octal, hexadecimal, sep=', ')