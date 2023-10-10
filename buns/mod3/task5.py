input_string = input()
count_one, count_zero = input_string.count('1'), input_string.count('0')
print('yes' if count_one == count_zero else 'no')