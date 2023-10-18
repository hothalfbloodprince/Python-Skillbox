#filename = input()
filename = 'task5_input.txt'

with open(filename, 'r') as f:
    text = f.read()

letter_count = {}
for letter in text:
    if letter.isalpha(): #из задачи не совсем поняла что в файле содержится, поэтому решила, что не только буквы
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1])

with open('task5_output.txt', 'w') as f:
    for letter, count in sorted_letter_count:
        f.write(f"{letter}: {count}\n")