def power(a, n):
    if n == 0:
        return 1

    if a % 2:
        return a * power(a, n - 1)

    return a * power(a ** 2, n / 2)

print(power(int(input()), int(input())))