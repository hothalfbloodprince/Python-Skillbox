number = input()
chars ='+0123456789'
new_number = ''

for i in range(len(number)):
    if number[i] in chars:
        new_number += number[i]

print(new_number)