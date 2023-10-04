numbers = input()
numbers = numbers.replace(' ', '')
flag = False

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            flag = True
            break
    if flag:
        break

print(flag)