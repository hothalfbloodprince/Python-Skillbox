with open('task9_input.txt', 'r') as f:
    N = int(f.readline())

x = 0
y = 0
dx = 0
dy = -1
steps = 1

while steps <= N:
    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
        dx, dy = -dy, dx
    x, y = x + dx, y + dy
    steps += 1

with open('task9_output.txt', 'w') as f:
    f.write(str(-x) + ' ' + str(-y))