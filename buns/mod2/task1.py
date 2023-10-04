numbers = input()
counter, first_number = 0, 0

while numbers[counter] != ',':
    first_number *= 10
    first_number += float(numbers[counter])
    counter += 1

second_number = float(numbers[counter + 1:])
operation = first_number % second_number

if operation % 1 == 0:
    print(round(operation))
else:
    print(operation)