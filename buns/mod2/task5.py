couple = input()
i = couple[0]
n = int(couple[3:])
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = (alphabet.index(i) + n) % len(alphabet)

print(alphabet[index])