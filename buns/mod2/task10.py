words = input()
word = ''

for i in range(len(words)):
    char = words[i]
    if char == ' ':
        word += words[i - 1]

word += words[-1]

print(word)