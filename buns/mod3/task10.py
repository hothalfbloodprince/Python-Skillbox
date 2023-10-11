size = int(input())
line = [str(i) for i in range(1, size + 1)]

for i in range(1, size + 1):
    print(', '.join(line))
print()

for i in range(1, size + 1):
    for j in range(1, size + 1):
        if j != size:
            print(i, end=', ')
        else:
            print(i)
