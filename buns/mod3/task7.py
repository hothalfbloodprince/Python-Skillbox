input_numbers = input().split()
repeating_numbers = [number for number in input_numbers if input_numbers.count(number) > 1]
print(repeating_numbers != [])