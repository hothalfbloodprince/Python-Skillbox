string = input()
string = string.replace(' ', '')
vowels = 'яаыуеэоиюё'
consonants = 'йцкнгшщзхфвпрлджбтмсч'
count_vow, count_cons = 0, 0

for i in range(len(string)):
    if string[i] in vowels:
        count_vow += 1
    elif string[i] in consonants: #помним про ъ,ь, поэтому elif
        count_cons += 1

print(count_vow, count_cons, sep=' ')