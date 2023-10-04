side_length = float(input())
P = side_length * 4
S = side_length ** 2
d = (S * 2) ** 0.5

print(round(P, 2), round(S, 2), round(d, 2), sep=', ')