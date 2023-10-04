code = input()
sum_even, sum_odd = 0, 0

for i in range(len(code)):
    digit = int(code[i])
    if i % 2 == 0:
        sum_odd += digit
    else:
        sum_even += digit

if (sum_odd + sum_even * 3) % 10 == 0:
    print('yes')
else:
    print('no')