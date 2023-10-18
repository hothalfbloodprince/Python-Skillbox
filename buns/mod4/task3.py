def algorithm_euclid(a, b):
    if a == b:
        return a

    if a > b:
        return algorithm_euclid(a - b, b)

    return algorithm_euclid(a, b - a)

print(algorithm_euclid(int(input()), int(input())))