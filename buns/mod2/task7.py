string = input()
counter0, counter1 = 0, 0

for i in range(len(string)):
    if string[i] == '0':
        counter0 += 1
    else:
        counter1 += 1

if counter0 == counter1:
    print('yes')
else:
    print('no')