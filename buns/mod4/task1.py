input_numbers = input().split()
repeating_numbers = [number for number in input_numbers if input_numbers.count(number) > 1]
if (input_numbers == repeating_numbers):
    print('Все числа равны')
elif (len(repeating_numbers) == 0):
    print('Все числа разные')
else:
    print('Есть равные и неравные числа')