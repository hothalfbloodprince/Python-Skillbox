s = input()
i = s[-1]
counter = 0
s = s[:-2]

while s[counter] == i:
    counter += 1

print(counter)